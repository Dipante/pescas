import pyautogui, time, os, logging, sys, random, copy

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s.%(msecs)03d: %(message)s', datefmt='%H:%M:%S')

def imPath(filename):
    """A shortcut for joining the 'images/'' file path, since it is used so often. Returns the filename with 'images/' prepended."""
    return os.path.join('images', filename)

def getGameRegion():
    """Obtains the region that the Sushi Go Round game is on the screen and assigns it to GAME_REGION. The game must be at the start screen (where the PLAY button is visible)."""
    global GAME_REGION

    # identify the top-left corner
    logging.debug('Barra de pesca...')
    region = pyautogui.locateOnScreen('C:\\Users\\We\\Pictures\\bait.png')
    if region is None:
        raise Exception('Could not find game on screen. Is the game visible?')

    # calculate the region of the entire game
    topRightX = region[0] + region[2] # left + width
    topRightY = region[1] # top
    GAME_REGION = (topRightX - 640, topRightY, 640, 480) # the game screen is always 640 x 480
    logging.debug('Game region found: %s' % (GAME_REGION,))


def getOrders():
    """Scans the screen for orders being made. Returns a dictionary with a (left, top, width, height) tuple of integers for keys and the order constant for a value.

    The order constants are ONIGIRI, GUNKAN_MAKI, CALIFORNIA_ROLL, SALMON_ROLL, SHRIMP_SUSHI, UNAGI_ROLL, DRAGON_ROLL, COMBO."""
    orders = {}
    for orderType in (ALL_ORDER_TYPES):
        allOrders = pyautogui.locateAllOnScreen(imPath('%s_order.png' % orderType), region=(GAME_REGION[0] + 32, GAME_REGION[1] + 46, 558, 44))
        for order in allOrders:
            orders[order] = orderType
    return orders


def getGud():

    logging.info('Finding suitable spot...')
    while True:
        region = pyautogui.locateOnScreen('C:\\Users\\We\\Pictures\\Untitled5.png', confidence=0.9)
        if region is not None:
            break

    pyautogui.click(region, duration=1.25)
    # click on Play
    logging.info('Waiting for Bite...')
    while True: # loop because it could be the blue or pink Play button displayed at the moment.
        pos = pyautogui.locateCenterOnScreen('C:\\Users\\We\\Pictures\\Untitled3.png', confidence=0.9)
        if pos is not None:
            break
    pyautogui.click(pos, duration=0.25)
    pyautogui.click(pos, duration=0.85)
    logging.info('Clicked on Event button.')

def replayTudo():
    i = 0
    while True:
        getGud()
        i = i + 1
        print('Ja foram', i,'peixes')
        time.sleep(4) #se tiver upando 4, if not 2

replayTudo()

