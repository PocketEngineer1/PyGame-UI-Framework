from UI_Framework import *

def hello():
  print('Hello World!')

ui = UI(800, 600, 'Example')
button = Button(100, 100, 200, 50, (255, 0, 0), 'Click me!', click_handler=hello)
text = Text(100, 80, 'Hello World!')
checkbox = Checkbox(20, 20, 20, (255, 0, 0))
# text_input = TextInput(100, 200, 200, 50, text='i am confusion')
ui.add_button(button)
ui.add_text(text)
ui.add_checkbox(checkbox)
# ui.add_text_input(text_input)
ui.run()
