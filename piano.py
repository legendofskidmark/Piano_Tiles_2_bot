import numpy as np
from PIL import ImageGrab
import cv2
import time
import pyautogui

start = time.time()

game_Area = [653,620,1240,621] # Region of analysisfor black pixels

line_1 = [740,660]  # 1st lane
line_2 = [890,660]  # 2nd lane
line_3 = [1040,660] # 3rd lane
line_4 = [1200,660] # 4th lane

pyautogui.PAUSE = 0.001

flag = True

def click_on_tile(screen):

    global flag
    elapse = time.time() - start # Time elasped till now,used to speed up the mouse movement

    if elapse > 59.0 and elapse < 61.0 and flag:
        pyautogui.PAUSE /= 10
        flag = not flag

    elif elapse > 100.0 and elapse < 102.0 and flag == False:
        flag = True
        pyautogui.PAUSE /= 10

    elif elapse > 150.0 and elapse < 152.0 and flag:
        flag =  False
        line_1[1] += 3
        line_2[1] += 3
        line_3[1] += 3
        line_4[1] += 3
        pyautogui.PAUSE /= 10

##    elif elapse > 200.0 and not flag:
##        flag =  True
##        line_1[1] += 10
##        line_2[1] += 10
##        line_3[1] += 10
##        line_4[1] += 10
##        pyautogui.PAUSE /= 10
##    
##    print(elapse)

    # 74, 221, etc., are pixels of "piano" window
    if screen[0][74][0] <= 30:  # screen[0][x] is array of three values (RGB colors) 
        pyautogui.click(line_1) # <= 30 for blackish pixels
    elif screen[0][221][0] <= 30:
        pyautogui.click(line_2)
    elif screen[0][368][0] <= 30:
        pyautogui.click(line_3)
    elif screen[0][515][0] <= 30:
        pyautogui.click(line_4)

while True:
    screen = np.array(ImageGrab.grab(bbox= game_Area))
    cv2.imshow('piano',screen)
    click_on_tile(screen)
    
    

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break

