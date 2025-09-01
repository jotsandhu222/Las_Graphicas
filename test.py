import formulas
import time

formulas.circle(3.5)

def time_sleep(i):
    count = 0
    samay = time.time()
    for _ in range(i*5):
        samay_latest = time.time() - samay + 1
        time.sleep(0.2)
        print(f"time since waiting: {samay_latest}")
        count += 1
        print(f"times checked: {count}")

def time_sleep0(i):
    count = 0
    samay = time.time()
    while True:
        samay_latest = time.time() - samay
        if samay_latest > 10:
            break
        else:
            count += 1
            print(count)

time_sleep(10)

	