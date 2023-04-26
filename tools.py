import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from screen import *

slider = Slider(screen, 400, 500, 800, 20, initial = 100, min=0, max=99, step=1, colour=(255, 255, 255))
text = TextBox(screen, 1350, 485, 50, 50, fontSize=30)
text.disable()