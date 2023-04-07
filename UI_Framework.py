import pygame

class Button:
  def __init__(self, position: tuple, size: tuple, color: tuple, text='', font_size=20, click_handler=None, button=0):
    self.rect = pygame.Rect(position[0], position[1], size[0], size[1])
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
      if self.button == 0:
        if self.rect.collidepoint(event.pos):
          if self.click_handler is not None:
            self.click_handler()

class Text:
  def __init__(self, size: tuple, text, font_size=20, color=(0, 0, 0)):
    self.x = size[0]
    self.y = size[1]
    self.text = text
    self.color = color
    self.font = pygame.font.Font(None, font_size)

  def draw(self, surface):
    text_surface = self.font.render(self.text, True, self.color)
    surface.blit(text_surface, (self.x, self.y))

class UI:
  def __init__(self, size: tuple, title):
    pygame.init()
    self.width = size[0]
    self.height = size[1]
    self.screen = pygame.display.set_mode(size)
    pygame.display.set_caption(title)
    self.clock = pygame.time.Clock()
    self.buttons = []
    self.texts = []

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
      pygame.display.flip()
      self.clock.tick(60)

  def add_button(self, button):
    self.buttons.append(button)

  def add_text(self, text):
    self.texts.append(text)

  def clear_buttons(self):
    self.buttons = []

  def clear_texts(self):
    self.texts = []
