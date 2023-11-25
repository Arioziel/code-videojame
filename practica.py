from pygame import * 
 
window = display.set_mode((700, 500)) 
display.set_caption("Detection Keys") 
 
height = 40 
width = 40 
 
x = 5 
y = 500 - height - 5 
 
character = draw.rect(window, (0, 0, 255), (x, y, width, height)) 
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
            if e.key == K_LEFT: 
                moving_left = False 
            elif e.key == K_RIGHT: 
                moving_right = False 
            elif e.key == K_UP: 
                moving_up = False 
            elif e.key == K_DOWN: 
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
 
    # Dibujar el personaje en la nueva posición 
    character = draw.rect(window, (0, 0, 255), (x, y, width, height)) 
 
    # Actualizar la pantalla 
    display.update() 
 
quit()