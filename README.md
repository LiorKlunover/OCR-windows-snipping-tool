# OCR Tool (Image to Text) for Windows
A lightweight and fast OCR tool for Windows that seamlessly integrates with the Snipping Tool. Easily capture screen snippets and instantly convert them to text with high accuracy. Perfect for quick and efficient text extraction from images without the need for heavy software.

Features:
Fast Integration: Utilize Windows key + Shift + W for quick screen capture and OCR processing.
Easy to Use: Press Ctrl + Alt + Q to stop the tool at any time.
Installation Steps:
1. Download the Script:

  Download the OCR.py file and save it anywhere on your computer.
  Install Required Python Packages:

2. Ensure all necessary Python packages are installed. You may need to run these commands with administrator privileges.
  bash
  Copy code
  pip install keyboard
  pip install mouse
  pip install pillow
  pip install pytesseract
  pip install pyperclip

3. Create a Batch File:

Open Notepad and insert the following lines (adjust the paths as needed):
batch
Copy code
@echo off
start "" /B "C:\Users\user123\AppData\Local\Programs\Python\Python312\pythonw.exe" "C:\Users\user123\OCR.py"
Save the file as OCR.bat and select "All Files" in the save dialog.

4. Set Up Automatic Startup:

  Save the OCR.bat file in the Startup folder so the tool runs automatically when your computer restarts:
  Press Windows key + R.
  Type shell:startup and press Enter.
  Save the OCR.bat file in the directory that opens.
  Now, the tool will start automatically when you reboot your computer.
