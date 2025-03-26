def universal_draw(screen, text, font, color, x, y): 
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x,y))
    