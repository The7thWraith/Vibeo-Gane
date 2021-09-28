# Wormy (a Nibbles clone)
# By Al Sweigart al@inventwithpython.com
# http://inventwithpython.com/pygame
# Released under a "Simplified BSD" license
#
# Skidded and Modified by Wraith
# Ok guys I actually modified this a shit ton its not fully skidded please don't hu-


import random, pygame, sys, time
from pygame.locals import *

FPS = 15

WINDOWWIDTH = 640
WINDOWHEIGHT = 480
CELLSIZE = 20


assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
BLUE      = (  0,   0, 255)

BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

HEAD = 0

SCORES = []
Color1 = GREEN
Color2 = GREEN

def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('Wormy')

    showStartScreen()

    while True:
        lives = runGame(5)
        if lives == 0:
            showGameOverScreen()



def runGame(lives):

    global FPS, Color1, Color2
    levelUp = False
    level = 1
    lives = 5
    score = 0
    Color1 = DARKGREEN
    Color2 = GREEN


    # Set a random start point.
    startx = random.randint(5, CELLWIDTH - 6)
    starty = random.randint(5, CELLHEIGHT - 6)
    wormCoords = [{'x': startx,     'y': starty},
                  {'x': startx - 1, 'y': starty},
                  {'x': startx - 2, 'y': starty}]
    direction = RIGHT


    # Start the apple in a random place.
    apple = getRandomLocation()

    specialApple = getRandomLocation()

    badApple = getRandomLocation()
    badApple2 = getRandomLocation()
    badApple3 = getRandomLocation()
    badApple4 = getRandomLocation()
    badApple5 = getRandomLocation()
    badApple6 = getRandomLocation()
    teleportApple = getRandomLocation()
    start = time.time()

    while True: # main game loop
        if lives == 0:
            showGameOverScreen()

        timer = time.time()

        if (timer - start > 5 and timer - start < 5.05):
            lives -=1

        for event in pygame.event.get(): # event handling loop
            if event.type == QUIT:
                terminate()
            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and direction != RIGHT:
                    direction = LEFT
                elif (event.key == K_RIGHT or event.key == K_d) and direction != LEFT:
                    direction = RIGHT
                elif (event.key == K_UP or event.key == K_w) and direction != DOWN:
                    direction = UP
                elif (event.key == K_DOWN or event.key == K_s) and direction != UP:
                    direction = DOWN
                elif event.key == K_ESCAPE:
                    terminate()

        # check if the worm has hit edge
        if wormCoords[HEAD]['x'] == -1 or wormCoords[HEAD]['x'] == CELLWIDTH or wormCoords[HEAD]['y'] == -1 or wormCoords[HEAD]['y'] == CELLHEIGHT:
            lives -= 1
            # Set a random start point.
            startx = random.randint(5, CELLWIDTH - 6)
            starty = random.randint(5, CELLHEIGHT - 6)
            wormCoords = [{'x': startx,     'y': starty},
                          {'x': startx - 1, 'y': starty},
                          {'x': startx - 2, 'y': starty}]
            direction = RIGHT

        # check if the worm has hit itself
        for wormBody in wormCoords[1:]:
            if wormBody['x'] == wormCoords[HEAD]['x'] and wormBody['y'] == wormCoords[HEAD]['y']:
                lives -=1

                # Set a random start point.
                startx = random.randint(5, CELLWIDTH - 6)
                starty = random.randint(5, CELLHEIGHT - 6)
                wormCoords = [{'x': startx,     'y': starty},
                          {'x': startx - 1, 'y': starty},
                          {'x': startx - 2, 'y': starty}]
                direction = RIGHT
                if lives == 0:
                    return # game over

        # check if worm has eaten an apple
        if wormCoords[HEAD]['x'] == apple['x'] and wormCoords[HEAD]['y'] == apple['y']:
            # don't remove worm's tail segment
            apple = getRandomLocation() # set a new apple somewhere
            levelUp = False
            level = 1
            badApple = getRandomLocation()
            badApple2 = getRandomLocation()
            badApple3 = getRandomLocation()
            badApple4 = getRandomLocation()
            badApple5 = getRandomLocation()
            badApple6 = getRandomLocation()
            score += 1
        else:
            del wormCoords[-1] # remove worm's tail segment

        if wormCoords[HEAD]['x'] == badApple['x'] and wormCoords[HEAD]['y'] == badApple['y']:
            terminate()

        if wormCoords[HEAD]['x'] == badApple2['x'] and wormCoords[HEAD]['y'] == badApple2['y']:
            terminate()

        if wormCoords[HEAD]['x'] == badApple3['x'] and wormCoords[HEAD]['y'] == badApple3['y']:
            terminate()

        if wormCoords[HEAD]['x'] == badApple4['x'] and wormCoords[HEAD]['y'] == badApple4['y']:
            terminate()

        if wormCoords[HEAD]['x'] == badApple5['x'] and wormCoords[HEAD]['y'] == badApple5['y']:
            terminate()
        if wormCoords[HEAD]['x'] == badApple6['x'] and wormCoords[HEAD]['y'] == badApple6['y']:
            terminate()

        # check if worm has eaten a teleport apple
        if wormCoords[HEAD]['x'] == teleportApple['x'] and wormCoords[HEAD]['y'] == teleportApple['y']:

            colorcheck = random.randint(1, 5)
            if colorcheck == 1:
                Color1 = GREEN
            elif colorcheck == 2:
                Color1 = RED
            elif colorcheck == 3:
                Color1 = BLACK
            else:
                Color1 = BLUE

            randomDirection = random.randint(1, 4)
            if randomDirection == 1:
                direction = RIGHT
            elif randomDirection == 2:
                direction = LEFT
            elif randomDirection == 3:
                direction = UP
            else:
                direction = DOWN

            wormCoords[HEAD]['x'] = random.randint(0, CELLWIDTH - 1)
            wormCoords[HEAD]['y'] = random.randint(0, CELLWIDTH - 1)

            for wormBody in range(1, len(wormCoords)):
                wormCoords[wormBody]['x'] = wormCoords[wormBody]['x']




            teleportApple = getRandomLocation()

        # check if worm has eaten a special Apple
        if wormCoords[HEAD]['x'] == specialApple['x'] and wormCoords[HEAD]['y'] == specialApple['y']:
            lives +=1

            FPS +=10

            if (timer - start % 10) == 0:
                FPS -=10

            specialApple = {"x": 1000, "y": 1000}


        # move the worm by adding a segment in the direction it is moving
        if direction == UP:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] - 1}
        elif direction == DOWN:
            newHead = {'x': wormCoords[HEAD]['x'], 'y': wormCoords[HEAD]['y'] + 1}
        elif direction == LEFT:
            newHead = {'x': wormCoords[HEAD]['x'] - 1, 'y': wormCoords[HEAD]['y']}
        elif direction == RIGHT:
            newHead = {'x': wormCoords[HEAD]['x'] + 1, 'y': wormCoords[HEAD]['y']}
        wormCoords.insert(0, newHead)

        DISPLAYSURF.fill(BGCOLOR)
        drawGrid()
        drawWorm(wormCoords)
        drawApple(apple)
        drawSpecialApple(specialApple)
        drawScore(score)
        drawLives(lives)
        drawbadApple(badApple)
        drawTimer(round(timer-start,2))
        drawbadApple2(badApple2)
        drawbadApple3(badApple3)
        drawbadApple4(badApple4)
        drawbadApple5(badApple5)
        drawbadApple6(badApple6)
        drawteleportApple(teleportApple)
        # Increase FPS every 3 points
        if(len(wormCoords)-3 % 3 == 0 and levelUp == False):
            FPS +=3
            levelUp = True
            level +=1
            specialApple = getRandomLocation()

        drawLevel(level)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

