from UI_Framework import *

def hello(
  print('Hello World!')
ui = UI((800, 600), 'Example')
button = Button((100, 100), (200, 50), (255, 0, 0), 'Click me!', click_handler=hello)
ui.add_button(button)
ui.run()
