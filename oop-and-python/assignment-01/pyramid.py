import pyautogui
import time

height = int(input("Enter pyramid height: "))

print("You have 5 seconds to click inside your text editor...")
time.sleep(5)

for i in range(1, height + 1):
    row_text = "#" * i
    pyautogui.typewrite(row_text)
    pyautogui.press("enter")
