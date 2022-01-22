import pygame
import pygame_gui
from pygame_textinput import TextInputVisualizer, TextInputManager
from unpack_settings import load_and_unpack_settings_yaml

colors, settings = load_and_unpack_settings_yaml()


def save_from_input(WIN, color_or_name):
    my_font = pygame.font.SysFont(settings['FONT'], 20)
    manager1 = TextInputManager(validator=lambda input: len(input) <= 10)
    textinput = TextInputVisualizer(manager=manager1, font_object=my_font)
    events = pygame.event.get()
    pygame.font.init()
    run_2nd = True
    while run_2nd:
        pygame.display.update()
        WIN.fill(colors['WHITE'])
        events = pygame.event.get()
        WIN.blit(textinput.surface, (10, 10))
        textinput.update(events)
        for event in events:
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                print(f"User pressed enter! Input to two: {textinput.value}")
                color_or_name += 1
                return textinput.value, color_or_name



def ui():
    player_number = 0
    players_number = None
    players_list = []
    pygame.init()
    WIN = pygame.display.set_mode(settings['RESOLUTION'])
    manager = pygame_gui.UIManager(settings['RESOLUTION'])
    button_pressed = False
    if not button_pressed:
        button_width = 250
        x = settings['RESOLUTION'][0]//2 - button_width
        y = settings['RESOLUTION'][1]//4
        two_player_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y), (button_width*2, 50)),
                                                text='Two players game',
                                                manager=manager)
        three_player_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, 450), (button_width, 50)),
                                                text='Three players game',
                                                manager=manager)
        four_player_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x + button_width+10, 450), (button_width, 50)),
                                                text='Four players game',
                                                manager=manager)

    clock = pygame.time.Clock()
    pygame.key.set_repeat(200, 25)
    break_all = False
    run = True
    color_or_name = 0
    while run:
        pygame.display.update()
        pygame.font.init()
        manager.update(clock.tick(60)/1000)
        if not button_pressed:
            manager.draw_ui(WIN)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False
            if not button_pressed:
                if event.type == pygame_gui.UI_BUTTON_PRESSED:
                    button_pressed = True
                    if event.ui_element == two_player_button:
                        players_number = 2
                    if event.ui_element == three_player_button:
                        players_number = 3
                    if event.ui_element == four_player_button:
                        players_number = 4
            manager.process_events(event)
        if button_pressed:
            for player_number in range(players_number):
                my_list = []
                if player_number <= players_number and color_or_name % 2 == 0:
                    result = save_from_input(WIN, color_or_name)
                    if result:
                        value, color_or_name = result
                        my_list.append(value)
                    else:
                        break_all = True
                        break
                if player_number <= players_number and color_or_name % 2 == 1:
                    result = save_from_input(WIN, color_or_name)
                    if result:
                        value, color_or_name = result
                        my_list.append(value)

                    else:
                        break_all = True
                        break
                    players_list.append(my_list)
        if break_all:
            run = False
            break
        pygame.display.update()
        manager.update(clock.tick(60)/1000)
        if len(players_list) == players_number:
            return players_list
