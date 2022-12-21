import time
import pyautogui


def timer_countdown(seconds):
    while seconds:
        mins, sec = divmod(seconds, 60)
        print(f'{mins:02d}:{sec:02d}')
        time.sleep(1)
        seconds -= 1
    print('Time finished!')


seconds = pyautogui.prompt(text="Please enter the seconds for the timer:", title = 'Seconds timer', default='')
timer_countdown(int(seconds))
