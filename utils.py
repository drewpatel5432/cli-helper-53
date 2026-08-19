import time
import pyautogui

def click_mouse(x, y, button='left', clicks=1, interval=0):
    pyautogui.click(x=x, y=y, button=button, clicks=clicks, interval=interval)

def double_click(x, y, interval=0):
    click_mouse(x, y, clicks=2, interval=interval)

def hold_mouse(x, y, duration):
    pyautogui.moveTo(x, y)
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()

def move_mouse_smoothly(start_x, start_y, end_x, end_y, steps=10):
    x_step = (end_x - start_x) / steps
    y_step = (end_y - start_y) / steps
    for i in range(steps):
        pyautogui.moveTo(start_x + x_step * i, start_y + y_step * i)
        time.sleep(0.01)

def wait_for_image(image_path, timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        location = pyautogui.locateOnScreen(image_path)
        if location:
            return location
        time.sleep(0.5)
    return None

