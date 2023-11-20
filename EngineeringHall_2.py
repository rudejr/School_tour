import pygame
import sys

# 초기화
pygame.init()

# 화면 크기 설정
screen_size = (1760, 1000)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("EngineeringHall_2")

# 폰트 설정
font_path = "font/NanumGothicExtraBold.otf"
font_text = pygame.font.Font(font_path, 36)

# 이미지 관리
imageZip = {
    'DefaultImg' : pygame.transform.scale(pygame.image.load(".\img\EngineeringHall_2\_stairs.jpg"), (620, 820)),
    'img5' : pygame.transform.scale(pygame.image.load(".\img\EngineeringHall_2\_5F\_hallway.jpg"), (740, 500)),
    'img4' : pygame.transform.scale(pygame.image.load(".\img\EngineeringHall_2\_4F\_hall.jpg"), (740, 500)),
    'img3' : pygame.transform.scale(pygame.image.load(".\img\EngineeringHall_2\_3F\_hallway.jpg"), (740, 500)),
    'img2' : pygame.transform.scale(pygame.image.load(".\img\EngineeringHall_2\_2F\_hallway.jpg"), (740, 500)),
    'img1' : pygame.transform.scale(pygame.image.load(".\img\EngineeringHall_2\_1F\_hallway.jpg"), (740, 500)),
    'img0' : pygame.transform.scale(pygame.image.load(".\img\EngineeringHall_2\_1B\_hallway.jpg"), (740, 500)),
}

# 텍스트 관리
textZip = {
    'buildingsName' : font_text.render("제 2공학관", True, (255, 255, 255)),
    '5F' : font_text.render("5층", True, (255, 255, 255)),
    '4F' : font_text.render("4층", True, (255, 255, 255)),
    '3F' : font_text.render("3층", True, (255, 255, 255)),
    '2F' : font_text.render("2층", True, (255, 255, 255)),
    '1F' : font_text.render("1층", True, (255, 255, 255)),
    '1B' : font_text.render("지하 1층", True, (255, 255, 255)),
}

# 엘리베이터 버튼 설정
button_radius = 29
button_color = (255, 255, 255)
button_font = pygame.font.Font(None, 36)

button_coordinates = [(800, 920), (800, 820), (800, 720), (800, 620), (800, 520), (800, 420)]
button_x5, button_y5 = button_coordinates[5]
button_x4, button_y4 = button_coordinates[4]
button_x3, button_y3 = button_coordinates[3]
button_x2, button_y2 = button_coordinates[2]
button_x1, button_y1 = button_coordinates[1]
button_x0, button_y0 = button_coordinates[0]

def draw_button(x, y, radius, color, text_surface):
    pygame.draw.ellipse(screen, color, (x - radius, y - radius, 2 * radius, 2 * radius))
    text_x = x - radius // 2
    text_y = y - radius // 2
    screen.blit(text_surface, (text_x, text_y))
    
def is_button_clicked(button_x, button_y, radius, mouse_pos):
    distance = ((mouse_pos[0] - button_x) ** 2 + (mouse_pos[1] - button_y) ** 2) ** 0.5
    return distance <= radius

# Room 버튼 정의 및 설정
white = (255, 255, 255)
black = (0, 0, 0)
button_color = (150, 150, 150)
highlight_color = (200, 200, 200)
text_color = (0, 0, 0)
button_width, button_height = 200, 60
button_spacing = 20

