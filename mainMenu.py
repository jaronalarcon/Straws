import pygame
import buttons 

pygame.init()

#create game window
screen_width = 1200
screen_height = 800

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

#fonts
font = pygame.font.SysFont("Baloo 2", 80)

#define colors
text_color = (46, 121, 43)

#load images
start_img = pygame.image.load("StartButton.png").convert_alpha()
end_img = pygame.image.load("EndButton.png").convert_alpha()

#create button instances
start_button = buttons.Button(160, 205, start_img)
end_button =  buttons.Button(205, 320, end_img)


def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x,y))
    
#game loop
run = True
while run:
    screen.fill((233, 233, 233))
    #start_button.draw()
    draw_text("Straws", font, text_color, 500, 100)
        
    
    
#event handler
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 :
                if start_button.rect.collidepoint(event.pos) :
                    start_button.clicked = True
                    print("clicked")
                    action = True
                
                elif end_button.rect.collidepoint(event.pos) :
                    end_button.clicked = True
                    print("end game")
                    pygame.quit()
    
    if start_button.draw():
        print("Start the game?")
        
    if end_button.draw():
        run = False
        
    
    pygame.display.update()

pygame.quit()
    


    
