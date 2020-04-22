import pyautogui, time, logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

# identify the top-left corner
logging.debug('Barra de pesca...')
region = pyautogui.locateOnScreen('C:\\Users\\We\\Pictures\\bait.png',confidence= 0.9)
if region is None:
    raise Exception('Local inadequado')

# calculate the region of the entire game
topRightX = region[0] + region[2]  # left + width
topRightY = region[1]  # top
GAME_REGION = (topRightX - 200, topRightY, 200, 90)
logging.debug('Game : %s' % (GAME_REGION,))
logging.info('Waiting for Bite...')

while True:

    up = pyautogui.locateCenterOnScreen('C:\\Users\\We\\Pictures\\up.png',confidence= 0.9)
    if up is None:
        logging.debug('1')
    if up is not None:
        logging.debug('Pulling out!')
        pyautogui.moveTo(up)
        time.sleep(3)

    reel = pyautogui.locateCenterOnScreen('C:\\Users\\We\\Pictures\\reel.png', confidence= 0.9)
    if reel is None:
        logging.debug('2')
    if reel is not None:
        logging.debug('Reeling')
        pyautogui.moveTo(reel)
        time.sleep(3)
        pyautogui.click(0,560)


    right = pyautogui.locateCenterOnScreen('C:\\Users\\We\\Pictures\\right.png', confidence= 0.9)
    if right is None:
        logging.debug('3')
    if right is not None:
        logging.debug('Direita')
        pyautogui.moveTo(right)
        time.sleep(3)

    left = pyautogui.locateCenterOnScreen('C:\\Users\\We\\Pictures\\left.png', confidence= 0.94)
    if left is None:
        logging.debug('4')
    if left is not None:
        logging.debug('Esquerda')
        pyautogui.moveTo(left)
        time.sleep(3)

    fish = pyautogui.locateCenterOnScreen('C:\\Users\\We\\Pictures\\fish.png', confidence= 0.94)
    if fish is None:
        logging.debug('5')
    if fish is not None:
        logging.debug('Soltando')
        pyautogui.moveTo(fish)
        time.sleep(3)
