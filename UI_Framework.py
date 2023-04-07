import pygame

pygame.init()
pygame.font.init()

class TextInput:
  def __init__(self, x, y, width, height, font_size=20, placeholder='', on_change=None):
    self.rect = pygame.Rect(x, y, width, height)
    self.text = ''
    self.font = pygame.font.Font(None, font_size)
    self.placeholder = placeholder
    self.placeholder_color = (128, 128, 128)
    self.text_color = (0, 0, 0)
    self.active_color = (0, 0, 255)
    self.inactive_color = (128, 128, 128)
    self.active = False
    self.on_change = on_change

  def draw(self, surface):
    # Draw the text input box
    pygame.draw.rect(surface, self.active_color if self.active else self.inactive_color, self.rect, 2)

    # Draw the text if it exists
    if self.text != '':
      text_surface = self.font.render(self.text, True, self.text_color)
      surface.blit(text_surface, (self.rect.x + 5, self.rect.y + 5))
    # Draw the placeholder text if the input is empty
    else:
      placeholder_surface = self.font.render(self.placeholder, True, self.placeholder_color)
      surface.blit(placeholder_surface, (self.rect.x + 5, self.rect.y + 5))

  def handle_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      # Toggle the active state of the input if clicked on
      if self.rect.collidepoint(event.pos):
        self.active = not self.active
      else:
        self.active = False
      # Update the text color based on the active state
      self.text_color = (0, 0, 0) if self.active else (128, 128, 128)
    elif event.type == pygame.KEYDOWN:
      # Add characters to the input text if active
      if self.active:
        if event.key == pygame.K_RETURN:
          self.active = False
        elif event.key == pygame.K_BACKSPACE:
          self.text = self.text[:-1]
        else:
          self.text += event.unicode
        # Call the on_change function if it exists
        if self.on_change is not None:
          self.on_change(self.text)

class Checkbox:
  def __init__(self, x, y, size, label='', font_size=20, checked=False, color=(0, 0, 0), check_color=(255, 255, 255)):
    self.rect = pygame.Rect(x, y, size, size)
    self.label = label
    self.font = pygame.font.Font(None, font_size)
    self.checked = checked
    self.color = color
    self.check_color = check_color

  def draw(self, surface):
    pygame.draw.rect(surface, self.color, self.rect, 2)
    if self.checked:
      pygame.draw.line(surface, self.check_color, (self.rect.left + 5, self.rect.centery), (self.rect.centerx, self.rect.bottom - 5), 2)
      pygame.draw.line(surface, self.check_color, (self.rect.centerx, self.rect.bottom - 5), (self.rect.right - 5, self.rect.top + 5), 2)

    if self.label:
      label_text = self.font.render(self.label, True, self.color)
      label_rect = label_text.get_rect(left=self.rect.right + 10, centery=self.rect.centery)
      surface.blit(label_text, label_rect)

  def handle_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      if self.rect.collidepoint(event.pos):
        self.checked = not self.checked

class Button:
  def __init__(self, x, y, width, height, color: tuple, text='', font_size=20, click_handler=None, button=1):
    self.rect = pygame.Rect(x, y, width, height)
    self.color = color
    self.text = text
    self.font = pygame.font.Font(None, font_size)
    self.click_handler = click_handler
    self.button = button

  def draw(self, surface):
    pygame.draw.rect(surface, self.color, self.rect)
    if self.text != '':
      text_surface = self.font.render(self.text, True, (255, 255, 255))
      text_rect = text_surface.get_rect(center=self.rect.center)
      surface.blit(text_surface, text_rect)

  def handle_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      if self.rect.collidepoint(event.pos) and event.button == self.button:
        if self.click_handler is not None:
          self.click_handler()
      elif self.button == 0:
        if self.rect.collidepoint(event.pos):
          if self.click_handler is not None:
            self.click_handler()

class Text:
  def __init__(self, x, y, text, font_size=20, color=(0, 0, 0)):
    self.x = x
    self.y = y
    self.text = text
    self.color = color
    self.font = pygame.font.Font(None, font_size)

  def draw(self, surface):
    text_surface = self.font.render(self.text, True, self.color)
    surface.blit(text_surface, (self.x, self.y))

class UI:
  def __init__(self, width, height, title):
    pygame.init()
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption(title)
    self.clock = pygame.time.Clock()
    self.buttons = []
    self.texts = []
    self.checkboxs = []
    self.text_inputs = []

  def run(self):
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        for button in self.buttons:
          button.handle_event(event)
        for checkbox in self.checkboxs:
          checkbox.handle_event(event)
        for text_input in self.text_inputs:
          text_input.handle_event(event)

      self.screen.fill((255, 255, 255))
      for button in self.buttons:
        button.draw(self.screen)
      for text in self.texts:
        text.draw(self.screen)
      for checkbox in self.checkboxs:
        checkbox.draw(self.screen)
      for text_input in self.text_inputs:
        text_input.draw(self.screen)
      pygame.display.flip()
      self.clock.tick(60)

  def add_button(self, button):
    self.buttons.append(button)

  def add_text(self, text):
    self.texts.append(text)

  def add_checkbox(self, checkbox):
    self.checkboxs.append(checkbox)

  def add_text_input(self, textinput):
    self.text_inputs.append(textinput)

  def clear_buttons(self):
    self.buttons = []

  def clear_texts(self):
    self.texts = []

  def clear_checkboxs(self):
    self.checkboxs = []

  def clear_text_inputs(self):
    self.text_inputs = []
