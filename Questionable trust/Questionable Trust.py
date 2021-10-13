import pygame
import os
import time
import random
from pygame import mixer
pygame.font.init()

#Starting pygame music mixer
mixer.init()
mixer.music.set_volume(0.5)
pygame.mixer.music.load("Torture - Coyote Hearing.wav")

#Setting up game window
WIDTH, HEIGHT = 1000, 750
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Questionable Trust")

#Game Assets
ghost = pygame.image.load(os.path.join("assets", "ghost.png"))

#Background
bg = pygame.transform.scale(pygame.image.load(os.path.join("assets", "foggy.jpg")), (WIDTH, HEIGHT))

#main loop
def main():

    #Setting music to loop until game is over
    pygame.mixer.music.play(-1)

    #Setting up FPS/level/lives/font of game
    run = True
    FPS = 60
    lives = 2
    left = 0
    right = 0
    lost = False
    font = pygame.font.SysFont("times new roman", 50)
    lostFont = pygame.font.SysFont("times new roman", 80)
    clock = pygame.time.Clock()



    def redrawWindow():
        WINDOW.blit(bg, (0, 0))

        #making lives/level text
        leftText = font.render(f"Left: {left}", 1, (44, 228, 225))
        rightText = font.render(f"Right: {right}", 1, (44, 228, 225))

        WINDOW.blit(leftText, (10, 10))
        WINDOW.blit(rightText, (WIDTH - rightText.get_width() - 10, 10))

        if lost:
            lostLabel = lostFont.render("You Lose", 1, (241, 10, 10))
            WINDOW.blit(lostLabel, (WIDTH/2 - lostLabel.get_width()/2, 350))
        
        pygame.display.update()
    


    #Setting up QUIT event
    while run:
        clock.tick(FPS)
        redrawWindow()

        if lives <= 0:
            lost = True
            lostCounter += 1



    #setting up key actions
        pressedkeys = pygame.key.get_pressed()

        #moving player left
        if pressedkeys[pygame.K_a]and needle.x + velocity > 0:
            needle.x -= velocity

        #moving player right
        if pressedkeys[pygame.K_d]and needle.x + velocity + needle.getWidth() < WIDTH:
            needle.x += velocity

            

#main menu screen
def mainMenu():
    titleFont = pygame.font.SysFont("times new roman", 41)
    run = True
    while run:
        WINDOW.blit(bg, (0, 0))
        title = titleFont.render("Press the mouse button when you are ready", 1, (255, 255, 255))
        WINDOW.blit(title, (WIDTH / 2 - title.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()
    

mainMenu()
