import pygame
import pygame.time
import sys
import pygame_gui
from math import sqrt

pygame.init()
# Set resolution and framerate
width = 1280
height = 720
FPS = 60
ui_bound = height - height*10/72
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
manager = pygame_gui.UIManager((width, height))
# Fill background with white colour
screen.fill(((255, 255, 255)))

# Define font
f = pygame.font.SysFont("Times", 14)
# Define some variables
bp = 0.5
r = 0.5
t = 0
gp = 1/sqrt(1 - bp*bp)
L_c = width/3
L = r / gp * L_c
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
barn_color = BLACK


def draw_scene(bp, r, t):
    screen.fill(((255, 255, 255)))
    gp = 1/sqrt(1 - bp*bp)
    L = r / gp * L_c
    # Characteristic time
    tau_c = (gp + r)/(gp*bp)
    # Draw pole position
    pygame.draw.line(screen, (0, 0, 0),
                     (L_c*(1 + bp*tau_c*t) - L, ui_bound/2), (L_c*(1 + bp*tau_c*t), ui_bound/2), 2)
    # Draw UI line
    pygame.draw.line(screen, (0, 0, 0), (0, ui_bound), (width, ui_bound), 2)
    # Draw barn doors, check if pole is inside barn, color red if true
    if pole_in_barn(bp, r, t) is True:
        barn_color = RED
    else:
        barn_color = BLACK
    # Draw left barn door
    pygame.draw.line(screen, barn_color, (L_c, ui_bound), (L_c, 0), 2)
    # Draw right barn door
    pygame.draw.line(screen, barn_color, (2*L_c, ui_bound), (2*L_c, 0), 2)
    # Calculate wavefront positions
    left_dark = L_c * (1 + tau_c*t - r/(gp*bp))
    right_dark = L_c * (2 + r/(gp*bp) - tau_c*t)
    left_light = L_c * (1 + tau_c*t - 1/bp)
    right_light = L_c * (2 + 1/bp - tau_c*t)
    # Draw darkness wavefronts
    if L_c*(1 + bp*tau_c*t) - L > L_c:
        # Draw left darkness wavefront if inside barn
        if L_c * (1 + tau_c*t - r/(gp*bp)) < 2*L_c:
            pygame.draw.line(screen, GREEN, (left_dark, ui_bound), (L_c * (1 + tau_c*t - r/(gp*bp)), 0), 2)
        # Draw right darkness wavefront if inside barn
        if L_c * (2 + r/(gp*bp) - tau_c*t) > L_c:
            pygame.draw.line(screen, BLUE, (right_dark, ui_bound), (L_c * (2 + r/(gp*bp) - tau_c*t), 0), 2)
    # Draw newlight wavefronts
    if L_c*(1 + bp*tau_c*t) > 2*L_c:
        # Draw left light wavefront if not over halfway
        if L_c * (1 + tau_c*t - 1/bp) < width/2:
            pygame.draw.line(screen, GREEN, (left_light, ui_bound), (L_c * (1 + tau_c*t - 1/bp), 0), 2)
        # Draw right light wavefront if not over halfway
        if L_c * (2 + 1/bp - tau_c*t) > width/2:
            pygame.draw.line(screen, BLUE, (right_light, ui_bound), (L_c * (2 + 1/bp - tau_c*t), 0), 2)
    pygame.draw.rect(screen, RED, rect=pygame.Rect((right_dark, 0),(left_dark-right_dark, ui_bound)))


def pole_in_barn(bp, r, t):
    gp = 1/sqrt(1 - bp*bp)
    L = r / gp * L_c
    # Characteristic time
    tau_c = (gp + r)/(gp*bp)
    if L_c*(1 + bp*tau_c*t) - L > L_c and L_c*(1 + bp*tau_c*t) < 2*L_c:
        return True
    else:
        return False


def text(s, x, y, size=14, f=None):
    global screen
    if f is None:  # Create a font if needed
        f = pygame.font.SysFont(None, size)
    text = f.render(s, 1, (0, 0, 0))
    screen.blit(text, (x, y))


speed_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((40, ui_bound), (300, 40)),
                                                      start_value=0.5,
                                                      value_range=(0.00001, 0.99999),
                                                      manager=manager)

speed_textbox = pygame_gui.elements.UITextBox("β = 0.5",relative_rect=pygame.Rect((340, ui_bound), (120, 40)),
                                              manager=manager)

r_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((40, ui_bound+40), (300, 40)),
                                                  start_value=0.5,
                                                  value_range=(0,2/sqrt(3)),
                                                  manager=manager)

r_textbox = pygame_gui.elements.UITextBox("r = 0.5",relative_rect=pygame.Rect((340, ui_bound+40), (120, 40)),
                                          manager=manager)

t_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((700, ui_bound), (300, 40)),
                                                  start_value=0.001,
                                                  value_range=(0, 1),
                                                  manager=manager)

t_textbox = pygame_gui.elements.UITextBox("t = 0.001", relative_rect=pygame.Rect((700+300, ui_bound), (120, 40)),
                                          manager=manager)
while True:
    time_delta = clock.tick(FPS)/1000.0
    events = pygame.event.get()
    pygame.event.get()
    clock.tick(FPS)
    mouseX, mouseY = pygame.mouse.get_pos()

    # Allow exit of program using the X button
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == speed_slider:
                    bp = event.value
                    # Change the textbox to current speed
                    speed_textbox.html_text = "β = " + str(round(bp, 5))
                    speed_textbox.rebuild()
                    gp = 1/sqrt(1 - bp*bp)
                    # Adjust slider range for r to new gamma factor
                    r_slider.value_range = (0.00001, gp)
                    r_slider.rebuild()
                    draw_scene(bp, r, t)
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == r_slider:
                    r = event.value
                    # Change the textbox to current ratio
                    r_textbox.html_text = "r = " + str(round(r, 5))
                    r_textbox.rebuild()
                    draw_scene(bp, r, t)
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                if event.ui_element == t_slider:
                    t = event.value
                    # Change the textbox to current time
                    t_textbox.html_text = "t = " + str(round(t, 5))
                    t_textbox.rebuild()
                    draw_scene(bp, r, t)
        manager.process_events(event)

    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.update()
