# Done by Frannecklp

import cv2
import numpy as np
from grabscreen import grab_screen

def main():
    last_time = time.time()
    for i in list(range(4))[::-1]:
        print(i+1)
        time.sleep(1)

    paused = False

    while(True):
        
        if not paused:
            screen = grab_screen(region=(0,40,GAME_WIDTH,GAME_HEIGHT+40))

        # p pauses game and can get annoying.
        if 'T' in keys:
            if paused:
                paused = False
                time.sleep(1)
            else:
                paused = True
                #ReleaseKey(A)
                #ReleaseKey(W)
                #ReleaseKey(D)
                time.sleep(1)

main()

