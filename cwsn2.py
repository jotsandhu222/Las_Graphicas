import pygame
import pyttsx3
import os
import string
import random
import time
import json

# === Init Text To Speech ===
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# === Init Pygame ===
pygame.init()
screen = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Sign Language Game")
font = pygame.font.SysFont(None, 48)

image_folder = "sign_images"
data_file = "student_progress.json"

# === Load or create student data ===
def load_data():
    if os.path.exists(data_file):
        with open(data_file, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(data_file, "w") as f:
        json.dump(data, f, indent=4)


def pygame_login():
    input_text = ""
    running = True

    while running:
        screen.fill((0, 0, 0))
        prompt = font.render("Enter your name and press ENTER:", True, (255, 255, 255))
        user_input_surface = font.render(input_text, True, (0, 255, 0))
        screen.blit(prompt, (50, 200))
        screen.blit(user_input_surface, (50, 300))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    name = input_text.strip().lower()
                    if name:
                        return name

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

                else:
                    if event.unicode.isprintable():
                        input_text += event.unicode

# === Login ===
def login():
    name = pygame_login()
    data = load_data()
    if name not in data:
        print(f"New student: {name}")
        data[name] = {}
        for ch in string.ascii_lowercase:
            data[name][ch] = {"correct": 0, "wrong": 0}
        save_data(data)
    else:
        print(f"Welcome back, {name}!")
    return name



# GameMode === Function to Show Letter and Speak ===
def show_and_speak(letter):
    screen.fill((0, 0, 0))
    image_path = os.path.join(image_folder, f"{letter.upper()}.jpg")
    
    if os.path.exists(image_path):
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (1280, 720))
        screen.blit(image, (0, 0))
    else:
        text = font.render(f"No image for {letter.upper()}", True, (255, 0, 0))
        screen.blit(text, (50, 180))
    
    pygame.display.flip()
    engine.say(f"Press the letter {letter.upper()}")
    engine.runAndWait()
    
    
# === Feedback ===
def display_feedback(message, color=(0, 255, 0)):
    screen.fill((0, 0, 0))
    text = font.render(message, True, color)
    screen.blit(text, (100, 180))
    pygame.display.flip()
    time.sleep(1)
    
# === Weighted letter selection ===
def choose_letter(student_data):
    weights = []
    letters = list(string.ascii_lowercase)
    for ch in letters:
        wrong = student_data[ch]["wrong"]
        correct = student_data[ch]["correct"]
        weight = 1 + wrong - 0.3 * correct  # base 1, encourage wrongs
        weight = max(0.1, weight)
        weights.append(weight)
    return random.choices(letters, weights=weights, k=1)[0]
    
# NormalMode function to speak word and display pic  
def speak_and_show(letter):
    print(f"Pressed: {letter.upper()}")
    
    
    engine.say(f"{letter.lower()}")
    engine.runAndWait()

    image_path = os.path.join(image_folder, f"{letter.upper()}.jpg")
    # image available 
    if os.path.exists(image_path):
        image = pygame.image.load(image_path)
        image = pygame.transform.scale(image, (1280, 720))
        screen.blit(image, (0, 0))
        pygame.display.flip()
    
    # no image available
    else:
        screen.fill((0, 0, 0))
        text = font.render(f"No image for {letter.upper()}", True, (255, 0, 0))
        screen.blit(text, (50, 180))
        pygame.display.flip()


# === Function to Display Feedback ===
def display_feedback(message, color=(0, 255, 0)):
    screen.fill((0, 0, 0))
    text = font.render(message, True, color)
    screen.blit(text, (100, 180))
    pygame.display.flip()
    time.sleep(1)

# Function to speak a full word
def speak_word(word):
    print(f"speaking full word: {word}")
    engine.say(f"the word is {word}")
    engine.runAndWait()

