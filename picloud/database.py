import aiosqlite
import os

DB_FILE = "picloud.db"

async def init_db():
    async with aiosqlite.connect(DB_FILE) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            )
        ''')
        # Check if default user exists
        cursor = await db.execute("SELECT * FROM users WHERE username = 'admin'")
        user = await cursor.fetchone()
        if not user:
            # Default password is 'admin', in a real app this should be forced to change
            from passlib.context import CryptContext
            pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
            hashed_password = pwd_context.hash("admin")
            await db.execute(
                "INSERT INTO users (username, password_hash) VALUES (?, ?)",
                ("admin", hashed_password)
            )

        await db.commit()

async def get_db():
    db = await aiosqlite.connect(DB_FILE)
    try:
        yield db
    finally:
        await db.close()
