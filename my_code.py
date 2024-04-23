import pyautogui
import time

def move_mouse_away():
    # Move the mouse pointer to a position away from the button
    pyautogui.moveTo(100, 100)  # Move to position (100, 100) on the screen

def find_and_click_start_crawling():
    # Define the image file path to search for
    image_path = 'screenshot.png'

    # Search for the image on the screen
    try:
        position = pyautogui.locateCenterOnScreen(image_path)
        if position is not None:
            # If image found, click on it
            pyautogui.click(position)
            print("Clicked on 'Start crawling' button")
            # Move the mouse pointer away from the button
            move_mouse_away()
    except Exception as e:
        print(f"Error: {e}")

# Continuous loop to check for the button and click it if found
while True:
    find_and_click_start_crawling()
    time.sleep(0.01) 