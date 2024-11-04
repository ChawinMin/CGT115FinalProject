import pygame
import pymunk
import math
import random

#Initialize the game
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800, 800))
space = pymunk.Space()
space.gravity = (0, 0)

#Initializing variables
screen_width, screen_height = screen.get_size()
center_x = screen_width // 2
center_y = screen_height // 2
rand_x = 0
rand_y = 0
score = 0
hp_list = []

#Drawing the enemies
def draw_enemy(rand_x, rand_y):
    pygame.draw.circle(screen, (255, 255, 255), (rand_x, rand_y), 10)
                       
#Creating the player
org_main_character = pygame.image.load("example_image.png").convert_alpha()

#Creating the HP
hp_image = pygame.image.load("HP.jpg").convert_alpha()

#Define projectiles
projectiles = []
projectile_speed = 10
projectile_radius = 10
projectile_color = (255, 0, 0)

#Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                #Calculate the direction for the projectile
                mouse_x, mouse_y = pygame.mouse.get_pos()
                angle = math.atan2(mouse_y - center_y, mouse_x - center_x)
                
                #Calculate the initial position and velocity of the projectile
                velocity_x = projectile_speed * math.cos(angle)
                velocity_y = projectile_speed * math.sin(angle)
                
                #Add the projectile to the list
                projectiles.append({"x":center_x, "y": center_y, "vx": velocity_x, "vy": velocity_y})
            
    #clear the screen
    screen.fill((0, 0, 0))
    
    #Get the mouse position
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    #Calculate the main character angle
    x_dist = mouse_x - center_x
    y_dist = -(mouse_y - center_y) #negative because y coord increases as you go down the screen
    angle = math.degrees(math.atan2(y_dist, x_dist))
    
    #rotate the main_character
    rotated_main_character = pygame.transform.rotate(org_main_character, angle - 90)
    main_character_rect = rotated_main_character.get_rect(center = (center_x, center_y))
    
    #draw image
    screen.blit(rotated_main_character, main_character_rect)
    
    #Adding the main text
    font = pygame.font.SysFont('Times New Roman', 30)
    text = font.render(f'Score: {score}', True, (255, 255, 255))
    screen.blit(text, (350, 0))
    
    #Update and draw each projectile
    for projectile in projectiles:
        #Update projectile position
        projectile["x"] += projectile["vx"]
        projectile["y"] += projectile["vy"]
        
        #Draw the projectile as a cirlce
        pygame.draw.circle(screen, projectile_color, (int(projectile["x"]), int(projectile["y"])), projectile_radius)
            
    #Update the display        
    pygame.display.flip()      
    
#Quit Pygame            
pygame.quit()