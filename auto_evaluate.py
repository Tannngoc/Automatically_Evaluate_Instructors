import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import easyocr

reader = easyocr.Reader(['en'])


time.sleep(2)

select_img = "test1.png"
input_img = "input.png"
url_login = "https://mydtu.duytan.edu.vn/Signin.aspx"

scroll_attempts = 0
max_scroll_attempts = 20


def solve_captcha(driver):
    captcha_imgs = driver.find_elements(By.TAG_NAME, "img")

    for img in captcha_imgs:
        alt = img.get_attribute("alt")
        if alt and "captcha" in alt.lower():
            img.screenshot("captcha.png")
            break

    result = reader.readtext("captcha.png", detail=0)  # Nhận diện ký tự
    captcha_text = "".join(result).replace(" ", "")  # Ghép các ký tự lại
    print("CAPTCHA nhận diện:", captcha_text)

    return captcha_text


def login_mydtu(username, password):
    driver = webdriver.Chrome()
    driver.get(url_login)
    time.sleep(2)

    txt_username = driver.find_element(By.ID, "txtUser")
    txt_username.send_keys(username)
    time.sleep(0.5)

    txt_password = driver.find_element(By.ID, "txtPass")
    txt_password.send_keys(password)
    time.sleep(0.5)

    captcha_code = solve_captcha(driver)
    driver.find_element(By.ID, "txtCaptcha").send_keys(captcha_code)
    time.sleep(0.5)

    btn_login = driver.find_element(By.ID, "btnLogin1")
    btn_login.click()
    time.sleep(3)


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


login_mydtu("ngongoctan", "Ngoctan4677.")
# find_and_click(img, scroll_attempts, max_scroll_attempts)
# find_and_type(input_img)
# K87865304888957





