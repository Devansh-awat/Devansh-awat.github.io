import pyautogui
import random
import string
import time

def random_text(length):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for _ in range(length))

def main():
    while True:
        text = random_text(random.randint(5, 15))
        pyautogui.typewrite(text)
        pyautogui.press('enter')
        time.sleep(random.uniform(0.5, 2.0))
        pyautogui.moveTo(random.randint(0, 1920), random.randint(0, 1080))
        time.sleep(random.uniform(0.5, 2.0))

if __name__ == "__main__":
    main()
