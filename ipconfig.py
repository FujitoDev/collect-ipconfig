import pyautogui as pag
import time

pag.PAUSE = 0.22
pag.hotkey("win", "r")
pag.write("cmd")
pag.press("enter")
pag.write("ipconfig")
pag.press("enter")
pag.write("ipconfig | findstr /i ""IPv4"" | clip")
pag.press("enter")
pag.hotkey("alt", "F4")