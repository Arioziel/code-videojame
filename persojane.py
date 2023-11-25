from pygame import *

window = display.set_mode((700, 500))
display.set_caption("Intro to Pygame")

new_height = 150
new_width = 95

x = 5
y = 500 - new_height - 5

original_character_image = image.load("dino.png")
character_image = transform.scale(original_character_image, (new_width, new_height))
character = Rect(x, y, new_width, new_height)

window.blit(character_image, (x, y))
display.update()

moving_left = False
moving_right = False
moving_up = False
moving_down = False

running = True

while running:
    time.delay(50)

    for e in event.get():
        if e.type == QUIT:
            running = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT or e.key == K_a:
                moving_left = True
            elif e.key == K_RIGHT or e.key == K_d:
                moving_right = True
            elif e.key == K_UP or e.key == K_w:
                moving_up = True
            elif e.key == K_DOWN or e.key == K_s:
                moving_down = True
            elif e.key == K_x:
                running = False
        elif e.type == KEYUP:
            if e.key == K_LEFT or e.key == K_a:
                moving_left = False
            elif e.key == K_RIGHT or e.key == K_d:
                moving_right = False
            elif e.key == K_UP or e.key == K_w:
                moving_up = False
            elif e.key == K_DOWN or e.key == K_s:
                moving_down = False

    if moving_left and character.left > 0:
        x -= 5
    if moving_right and character.right < window.get_width():
        x += 5
    if moving_up and character.top > 0:
        y -= 5
    if moving_down and character.bottom < window.get_height():
        y += 5

    window.fill((255, 255, 255))

    character = Rect(x, y, new_width, new_height)
    window.blit(character_image, (x, y))

    display.update()

quit()