# 초기화
current_image_key = None
current_text_key = None
roomImage = None
roomData = []
exitData = [
    {"x" : 1420, "y" : 120, "text" : "건물 나가기"},
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
        
        # 엘리베이터 버튼 상황별 관리
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()
            if is_button_clicked(button_x5, button_y5, button_radius, mouse_pos):
                roomImage = None
                current_text_key = '5F'
                current_image_key = 'img5'
                roomData = [
                    {"x" : 900,  "y" : 720, "text" : "컴퓨터네트워크실습실", "image_path" : ".\img\EngineeringHall_2\_5F\_lectureRoom1.jpg"},
                    {"x" : 1150, "y" : 720, "text" : "강의실", "image_path" : ".\img\EngineeringHall_2\_5F\_lectureRoom2.jpg"},
                    {"x" : 1400, "y" : 720, "text" : "강의실", "image_path" : ".\img\EngineeringHall_2\_5F\_lectureRoom3.jpg"},
                    {"x" : 900,  "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1150, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1400, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                ]
            if is_button_clicked(button_x4, button_y4, button_radius, mouse_pos):
                roomImage = None
                current_text_key = '4F'
                current_image_key = 'img4'
                roomData = [
                    {"x" : 900,  "y" : 720, "text" : "응용소프트웨어실습실", "image_path" : ".\img\EngineeringHall_2\_4F\_lectureRoom1.jpg"},
                    {"x" : 1150, "y" : 720, "text" : "오픈소스실습실", "image_path" : ".\img\EngineeringHall_2\_4F\_lectureRoom2.jpg"},
                    {"x" : 1400, "y" : 720, "text" : "강의실", "image_path" : ".\img\EngineeringHall_2\_4F\_lectureRoom3.jpg"},
                    {"x" : 900,  "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1150, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1400, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                ]
            if is_button_clicked(button_x3, button_y3, button_radius, mouse_pos):
                roomImage = None
                current_text_key = '3F'
                current_image_key = 'img3'
                roomData = [
                    {"x" : 900,  "y" : 720, "text" : "강의실", "image_path" : ".\img\EngineeringHall_2\_3F\_lectureRoom1.jpg"},
                    {"x" : 1150, "y" : 720, "text" : "강의실", "image_path" : ".\img\EngineeringHall_2\_3F\_lectureRoom2.jpg"},
                    {"x" : 1400, "y" : 720, "text" : "강의실", "image_path" : ".\img\EngineeringHall_2\_3F\_lectureRoom3.jpg"},
                    {"x" : 900,  "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1150, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1400, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                ]
            if is_button_clicked(button_x2, button_y2, button_radius, mouse_pos):
                roomImage = None
                current_text_key = '2F'
                current_image_key = 'img2'
                roomData = [
                    {"x" : 900,  "y" : 720, "text" : "강의실", "image_path" : ".\img\EngineeringHall_2\_2F\_lectureRoom1.jpg"},
                    {"x" : 1150, "y" : 720, "text" : "강의실", "image_path" : ".\img\EngineeringHall_2\_2F\_lectureRoom2.jpg"},
                    {"x" : 1400, "y" : 720, "text" : "강의실", "image_path" : ".\img\EngineeringHall_2\_2F\_lectureRoom3.jpg"},
                    {"x" : 900,  "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1150, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1400, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                ]
            if is_button_clicked(button_x1, button_y1, button_radius, mouse_pos):
                roomImage = None
                current_text_key = '1F'
                current_image_key = 'img1'
                roomData = [
                    {"x" : 900,  "y" : 720, "text" : "대강의실", "image_path" : ".\img\EngineeringHall_2\_1F\_lectureRoom1.jpg"},
                    {"x" : 1150, "y" : 720, "text" : "강의실", "image_path" : ".\img\EngineeringHall_2\_1F\_lectureRoom2.jpg"},
                    {"x" : 1400, "y" : 720, "text" : "강의실", "image_path" : ".\img\EngineeringHall_2\_1F\_lectureRoom3.jpg"},
                    {"x" : 900,  "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1150, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1400, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                ]
            if is_button_clicked(button_x0, button_y0, button_radius, mouse_pos):
                roomImage = None
                current_text_key = '1B'
                current_image_key = 'img0'
                roomData = [
                    {"x" : 900,  "y" : 720, "text" : "강의실", "image_path" : ".\img\EngineeringHall_2\_1B\_lectureRoom1.jpg"},
                    {"x" : 1150, "y" : 720, "text" : "깅의실", "image_path" : ".\img\EngineeringHall_2\_1B\_lectureRoom2.jpg"},
                    {"x" : 1400, "y" : 720, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 900,  "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1150, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1400, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                ]
        
        # ROOM 버튼 상황별 관리
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for button in roomData:
                    button_rect = pygame.Rect(button["x"], button["y"], button_width, button_height)
                    if button_rect.collidepoint(event.pos):
                        roomImage = pygame.transform.scale(pygame.image.load(button["image_path"]), (740, 500))
    
    # UI 설정
    screen.fill((0, 0, 0))
    
    # 엘리베이터 버튼 그리기
    draw_button(button_x5, button_y5, button_radius, button_color, button_font.render("5F", True, (0, 0, 0)))
    draw_button(button_x4, button_y4, button_radius, button_color, button_font.render("4F", True, (0, 0, 0)))
    draw_button(button_x3, button_y3, button_radius, button_color, button_font.render("3F", True, (0, 0, 0)))
    draw_button(button_x2, button_y2, button_radius, button_color, button_font.render("2F", True, (0, 0, 0)))
    draw_button(button_x1, button_y1, button_radius, button_color, button_font.render("1F", True, (0, 0, 0)))
    draw_button(button_x0, button_y0, button_radius, button_color, button_font.render("B1", True, (0, 0, 0)))
    
    # 출력 텍스트 관리
    screen.blit(textZip['buildingsName'], (100, 70))
    if current_text_key is not None:
        screen.blit(textZip[current_text_key], (880, 135))
    
    # 출력 이미지 관리
    screen.blit(imageZip['DefaultImg'], (100, 120))
    if current_image_key is not None:
        screen.blit(imageZip[current_image_key], (880, 190))
    if roomImage is not None:
        screen.blit(roomImage, (880, 190))
        
    # 출력 버튼 : ROOM 관리
    for button in roomData:
        button_rect = pygame.Rect(button["x"], button["y"], button_width, button_height)

        # 마우스가 버튼 위에 있는지 확인하여 색상 변경
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, highlight_color, button_rect)
        else:
            pygame.draw.rect(screen, button_color, button_rect)

        # 텍스트 그리기
        font = pygame.font.Font(font_path, 20)
        text = font.render(button["text"], True, text_color)
        text_rect = text.get_rect(center=button_rect.center)
        screen.blit(text, text_rect) 
        
    # 출력 버튼 : '나가기' 관리
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
