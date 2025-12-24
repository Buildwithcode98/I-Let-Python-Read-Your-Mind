import time
import pyautogui
import keyboard
import pyperclip

# Store the program's own source code as a string
code = 'paste the code here with the tripple_quote '

print("Click inside VS Code editor in 3 seconds...")
time.sleep(3)

for char in code:
    if keyboard.is_pressed("esc"):
        print("Typing stopped.")
        break

    if char == '\n':
        pyautogui.press('enter')
    else:
        pyerclip.copy(char)
        pyautogui.hotkey('ctrl', 'v')
