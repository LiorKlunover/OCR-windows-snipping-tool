import time
import keyboard
import mouse
from PIL import ImageGrab, Image
import pytesseract
import pyperclip
import sys


def snip_and_ocr():

    time.sleep(0.8)
    # Trigger the snipping tool
    keyboard.press_and_release('windows+shift+s')  # Using keyboard library to handle the snipping tool activation

    # Wait for a short period to allow the snipping tool to open
    time.sleep(1)

    # Wait for the user to finish snipping

    mouse.wait(button='left', target_types=('up',))

    # Wait a short moment for the clipboard to update
    time.sleep(0.5)

    # Try to grab the image from clipboard
    img = ImageGrab.grabclipboard()

    # Check if we got an image
    if isinstance(img, Image.Image):

        # Perform OCR on the image
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(img, lang='eng+heb', config=custom_config)

        # Copy the extracted text to the clipboard
        pyperclip.copy(text)

    else:
        print("No image found in clipboard. Please try again.")


def on_trigger_hotkey():
    print("Hotkey triggered")  # Debug message
    snip_and_ocr()


def on_exit_hotkey():
    #unhook all the hotkeys and exit the program
    keyboard.unhook_all()
    sys.exit()


def main():
    # Register the hotkeys

    keyboard.add_hotkey('windows+shift+w', on_trigger_hotkey, suppress=False)
    keyboard.add_hotkey('ctrl+alt+q', on_exit_hotkey, suppress=False)

    keyboard.wait()

if __name__ == "__main__":
    main()
