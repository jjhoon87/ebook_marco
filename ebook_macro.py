import pyautogui as auto
import time
import pyperclip

total_page = 100
book_name = 'ebook'
capture_pos = (1269, 536)
ebook_screen_center_pos = (2144, 1041)
sleep_time = 1.0

time.sleep(5.)

for i in range(int(total_page/2)):
    file_name = book_name + '_' + str(i+1).zfill(4) + '.png'
    pyperclip.copy(file_name)

    auto.click(capture_pos)
    time.sleep(sleep_time)

    auto.hotkey('ctrl', 'v')
    time.sleep(sleep_time)

    auto.press('enter')
    time.sleep(sleep_time)

    auto.click(ebook_screen_center_pos)
    time.sleep(sleep_time)

    auto.press('right')
    time.sleep(sleep_time)

    print(str(i+1), '/', int(total_page/2))
