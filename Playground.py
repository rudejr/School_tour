import pygame
import sys

# 초기화
pygame.init()

# 화면 크기 설정
screen_size = (1760, 1000)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Playground")

# 폰트 설정
font_path = "font/NanumGothicExtraBold.otf"
font_text = pygame.font.Font(font_path, 36)

# 이미지 관리
imageZip = {
    'DefaultImg' : pygame.transform.scale(pygame.image.load(".\img\Playground\_view.jpg"), (1520, 750)),
}

# 텍스트 관리
textZip = {
    'buildingsName' : font_text.render("운동장", True, (255, 255, 255)),
}

# Exit 버튼 정의 및 설정
white = (255, 255, 255)
black = (0, 0, 0)
button_color = (150, 150, 150)
highlight_color = (200, 200, 200)
text_color = (0, 0, 0)
button_width, button_height = 200, 60
button_spacing = 20

# 초기화
exitData = [
    {"x" : 1420, "y" : 120, "text" : "나가기"},
]

# 게임 루프
running = True
while running:
    
    for event in pygame.event.get():
        # 종료 조건 3가지 ( 창 닫기, 키보드 ESC, 버튼 '나가기' )
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            for exit_button in exitData:
                exit_button_rect = pygame.Rect(exit_button["x"], exit_button["y"], button_width, button_height)
                if exit_button_rect.collidepoint(mouse_pos):
                    running = False
    
    # UI 설정
    screen.fill((0, 0, 0))
    
    # 출력 텍스트 관리
    screen.blit(textZip['buildingsName'], (800, 135))
    
    # 출력 이미지 관리
    screen.blit(imageZip['DefaultImg'], (100, 190))
        
    # Exit 버튼 기능 관리
    for exit_button in exitData:
       exit_button_rect = pygame.Rect(exit_button["x"], exit_button["y"], button_width, button_height)

       # 마우스가 버튼 위에 있는지 확인하여 색상 변경
       if exit_button_rect.collidepoint(pygame.mouse.get_pos()):
           pygame.draw.rect(screen, highlight_color, exit_button_rect)
       else:
           pygame.draw.rect(screen, button_color, exit_button_rect)

       # 텍스트 그리기
       exit_button_font = pygame.font.Font(font_path, 20)
       exit_button_text = exit_button_font.render(exit_button["text"], True, text_color)
       exit_button_text_rect = exit_button_text.get_rect(center=exit_button_rect.center)
       screen.blit(exit_button_text, exit_button_text_rect)
    
    pygame.display.flip() # 화면 업데이트

# 게임 종료
pygame.quit()
sys.exit()
