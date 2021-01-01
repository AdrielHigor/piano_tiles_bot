from pyautogui import *
import pyautogui
import win32api, win32con
import keyboard
from PIL import ImageGrab

#  (x, y)

first_tile = (390, 390)
second_tile = (460, 390)
third_tile = (525, 390)
fourth_tile = (585, 390)

# list of pixels to be clicked on (r, g, b)
compare_list = ((1,1,1), (0, 2, 4), (255,183,9))

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def verify_pixel(pixel, compare):
    for item in compare:
        if pixel == item:
            return True
        
    return False

while keyboard.is_pressed('esc') == False:

    image = ImageGrab.grab()

    first_tile_pixel = image.getpixel(first_tile)
    second_tile_pixel = image.getpixel(second_tile)
    third_tile_pixel = image.getpixel(third_tile)
    fourth_tile_pixel = image.getpixel(fourth_tile)

    print(first_tile_pixel)
    print(second_tile_pixel)
    print(third_tile_pixel)
    print(fourth_tile_pixel)
    print("====================================")


    if verify_pixel(first_tile_pixel, compare_list):
        click(first_tile[0], first_tile[1] + 30) 
    if verify_pixel(second_tile_pixel, compare_list):
        click(second_tile[0], second_tile[1] + 30)
    if verify_pixel(third_tile_pixel, compare_list):
        click(third_tile[0], third_tile[1] + 30)
    if verify_pixel(fourth_tile_pixel, compare_list):
        click(fourth_tile[0], fourth_tile[1] + 30)
