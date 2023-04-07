import pygame

pygame.init()
pygame.font.init()

class RadioButton:
  def __init__(self, x, y, size, color, selected=False, group=None, click_handler=None):
    self.rect = pygame.Rect(x, y, size, size)
    self.color = color
    self.selected = selected
    self.group = group
    self.click_handler = click_handler
    
    # If this button is part of a group, register it
    if group is not None:
      group.add_button(self)

  def draw(self, surface):
    # Draw the button outline
    pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width // 2, 3)
    # If selected, draw a filled circle in the center
    if self.selected:
      pygame.draw.circle(surface, self.color, self.rect.center, self.rect.width // 4)

  def handle_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      if self.rect.collidepoint(event.pos):
        self.selected = True
        if self.group is not None:
          self.group.deselect_other_buttons(self)
        if self.click_handler is not None:
          self.click_handler()

  def deselect(self):
    self.selected = False

class RadioButtonGroup:
  def __init__(self):
    self.buttons = []

  def add_button(self, button):
    self.buttons.append(button)

  def deselect_other_buttons(self, selected_button):
    for button in self.buttons:
      if button is not selected_button:
        button.deselect()

class Frame:
  def __init__(self, x, y, width, height, color=(255, 255, 255), border_color=(0, 0, 0), border_width=1):
    self.rect = pygame.Rect(x, y, width, height)
    self.color = color
    self.border_color = border_color
    self.border_width = border_width
    
  def draw(self, surface):
    # Draw the frame background
    pygame.draw.rect(surface, self.color, self.rect)
        
    # Draw the frame border
    border_rect = pygame.Rect(
      self.rect.x - self.border_width,
      self.rect.y - self.border_width,
      self.rect.width + self.border_width * 2,
      self.rect.height + self.border_width * 2
    )
    pygame.draw.rect(surface, self.border_color, border_rect, self.border_width)
        
  def handle_event(self, event):
    pass

class TextInput:
  def __init__(self, x, y, width, height, font_size=20, placeholder='', on_change=None, placeholder_color=(128, 128, 128), text_color=(0, 0, 0), active_color=(0, 0, 255), inactive_color=(128, 128, 128), font=None):
    self.rect = pygame.Rect(x, y, width, height)
    self.text = ''
    self.font = pygame.font.Font(font, font_size)
    self.placeholder = placeholder
    self.placeholder_color = placeholder_color
    self.text_color = text_color
    self.active_color = active_color
    self.inactive_color = inactive_color
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
  def __init__(self, x, y, size, label='', font_size=20, checked=False, color=(0, 0, 0), check_color=(255, 255, 255), font=None, group=None):
    self.rect = pygame.Rect(x, y, size, size)
    self.label = label
    self.font = pygame.font.Font(font, font_size)
    self.checked = checked
    self.color = color
    self.check_color = check_color

    # If this button is part of a group, register it
    if group is not None:
      group.add_button(self)

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
  
  def get_checked(self):
    return self.checked

class CheckboxGroup:
  def __init__(self):
    self.buttons = []

  def add_button(self, button):
    self.buttons.append(button)

  def get_states(self):
    states = []
    for button in self.buttons:
      states.append(button.get_checked())
    return states

class Button:
  def __init__(self, x, y, width, height, color=(255, 0, 0), text='', font_size=20, click_handler=None, disabled=False, font=None):
    self.rect = pygame.Rect(x, y, width, height)
    self.color = color
    self.text = text
    self.font = pygame.font.Font(font, font_size)
    self.click_handler = click_handler
    self.disabled = disabled

  def draw(self, surface):
    pygame.draw.rect(surface, self.color, self.rect)
    if self.text != '':
      text_surface = self.font.render(self.text, True, (255, 255, 255))
      text_rect = text_surface.get_rect(center=self.rect.center)
      surface.blit(text_surface, text_rect)

  def handle_event(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      if not self.disabled:
        if self.rect.collidepoint(event.pos) and event.button == 1:
          if self.click_handler is not None:
            self.click_handler()

class Text:
  def __init__(self, x, y, text, font_size=20, color=(0, 0, 0), font=None):
    self.x = x
    self.y = y
    self.text = text
    self.color = color
    self.font = pygame.font.Font(font, font_size)

  def draw(self, surface):
    text_surface = self.font.render(self.text, True, self.color)
    surface.blit(text_surface, (self.x, self.y))

  def handle_event(self, event):
    pass

class UI:
  def __init__(self, width, height, title, background_color=(255, 255, 255)):
    pygame.init()
    self.width = width
    self.height = height
    self.screen = pygame.display.set_mode((width, height))
    self.background_color = background_color
    pygame.display.set_caption(title)
    self.clock = pygame.time.Clock()
    self.elements = []

  def run(self):
    running = True
    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
        for element in self.elements:
          element.handle_event(event)

      self.screen.fill(self.background_color)
      for element in self.elements:
        element.draw(self.screen)
      pygame.display.flip()
      self.clock.tick(60)

  def add_element(self, element):
    self.elements.append(element)

  def clear_elements(self):
    self.elements = []
