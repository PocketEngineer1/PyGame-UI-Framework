#!/usr/bin/python3

from UI_Framework import *

def hello():
  print('Hello World!')

def handle_text_change(text):
  print("Text input changed:", text)

ui = UI(800, 600, 'Example')

button = Button(5, 5, 200, 50, (255, 0, 0), 'Click me!', click_handler=hello)
text = Text(210, 5, 'Hello World!')
checkbox = Checkbox(210, 20, 20, check_color=(0, 0, 0))
text_input = TextInput(5, 60, 200, 30, placeholder="Type something", on_change=handle_text_change)
frame = Frame(5, 95, 200, 30, color=(200, 200, 200))

radio_button_group = RadioButtonGroup()
radio_button_1 = RadioButton(5, 130, 20, (0, 0, 0), group=radio_button_group)
radio_button_2 = RadioButton(30, 130, 20, (0, 0, 0), group=radio_button_group)
radio_button_3 = RadioButton(55, 130, 20, (0, 0, 0), group=radio_button_group)

ui.add_element(button)
ui.add_element(text)
ui.add_element(checkbox)
ui.add_element(text_input)
ui.add_element(frame)

ui.add_element(radio_button_1)
ui.add_element(radio_button_2)
ui.add_element(radio_button_3)

ui.run()
