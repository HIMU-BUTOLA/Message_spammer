#I want to send my friend repetitive message
import pyautogui
import pyperclip
import time

#lets configure 
emoji = "Hi"
count = 10
delay = 1
start_delay = 10

print("Emoji: ",emoji, " Sending ",count, " times")

#copy emoji to clipboard
pyperclip.copy(emoji)

#Starting to send emoji
time.sleep(delay) #giving time delay to open watsapp

try:
    for i in range(count):
        #paste emoji
        pyautogui.hotkey("ctrl","v")

        #send message
        pyautogui.press("enter")

        print("\nMessage {i+1}/{count} sent!")

        time.sleep(delay)
except pyautogui.failSafeException:
    print("Emergency stop avtivated.")

print("Program finished")