def drawPressKeyMsg():
    pressKeySurf = BASICFONT.render('Press a key to play.', True, DARKGRAY)
    pressKeyRect = pressKeySurf.get_rect()
    pressKeyRect.topleft = (WINDOWWIDTH - 200, WINDOWHEIGHT - 30)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)


def checkForKeyPress():
    if len(pygame.event.get(QUIT)) > 0:
        terminate()

    keyUpEvents = pygame.event.get(KEYUP)
    if len(keyUpEvents) == 0:
        return None
    if keyUpEvents[0].key == K_ESCAPE:
        terminate()
    return keyUpEvents[0].key


def showStartScreen():
    titleFont = pygame.font.Font('freesansbold.ttf', 100)
    titleSurf1 = titleFont.render('Wormy!', True, WHITE, DARKGREEN)
    titleSurf2 = titleFont.render('Wormy!', True, GREEN)

    degrees1 = 0
    degrees2 = 0
    while True:
        DISPLAYSURF.fill(BGCOLOR)
        rotatedSurf1 = pygame.transform.rotate(titleSurf1, degrees1)
        rotatedRect1 = rotatedSurf1.get_rect()
        rotatedRect1.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf1, rotatedRect1)

        rotatedSurf2 = pygame.transform.rotate(titleSurf2, degrees2)
        rotatedRect2 = rotatedSurf2.get_rect()
        rotatedRect2.center = (WINDOWWIDTH / 2, WINDOWHEIGHT / 2)
        DISPLAYSURF.blit(rotatedSurf2, rotatedRect2)

        drawPressKeyMsg()

        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return
        pygame.display.update()
        FPSCLOCK.tick(FPS)
        degrees1 += 3 # rotate by 3 degrees each frame
        degrees2 += 7 # rotate by 7 degrees each frame


