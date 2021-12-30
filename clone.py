import pyautogui
import time
import subprocess
import keyboard
from pathlib import Path


def loop(path):
    print("rock found")
    time.sleep(2)


    my_file = Path('alphabet.txt')
    if my_file.is_file():
        print("path exists!")
    else:
        print("path does not exist -> restart program")

    file1 = open('alphabet.txt', 'r')
    Lines = file1.readlines()

    for line in Lines:
        subprocess.call([path])
        a = line.strip()
        #pyautogui.typewrite(a)
        #pyautogui.press('enter')
        print(a)
        time.sleep(3)
        keyboard.press_and_release('ctrl+w')
        time.sleep(3)


def main():
    print("\t\t\t Brave Browser ad auto-miner by Shyrokaa")
    print(
        "\n\n\n\n (Help: the path should look like this C:\Program "
        "Files\BraveSoftware\Brave-Browser\Application\\brave.exe . type start on command section to mine   ")
    path = input("path to browser>")
    my_file = Path(path)
    if my_file.is_file():
        print("path exists!")
    else:
        print("path does not exist -> restart program")
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
