import random
import pygame
import os
from sys import exit

# pygame setup
pygame.init()

screen = pygame.display.set_mode((1000,800))
pygame.display.set_caption("RGB guessing")
clock = pygame.time.Clock()

# text
input_rectR = pygame.Rect(200, 200, 140, 32)
input_rectG = pygame.Rect(400, 200, 140, 32)
input_rectB = pygame.Rect(600, 200, 140, 32)
resultRect = pygame.Rect(0,500, 140, 32)

base_font = pygame.font.Font(os.path.join('ColorRGBguessing', 'Pixeltype.ttf'), 32)
user_textR = ''
user_textG = ''
user_textB = ''



# colors and logic
c_R = random.randint(0,255)
c_G = random.randint(0,255)
c_B = random.randint(0,255)

guessed_red = False
guessed_green = False
guessed_blue = False

activeR = False
activeG = False
activeB = False

textR = 'Red was incorect'
textG = 'Green was incorect'
textB = 'Blue was incorect'
textResult = ''

color = (c_R, c_G, c_B)

# visualizing in pygame
run = True
while run:
    clock.tick(60)

    # events
    for event in pygame.event.get():
        # quiting
        if event.type == pygame.QUIT:
            run = False
            pygame.quit
            exit()
        # checking on which box we clicked and can type on
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rectR.collidepoint(event.pos):
                activeR = True
            else:
                activeR = False
            if input_rectG.collidepoint(event.pos):
                activeG = True
            else:
                activeG = False
            if input_rectB.collidepoint(event.pos):
                activeB = True
            else:
                activeB = False
        # typing into the boxes
        if activeR:
            if event.type == pygame.KEYDOWN:
    
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
    
                    # get text input from 0 to -1 i.e. end.
                    user_textR = user_textR[:-1]
    
                # Unicode standard is used for string
                # formation
                else:
                    user_textR += event.unicode
        if activeG:
            if event.type == pygame.KEYDOWN:
    
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
    
                    # get text input from 0 to -1 i.e. end.
                    user_textG = user_textG[:-1]
    
                # Unicode standard is used for string
                # formation
                else:
                    user_textG += event.unicode
        if activeB:
            if event.type == pygame.KEYDOWN:
    
                # Check for backspace
                if event.key == pygame.K_BACKSPACE:
    
                    # get text input from 0 to -1 i.e. end.
                    user_textB = user_textB[:-1]
    
                # Unicode standard is used for string
                # formation
                else:
                    user_textB += event.unicode

    # drawing black boxes in which we type
    pygame.draw.rect(screen, (0,0,0), input_rectR)
    pygame.draw.rect(screen, (0,0,0), input_rectG)
    pygame.draw.rect(screen, (0,0,0), input_rectB)
    pygame.draw.rect(screen, (0,0,0), resultRect)

    # making the text for drawing
    text_surfaceR = base_font.render(user_textR, True, (255, 255, 255))
    text_surfaceG = base_font.render(user_textG, True, (255, 255, 255))
    text_surfaceB = base_font.render(user_textB, True, (255, 255, 255))

    #drawing text
    screen.blit(text_surfaceR, (input_rectR.x+5, input_rectR.y+5))
    screen.blit(text_surfaceG, (input_rectG.x+5, input_rectG.y+5))
    screen.blit(text_surfaceB, (input_rectB.x+5, input_rectB.y+5))

    # making boxes wider when long string of caracters is typed in
    input_rectR.w = max(100, text_surfaceR.get_width()+10)
    input_rectG.w = max(100, text_surfaceG.get_width()+10)
    input_rectB.w = max(100, text_surfaceB.get_width()+10)
    

    # checking if user estimated correctly
    for i in range(26):
        if not user_textR == '' and not user_textG == '' and not user_textB == '':
            if int(user_textR) + i == c_R:
                guessed_red = True
                textR = 'Red was corect'
            elif int(user_textR) - i == c_R:
                guessed_red = True
                textR = 'Red was corect'
            if int(user_textG) + i == c_G:
                guessed_green = True
                textG = 'Green was corect'
            elif int(user_textG) - i == c_G:
                guessed_green = True
                textG = 'Green was corect'
            if int(user_textB) + i == c_B:
                guessed_blue = True
                textB = 'Blue was corect'
            elif int(user_textB) - i == c_B:
                guessed_blue = True 
                textB = 'Blue was corect' 
            textResult = textR + ', red was: ' + str(c_R) + '. ' + textG + ', green was: ' + str(c_G) + '. ' + textB + ', blue was: ' + str(c_B) + '.'
            result_text = base_font.render(textResult, True, (255, 255, 255))
            resultRect.w = max(100, result_text.get_width()+10)
            screen.blit(result_text, (resultRect.x+5, resultRect.y+5))
            
            
    
    pygame.display.update()
    screen.fill(color)