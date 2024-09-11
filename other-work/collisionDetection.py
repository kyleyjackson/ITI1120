# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

rect1 = pygame.Rect(0, 0, 100, 100)
rect2 = pygame.Rect(1180, 620, 100, 100)
rect3 = pygame.Rect(0, 0, 100, 100)

if rect1.colliderect(rect2):
    pygame.draw.rect(screen, "purple", rect3)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.rect(screen, "red", rect1)
    pygame.draw.rect(screen, "blue", rect2)

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_w]:
        rect1.y -= 300 * dt
    if keys[pygame.K_s]:
        rect1.y += 300 * dt
    if keys[pygame.K_a]:
        rect1.x -= 300 * dt
    if keys[pygame.K_d]:
        rect1.x += 300 * dt
        
    if keys[pygame.K_UP]:
        rect2.y -= 300 * dt
    if keys[pygame.K_DOWN]:
        rect2.y += 300 * dt
    if keys[pygame.K_LEFT]:
        rect2.x -= 300 * dt
    if keys[pygame.K_RIGHT]:
        rect2.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()