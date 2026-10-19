import pygame
#some info from AI 
#starting from here, got these info from a pygame beginner tutorial from youtube
#Initialize Pygame
pygame.init()

#set up the display window
screen_width = 1200
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Buttons")

#create a clock object to manage frame rate
clock = pygame.time.Clock()

#load button images
start_img = pygame.image.load("StartButton.png").convert_alpha()
end_img = pygame.image.load("EndButton.png").convert_alpha()

#button class
class Button(pygame.sprite.Sprite):
  #(x,y, width, height) Width- how far from the x-starting pt Height- how far from the y-staeting pt 
  def __init__(self, x, y, image):
      # Call parent class constructor
      super().__init__()
      
      # Button attributes
      self.width = 600
      self.height = (self.width / image.get_width()) * image.get_height()
      self.image = pygame.transform.scale(image, (self.width, self.height))
      self.rect = self.image.get_rect()
      self.rect.width = self.width
      self.rect.height = self.height
      self.rect.center = (x, y)
      self.clicked = False
  
  def draw(self):
      #action is an variable name so the two buttons can perform different things
      action = False
        
      #get mouse position
      #pos is position
      pos = pygame.mouse.get_pos()

      #check mouseover and clicked conditions
      if self.rect.collidepoint(pos):
          #[0] means mouse left-click, [1] means middle-click, [2] means right-click
          #Since self.clicked is turned back to true from being false, you can only press the buttons once
          if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
              self.clicked = True
              #print("clicked")
              action = True
                
      if pygame.mouse.get_pressed()[0] == 0:
          self.clicked = False
        
      #draw button on screen
      screen.blit(self.image, (self.rect.x, self.rect.y))
      return action

#create button ex
#start_button = Button(170, 200, start_img)
#end_button = Button(220, 280, end_img)

#---Main Game Loop------
#run = True
#while run:
  #light blue 
  #screen.fill((156, 229, 255))

  #if start_button.draw():
      #print("start the game?") 
      
  #if end_button.draw():
      #print("end the game?")
      #run = False   
  
  #looks through the event queue (event handler)
  #for event in pygame.event.get():
    #quit game
    #if event.type == pygame.QUIT:
      #run = False
  #pygame.display.update()

#clean up & close
#pygame.quit()
#sys.exit()






    
