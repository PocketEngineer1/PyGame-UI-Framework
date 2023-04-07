import pygame

pygame.init()
pygame.font.init()

class Checkbox:
  def __init__(self, x, y, size, color, border_width=2, checked=False, click_handler=None):
    self.x = x
    self.y = y
    self.size = size
    self.color = color
    self.border_width = border_width
    self.checked = checked
    self.click_handler = click_handler
  
  def draw(self, surface):
    # Draw the checkbox border
    pygame.draw.rect(surface, (0, 0, 0), (self.x, self.y, self.size, self.size), self.border_width)

    # Draw the checkbox background
    pygame.draw.rect(surface, self.color, (self.x + self.border_width, self.y + self.border_width, self.size - 2 * self.border_width, self.size - 2 * self.border_width))

    # Draw the checkmark if the checkbox is checked
    if self.checked:
      check_size = int(self.size * 0.6)
      check_rect = pygame.Rect(self.x + self.size / 2 - check_size / 2, self.y + self.size / 2 - check_size / 2, check_size, check_size)
      pygame.draw.rect(surface, (0, 0, 0), check_rect)
  
  def handle_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      if self.clicked(event.pos):
        self.checked = not self.checked
        if self.click_handler is not None:
          self.click_handler(self.checked)
  
  def clicked(self, pos):
    return pos[0] > self.x and pos[0] < self.x + self.size and pos[1] > self.y and pos[1] < self.y + self.size

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

  def run(self):
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        for button in self.buttons:
          button.handle_event(event)

      self.screen.fill((255, 255, 255))
      for button in self.buttons:
        button.draw(self.screen)
      for text in self.texts:
        text.draw(self.screen)
      for checkbox in self.checkboxs:
        checkbox.draw(self.screen)
      pygame.display.flip()
      self.clock.tick(60)

  def add_button(self, button):
    self.buttons.append(button)

  def add_text(self, text):
    self.texts.append(text)

  def add_checkbox(self, checkboxs):
    self.checkboxs.append(checkboxs)

  def clear_buttons(self):
    self.buttons = []

  def clear_texts(self):
    self.texts = []

  def clear_checkboxs(self):
    self.checkboxs = []
