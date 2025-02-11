import pyautogui
import time
import cv2
import time
from PIL import Image
import pytesseract

time.sleep(5)

img = "test1.png"
input_img = "input.png" 
scroll_attempts = 0
max_scroll_attempts = 20

def find_and_click(img, scroll_attempts, max_scroll_attempts):
    while True:
        if scroll_attempts >= max_scroll_attempts:
            print("Không thể cuộn thêm, thoát vòng lặp.")
            break
        try:
            locations = list(pyautogui.locateAllOnScreen(img, confidence=0.8))
            if locations:
                for location in locations:
                    pyautogui.click(pyautogui.center(location))
                    time.sleep(0.2)
                    print(f"Clicked at: {location}")
                scroll_attempts = 0
                pyautogui.scroll(-800)
                time.sleep(0.2)
                scroll_attempts += 1
        except Exception:
            print("End! fac")
            break

def find_and_type(input_img):
    input_locations = list(pyautogui.locateAllOnScreen(input_img, confidence=0.8))
    print(input_locations)
    try:
        if input_locations:
            for il in input_locations:
                pyautogui.click(pyautogui.center(il))
                pyautogui.sleep(0.2)
                pyautogui.write("No")
                pyautogui.sleep(0.2)
    except Exception:
        print("End! fat")

find_and_click(img, scroll_attempts, max_scroll_attempts)
find_and_type(input_img)






