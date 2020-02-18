
from ctypes import windll, Structure, c_long, byref
import pyautogui


class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]



def Rechtermuisklik():
    pt = POINT()
    windll.user32.GetCursorPos(byref(pt))
    pyautogui.rightClick(x=pt.x, y=pt.y)

def PaginaSluiten():
    pyautogui.hotkey('ctrl', 'w')  

def Kopiëren():
    pyautogui.hotkey('ctrl', 'c')  

def Plakken():
    pyautogui.hotkey('ctrl', 'v')

def PrintScreen():
    pyautogui.hotkey('ctrl', 'PrtSc') 

def CommandPromptSluiten():
    pyautogui.hotkey("esc")

PrintScreen()
CommandPromptSluiten()