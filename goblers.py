import pygame

background_colour = (255, 255, 255)
WIDTH, HEIGTH = 900, 600
BLACK = (0, 0, 0)
BANANA = (227, 207, 87)
DARKOCHID3 = (154, 50, 205)
WIN = pygame.display.set_mode((WIDTH, HEIGTH))
pygame.display.set_caption('Gobblet Gobblers')

pygame.draw.circle(WIN, BANANA, (450, 300), 20)
# pygame.display.flip()


def draw_window():
    WIN.fill(background_colour)
    pygame.display.update()

# pygame.transform.scale()


def main():
    draw_window()
    # to do update window every click
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.draw.circle(WIN, BLACK, (450, 300), 80, 80)
        pygame.draw.circle(WIN, BANANA, (450, 300), 100, 80)
        pygame.draw.circle(WIN, DARKOCHID3, (50, 50), 40, 40)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