# === Game Loop ===
def game_loop(student_name):
    data = load_data()
    student_data = data[student_name]
    running = True

    current_letter = choose_letter(student_data)
    show_and_speak(current_letter)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            elif event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key).lower()

                if key_name == current_letter:
                    student_data[current_letter]["correct"] += 1
                    display_feedback("Correct!", (0, 255, 0))
                    current_letter = choose_letter(student_data)
                    show_and_speak(current_letter)

                elif key_name == "escape":
                    return "menu"

                elif key_name in string.ascii_lowercase:
                    student_data[current_letter]["wrong"] += 1
                    display_feedback("Try again!", (255, 0, 0))

    save_data(data)
    return "menu"


# NormalMode speak single letter and full word if enter pressed
def normal_mode():
    running = True
    current_word = ""
    word_start_time = None
    word_time_limit = 20
    print("Press a key (A-Z or 0-9). Press ESC to quit.")

    while running:
        current_time = time.time()
        if word_start_time and (current_time - word_start_time > word_time_limit):
            current_word = ""
            word_start_time = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key)

                if key_name in string.ascii_lowercase + string.digits:
                    speak_and_show(key_name)
                    current_word += key_name
                    if not word_start_time:
                        word_start_time = time.time()

                elif event.key == pygame.K_RETURN:
                    if current_word:
                        # Show animation of each letter
                        for letter in current_word:
                            image_path = os.path.join(image_folder, f"{letter.upper()}.jpg")
                            screen.fill((0, 0, 0))
                            if os.path.exists(image_path):
                                image = pygame.image.load(image_path)
                                image = pygame.transform.scale(image, (1280, 720))
                                screen.blit(image, (0, 0))
                            else:
                                text = font.render(f"No image for {letter.upper()}", True, (255, 0, 0))
                                screen.blit(text, (50, 180))
                            pygame.display.flip()

                            engine.say(letter.lower())
                            engine.runAndWait()
                            time.sleep(0.6)

                        speak_word(current_word)

                        # Clear screen after word is spoken
                        screen.fill((0, 0, 0))
                        pygame.display.flip()

                        current_word = ""
                        word_start_time = None


                elif event.key == pygame.K_ESCAPE:
                    running = False

    pygame.quit()

def type_to_sign_mode():
    user_input = input("Type a sentence: ").lower()
    words = user_input.split()

    for word in words:
        for letter in word:
            if letter in string.ascii_lowercase:
                image_path = os.path.join(image_folder, f"{letter.upper()}.jpg")
                screen.fill((0, 0, 0))
                if os.path.exists(image_path):
                    image = pygame.image.load(image_path)
                    image = pygame.transform.scale(image, (1280, 720))
                    screen.blit(image, (0, 0))
                else:
                    text = font.render(f"No image for {letter.upper()}", True, (255, 0, 0))
                    screen.blit(text, (50, 180))
                pygame.display.flip()

                time.sleep(0.5)  # Wait between letters to animate

        # Speak the full word after showing all letters
        engine.say(word)
        engine.runAndWait()

        # Small pause between words
        time.sleep(1)

    # Clear screen at end
    screen.fill((0, 0, 0))
    pygame.display.flip()

def keyboard_to_sign_mode():
    running = True
    screen.fill((0, 0, 0))
    pygame.display.flip()
    print("Live Letter Mode: Press a key (A-Z). ESC to go back.")

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            elif event.type == pygame.KEYDOWN:
                key_name = pygame.key.name(event.key).lower()

                if key_name == "escape":
                    return "menu"

                elif key_name in string.ascii_lowercase:
                    speak_and_show(key_name)

    return "menu"


def type_to_sign_mode():
    running = True
    input_text = ""
    display_text = font.render("Type your sentence and press ENTER", True, (255, 255, 255))

    while running:
        screen.fill((0, 0, 0))
        screen.blit(display_text, (50, 100))
        typed_surface = font.render(input_text, True, (0, 255, 0))
        screen.blit(typed_surface, (50, 200))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text.strip():
                        animate_sentence(input_text.strip())
                        input_text = ""  # Reset for next sentence

                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]

                elif event.key == pygame.K_ESCAPE:
                    return "menu"

                else:
                    if event.unicode.isprintable():
                        input_text += event.unicode

    return "menu"

