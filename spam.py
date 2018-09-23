import pyautogui

pyautogui.moveTo(722,776)
a=0

try:
	pyautogui.click(button='left')
	

	while a<50:
		pyautogui.typewrite('<Enter text>')
		pyautogui.press('enter')
		a=a+1

except WindowsError:
	while a<50:
		pyautogui.typewrite('<Enter text>')
		pyautogui.press('enter')
		a=a+1