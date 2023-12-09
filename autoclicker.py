# Set time between clicks (Secs) set to <= 0 for fastest 
KEY_INPUT_DELAY = 0.001
# Amount of clicks to preform before checking for exit keys (Use to speed up program if KEY_INPUT_DELAY is <= 0 (set EXIT_POLL_ITER higher))
EXIT_POLL_ITER = 50



# Import modules (Install if not installed)
try:
    import keyboard, pyautogui, time
except ImportError:
    import os
    print("Packages Missing! Installing ...")
    print("--------------------------------")
    os.system("pip install keyboard && pip install pyautogui")
    #Re-import and continue running
    import keyboard, pyautogui, time
cps = str(1 / KEY_INPUT_DELAY) if KEY_INPUT_DELAY > 0 else "N/A"
print(f"Set to {cps} CPS")
print("Press 1 & 3 (at the same time) to start, esc to cancel")
while True:
    if keyboard.is_pressed("esc"):
        exit(0)
    elif keyboard.is_pressed("1") and keyboard.is_pressed("3"):
        break
    time.sleep(0.1)


print("Starting ....")
pyautogui.PAUSE = 0
while True:
    if keyboard.is_pressed("esc"):
        break
    for i in range(EXIT_POLL_ITER):
        stT = time.time()
        pyautogui.leftClick()
        curT = time.time()
        if KEY_INPUT_DELAY > 0 and KEY_INPUT_DELAY - (curT - stT) >= 0:
            time.sleep(KEY_INPUT_DELAY - (curT - stT))
print("Finished!")
