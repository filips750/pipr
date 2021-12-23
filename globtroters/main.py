import pygame

background_colour = (255, 255, 255)
WIDTH, HEIGTH = 900, 600
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('First Game!')

# pygame.display.flip()
def draw_window():
    WIN.fill(background_colour)
    pygame.display.update()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
