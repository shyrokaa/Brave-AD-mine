import pyautogui
import time
import subprocess
import keyboard

def loop(path):
    time.sleep(2)
    subprocess.call([path])
    file1 = open('alphabet.txt', 'r')
    Lines = file1.readlines()

    for line in Lines:
        time.sleep(1)
        a = line.strip()
        pyautogui.typewrite(a)
        pyautogui.press('enter')

        time.sleep(1)
        keyboard.press_and_release('ctrl+t')
        keyboard.press_and_release('ctrl+tab')
        keyboard.press_and_release('ctrl+w')

def main():

    print("\t\t\t Brave Browser ad auto-miner by Shyrokaa")
    print("\n\n\n\n (Help: the path should look like this C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe . type start on command section to mine   ")
    path = input("path to browser>")
    minutes = input("minutes>")
    controller = input("command>")
    timeout = time.time() + 60 * float(minutes)
    while True:
        if time.time() > timeout:
            break
        if controller == "start":
            print("mining diamonds...")
            loop(path)
            keyboard.press_and_release('ctrl+w')
        else:
            print("!incorrect input!")
    print("mining complete. go count your money")

main()
input('Press ENTER to exit')