def animate_sentence(sentence):
    words = sentence.lower().split()

    for word in words:
        for letter in word:
            if letter in string.ascii_lowercase:
                image_path = os.path.join(image_folder, f"{letter.upper()}.jpg")
                screen.fill((0, 0, 0))
                if os.path.exists(image_path):
                    image = pygame.image.load(image_path)
                    image = pygame.transform.scale(image, (1280, 720))
                    screen.blit(image, (0, 0))
                else:
                    text = font.render(f"No image for {letter.upper()}", True, (255, 0, 0))
                    screen.blit(text, (50, 180))
                pygame.display.flip()

                engine.say(letter)
                engine.runAndWait()
                time.sleep(0.4)

        engine.say(word)
        engine.runAndWait()
        time.sleep(1)

    screen.fill((0, 0, 0))
    pygame.display.flip()


def main_loop(student_name):
    current_mode = "menu"

    while True:
        if current_mode == "menu":
            screen.fill((0, 0, 0))
            text = font.render("Press F1=Basic Mode | F2=Game Mode | F3=Advance Mode | ESC=Quit", True, (255, 255, 255))
            screen.blit(text, (50, 300))
            pygame.display.flip()

            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_F1:
                            current_mode = "live"
                            waiting = False
                        elif event.key == pygame.K_F2:
                            current_mode = "game"
                            waiting = False
                        elif event.key == pygame.K_F3:
                            current_mode = "type"
                            waiting = False
                        elif event.key == pygame.K_ESCAPE:
                            return

        elif current_mode == "game":
            result = game_loop(student_name)
            current_mode = result

        elif current_mode == "type":
            result = type_to_sign_mode()
            current_mode = result

        elif current_mode == "live":
            result = keyboard_to_sign_mode()
            current_mode = result

#send report to guardians
import requests

TELEGRAM_TOKEN = '7571524500:AAFSHo8blDwvHvm0AxLSOg7C1SGXwM5MddQ'
CHAT_ID = '6053365697'

def generate_student_report(student_name):
    data = load_data()
    if student_name not in data:
        return "No data found for student."

    student_data = data[student_name]
    report_lines = [f"📊 *Progress Report for {student_name.capitalize()}*"]

    total_correct = 0
    total_wrong = 0
    most_wrong_letter = None
    max_wrong = -1

    for letter, stats in student_data.items():
        correct = stats["correct"]
        wrong = stats["wrong"]
        total_correct += correct
        total_wrong += wrong

        if wrong > max_wrong:
            max_wrong = wrong
            most_wrong_letter = letter

        total = correct + wrong
        accuracy = f"{(correct / total * 100):.1f}%" if total > 0 else "N/A"
        report_lines.append(f"🔠 {letter.upper()}: ✅ {correct} ❌ {wrong} 🎯 Accuracy: {accuracy}")

    total_attempts = total_correct + total_wrong
    overall_accuracy = f"{(total_correct / total_attempts * 100):.1f}%" if total_attempts else "N/A"

    report_lines.append(f"\n📈 Total Attempts: {total_attempts}")
    report_lines.append(f"🎯 Overall Accuracy: {overall_accuracy}")
    if most_wrong_letter:
        report_lines.append(f"⚠️ Most mistakes on: *{most_wrong_letter.upper()}*")

    return "\n".join(report_lines)


def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }

    response = requests.post(url, data=payload)
    if response.status_code != 200:
        print("Failed to send message:", response.text)
    else:
        print("Report sent successfully.")


if __name__ == "__main__":
    student_name = login()
    main_loop(student_name)
    report = generate_student_report(student_name)
    send_telegram_message(report)
    pygame.quit()