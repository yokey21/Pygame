import sys, pygame

pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0

# track if ball is stopped
stopped = 0

screen = pygame.display.set_mode(size)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        pressed = pygame.key.get_pressed()
        # if 'w' key is pressed
        if pressed[pygame.K_SPACE]:
            if stopped == 1:
                print("GO")
                stopped = 0
                speed = [2, 2]
            elif stopped == 0:
                print("STOP")
                stopped = 1
                speed = [0, 0]


    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()