def terminate():
    pygame.quit()
    sys.exit()


def getRandomLocation():
    return {'x': random.randint(0, CELLWIDTH - 1), 'y': random.randint(0, CELLHEIGHT - 1)}


def showGameOverScreen():
    gameOverFont = pygame.font.Font('freesansbold.ttf', 150)
    scoreFont = pygame.font.Font('freesansbold.ttf', 50)

    gameSurf = gameOverFont.render('Game', True, WHITE)
    overSurf = gameOverFont.render('Over', True, WHITE)
    scoreSurf = score.render('Score: %s' % (SCORES[len(SCORES)-1]), True, WHITE)

    gameRect = gameSurf.get_rect()
    overRect = overSurf.get_rect()
    scoreRect = scoreSurf.get_rect()

    gameRect.midtop = (WINDOWWIDTH / 2, 10)
    overRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 25)
    scoreRect.midtop = (WINDOWWIDTH / 2, gameRect.height + 10 + 100)

    DISPLAYSURF.blit(scoreSurf, scoreRect)
    DISPLAYSURF.blit(gameSurf, gameRect)
    DISPLAYSURF.blit(overSurf, overRect)

    drawPressKeyMsg()
    pygame.display.update()
    pygame.time.wait(500)
    checkForKeyPress() # clear out any key presses in the event queue

    while True:
        if checkForKeyPress():
            pygame.event.get() # clear event queue
            return

def drawScore(score):
    scoreSurf = BASICFONT.render('Score: %s' % (score), True, WHITE)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 100, 10)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

def drawTimer(time):
    timeSurf = BASICFONT.render('time: %s' % (time), True, WHITE)
    timeRect = timeSurf.get_rect()
    timeRect.topleft = (WINDOWWIDTH - 400, 10)
    DISPLAYSURF.blit(timeSurf, timeRect)

def drawLives(lives):
    livesSurf = BASICFONT.render('lives: %s' % (lives), True, WHITE)
    livesRect = livesSurf.get_rect()
    livesRect.topleft = (WINDOWWIDTH - 300, 10)
    DISPLAYSURF.blit(livesSurf, livesRect)

def drawLevel(level):
    levelSurf = BASICFONT.render('level: %s' % (level), True, WHITE)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (WINDOWWIDTH - 200, 10)
    DISPLAYSURF.blit(levelSurf, levelRect)


def drawWorm(wormCoords):
    for coord in wormCoords:
        x = coord['x'] * CELLSIZE
        y = coord['y'] * CELLSIZE
        wormSegmentRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(DISPLAYSURF, Color1, wormSegmentRect)
        wormInnerSegmentRect = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(DISPLAYSURF,Color2, wormInnerSegmentRect)


def drawApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, RED, appleRect)

def drawteleportApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    teleportAppleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, BLUE, teleportAppleRect)

def drawbadApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    badAppleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, DARKGREEN , badAppleRect)

def drawbadApple2(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    badApple2Rect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, DARKGREEN , badApple2Rect)

def drawbadApple3(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    badApple3Rect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, DARKGREEN , badApple3Rect)

def drawbadApple4(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    badApple4Rect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, DARKGREEN , badApple4Rect)

def drawbadApple5(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    badApple5Rect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, DARKGREEN , badApple5Rect)

def drawbadApple6(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    badApple6Rect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, DARKGREEN , badApple6Rect)


def drawSpecialApple(coord):
    x = coord['x'] * CELLSIZE
    y = coord['y'] * CELLSIZE
    appleRect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    pygame.draw.rect(DISPLAYSURF, GREEN, appleRect)


def drawGrid():
    for x in range(0, WINDOWWIDTH, CELLSIZE): # draw vertical lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (x, 0), (x, WINDOWHEIGHT))
    for y in range(0, WINDOWHEIGHT, CELLSIZE): # draw horizontal lines
        pygame.draw.line(DISPLAYSURF, DARKGRAY, (0, y), (WINDOWWIDTH, y))


if __name__ == '__main__':
    main()
