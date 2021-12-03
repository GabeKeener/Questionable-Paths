#import pygame
import pygame
from pygame import mixer

#initialize game engine
pygame.init()

window_width=1200
window_height=800

animation_increment=10
clock_tick_rate=20


#Starting pygame music mixer
mixer.init()
mixer.music.set_volume(0.5)
pygame.mixer.music.load("A really dark alley.mp3")
mixer.music.play()

def main():
    #setting up pictures array
    i = 0
                                                                                                                                                                                                                                                                                            #slot 15
    pictures = ["intro 1.jpg", "intro 2.jpg", "Picture 1.jpg", "Picture 2.jpg", "Picture 3.jpg", "Picture 4.jpg", "Picture 5.jpg", "Picture 6.jpg", "Picture 7.jpg", "Picture 8.jpg", "Picture 9.jpg", "Picture 10.jpg", "Picture 11 (you win).jpg", "Picture 2.5.jpg", "Picture 2.6.jpg", "Death 1.jpg",
                "Picture 3.5.jpg", "Picture 4.5.jpg", "Picture 5.5.jpg", "Death 2.jpg", "Picture 6.5.jpg", "Death 3.jpg", "lose.jpg"]
    length = 2

    #Open a window
    size = (window_width, window_height)
    screen = pygame.display.set_mode(size)

    #Set title to the window
    pygame.display.set_caption("Questionable Paths")

    dead=False

    clock = pygame.time.Clock()

    #main Game Loop
    while(dead==False):
        background = pictures[i]
        background_image = pygame.image.load(background).convert()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dead = True
             
            #checking if keydown event happened or not
            if event.type == pygame.KEYDOWN:
                   
                #checking if key "A" was pressed
                if event.key == pygame.K_a:
                    if(i == 3):
                        i = i + 1
                    elif(i == 4):
                        i = i + 1
                    elif(i == 5):
                        i = i + 1
                    elif(i == 6):
                        i = i + 1
                    elif(i == 7):
                        i = 20

                        
                    #Standard
                    elif(i == 0):
                        i = i + 1
                    elif(i == 1):
                        i = i + 1
                    elif(i == 2):
                        i = i + 1
                    elif(i == 14):
                        i = i + 1
                    elif(i == 18):
                        i = i + 1
                    elif(i == 20):
                        i = i + 1
                    elif(i == 8):
                        i = i + 1
                    elif(i == 9):
                        i = i + 1
                    elif(i == 10):
                        i = i + 1
                    elif(i == 11):
                        i = i + 1

                        

                    #Survival tests
                    #Game 1
                    elif(i == 15):
                        answer = input("Type answer here: ")
                        if(answer == "16"):
                            i = 3
                            continue
                        else:
                            i = 22
                            
                    #Game 2
                    elif(i == 19):
                        answer = input("Type answer here: ")
                        if(answer == "23"):
                            i = 6
                            continue
                        else:
                            i = 22
                            
                    #Game 3
                    elif(i == 21):
                        answer = input("Type answer here: ")
                        if(answer == "43"):
                            i = 7
                            continue
                        else:
                            i = 22

                    else:
                        print("error")


                   
                #checking if key "D" was pressed
                if event.key == pygame.K_d:
                    if(i == 3):
                        i = 13
                    elif(i == 4):
                        i = 16
                    elif(i == 5):
                        i = 17
                    elif(i == 6):
                        i = 18
                    elif(i == 7):
                        i = i + 1
                    elif(i == 13):
                        i = i + 1

                        
                    #Standard
                    elif(i == 0):
                        i = i + 1                       
                    elif(i == 1):
                        i = i + 1                     
                    elif(i == 2):
                        i = i + 1
                    elif(i == 14):
                        i = i + 1                       
                    elif(i == 18):
                        i = i + 1
                    elif(i == 20):
                        i = i + 1
                    elif(i == 8):
                        i = i + 1
                    elif(i == 9):
                        i = i + 1
                    elif(i == 10):
                        i = i + 1
                    elif(i == 11):
                        i = i + 1


                    #Survival tests
                    #Game 1
                    elif(i == 15):
                        answer = input("Type answer here: ")
                        if(answer == "16"):
                            i = 3
                            continue
                        else:
                            i = 22
                            
                    #Game 2
                    elif(i == 19):
                        answer = input("Type answer here: ")
                        if(answer == "23"):
                            i = 6
                            continue
                        else:
                            i = 22
                            
                    #Game 3
                    elif(i == 21):
                        answer = input("Type answer here: ")
                        if(answer == "43"):
                            i = 7
                            continue
                        else:
                            i = 22

                    else:
                        print("error")


                        
                #checking if key "B" was pressed
                if event.key == pygame.K_b:
                    if(i == 13):
                        i = 3
                    if(i == 16):
                        i = 4
                    if(i == 17):
                        i = 5



        screen.blit(background_image, [0, 0])

        pygame.display.flip()
        clock.tick(clock_tick_rate)



if __name__ == '__main__':

    main()






    
