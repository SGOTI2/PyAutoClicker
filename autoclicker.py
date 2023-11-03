# Set time between clicks (Secs) set to <= 0 for fastest 
KEY_INPUT_DELAY = 0.1
# Amount of clicks to preform before checking for exit keys (Use to speed up program if KEY_INPUT_DELAY is <= 0 (set EXIT_POLL_ITER higher))
EXIT_POLL_ITER = 1
# Number of seconds before program starts
START_WAIT = 3



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
print(f"auto clicker starts in {START_WAIT} secs, hold esc to stop")
cps = str(1 / KEY_INPUT_DELAY) if KEY_INPUT_DELAY > 0 else "N/A"
print(f"Set to {cps} CPS")
time.sleep(START_WAIT)
if keyboard.is_pressed("esc"):
    exit(0)


print("Starting ....")
pyautogui.PAUSE = 0
while True:
    if keyboard.is_pressed("esc"):
        break
    for i in range(EXIT_POLL_ITER):
        stT = time.time()
        pyautogui.leftClick()
        curT = time.time()
        if KEY_INPUT_DELAY > 0 and curT - stT > 0:
            time.sleep(KEY_INPUT_DELAY - (curT - stT))
print("Finished!")