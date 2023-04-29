import pygame

class Button():
    def __init__(
            self, x=0, y=0, width=10, height=10,
            text='default', text_color=(255,255,255), normal_color=(235,64,52),
            hover_color=(189,49,40), center_x=True, font='Arial',
            font_size=20, border_radius=10
    ):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.text_color = text_color
        self.normal_color = normal_color
        self.hover_color = hover_color
        self.font_name = font
        self.font_size = font_size
        self.border_radius = border_radius
        if center_x:
            w_width, w_height = pygame.display.get_window_size()
            window_rect = pygame.Rect(0,0,w_width,w_height)
            self.rect.centerx = window_rect.centerx
        self.is_hovered = False

    def update(self, events):
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    self.is_hovered = True
                else:
                    self.is_hovered = False
    
    def draw(self,window):
        text_font = pygame.font.SysFont(self.font_name,self.font_size)
        text_image = text_font.render(self.text, True, self.text_color) 
        text_rect = text_image.get_rect()
        text_rect.center = self.rect.center
        if self.is_hovered:
            color = self.hover_color
        else:
            color = self.normal_color
        pygame.draw.rect(window,color,self.rect, border_radius=self.border_radius)
        window.blit(text_image,(text_rect.x, text_rect.y))

    def is_clicked(self,events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    return True
        return False

pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill((100, 100, 255))
clock = pygame.time.Clock()

btn = Button(y=70, width=150, height=50, text='Начать игру')

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
    
    btn.update(events)
    if btn.is_clicked(events):
        print('НАЖАТО!')
    btn.draw(window)

    clock.tick(60)
    pygame.display.update()
