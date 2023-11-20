import pygame
import sys

# 초기화
pygame.init()

# 화면 크기 설정
screen_size = (1760, 1000)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("HoseoLibrary")

# 폰트 설정
font_path = "font/NanumGothicExtraBold.otf"
font_text = pygame.font.Font(font_path, 36)

# 이미지 관리
imageZip = {
    'DefaultImg' : pygame.transform.scale(pygame.image.load(".\img\HoseoLibrary\_elevatorImg.jpg"), (620, 820)),
    'img6' : pygame.transform.scale(pygame.image.load(".\img\HoseoLibrary\_6F\_hallway.jpg"), (740, 500)),
    'img5' : pygame.transform.scale(pygame.image.load(".\img\HoseoLibrary\_5F\_place.jpg"), (740, 500)),
    'img4' : pygame.transform.scale(pygame.image.load(".\img\HoseoLibrary\_4F\_hall.jpg"), (740, 500)),
    'img3' : pygame.transform.scale(pygame.image.load(".\img\HoseoLibrary\_3F\_hall.jpg"), (740, 500)),
    'img2' : pygame.transform.scale(pygame.image.load(".\img\HoseoLibrary\_2F\_hall.jpg"), (740, 500)),
    'img1' : pygame.transform.scale(pygame.image.load(".\img\HoseoLibrary\_1F\_stairs.jpg"), (740, 500)),
    'img0' : pygame.transform.scale(pygame.image.load(".\img\HoseoLibrary\_1B\_hall.jpg"), (740, 500)),
}

# 텍스트 관리
textZip = {
    'buildingsName' : font_text.render("학술정보관", True, (255, 255, 255)),
    '6F' : font_text.render("6층", True, (255, 255, 255)),
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

button_coordinates = [(800, 920), (800, 820), (800, 720), (800, 620), (800, 520), (800, 420), (800, 320)]
button_x6, button_y6 = button_coordinates[6]
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
            if is_button_clicked(button_x6, button_y6, button_radius, mouse_pos):
                roomImage = None
                current_text_key = '6F'
                current_image_key = 'img6'
                roomData = [
                    {"x" : 900,  "y" : 720, "text" : "상성전시실", "image_path" : ".\img\HoseoLibrary\_6F\_showroom1.jpg"},
                    {"x" : 1150, "y" : 720, "text" : "기획전시실", "image_path" : ".\img\HoseoLibrary\_6F\_showroom2.jpg"},
                    {"x" : 1400, "y" : 720, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 900,  "y" : 820, "text" : "테라스라운지", "image_path" : ".\img\HoseoLibrary\_6F\_terrace1.jpg"},
                    {"x" : 1150, "y" : 820, "text" : "테라스라운지", "image_path" : ".\img\HoseoLibrary\_6F\_terrace2.jpg"},
                    {"x" : 1400, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                ]
            if is_button_clicked(button_x5, button_y5, button_radius, mouse_pos):
                roomImage = None
                current_text_key = '5F'
                current_image_key = 'img5'
                roomData = [
                    {"x" : 900,  "y" : 720, "text" : "북카페", "image_path" : ".\img\HoseoLibrary\_5F\_learningSpace1.jpg"},
                    {"x" : 1150, "y" : 720, "text" : "학습공간", "image_path" : ".\img\HoseoLibrary\_5F\_learningSpace2.jpg"},
                    {"x" : 1400, "y" : 720, "text" : "학습공간", "image_path" : ".\img\HoseoLibrary\_5F\_learningSpace3.jpg"},
                    {"x" : 900,  "y" : 820, "text" : "휴식공간", "image_path" : ".\img\HoseoLibrary\_5F\_restArea.jpg"},
                    {"x" : 1150, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1400, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                ]
            if is_button_clicked(button_x4, button_y4, button_radius, mouse_pos):
                roomImage = None
                current_text_key = '4F'
                current_image_key = 'img4'
                roomData = [
                    {"x" : 900,  "y" : 720, "text" : "학습공간", "image_path" : ".\img\HoseoLibrary\_4F\_learningSpace1.jpg"},
                    {"x" : 1150, "y" : 720, "text" : "학습공간", "image_path" : ".\img\HoseoLibrary\_4F\_learningSpace2.jpg"},
                    {"x" : 1400, "y" : 720, "text" : "비대면학습실", "image_path" : ".\img\HoseoLibrary\_4F\_learningSpace3.jpg"},
                    {"x" : 900,  "y" : 820, "text" : "프린트실", "image_path" : ".\img\HoseoLibrary\_4F\_printRoom.jpg"},
                    {"x" : 1150, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1400, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                ]
            if is_button_clicked(button_x3, button_y3, button_radius, mouse_pos):
                roomImage = None
                current_text_key = '3F'
                current_image_key = 'img3'
                roomData = [
                    {"x" : 900,  "y" : 720, "text" : "학습공간", "image_path" : ".\img\HoseoLibrary\_3F\_learningSpace1.jpg"},
                    {"x" : 1150, "y" : 720, "text" : "그룹스터디룸", "image_path" : ".\img\HoseoLibrary\_3F\_groupStudyRoom1.jpg"},
                    {"x" : 1400, "y" : 720, "text" : "일반열람실 A", "image_path" : ".\img\HoseoLibrary\_3F\eadingRoomA.jpg"},
                    {"x" : 900,  "y" : 820, "text" : "학습공간", "image_path" : ".\img\HoseoLibrary\_3F\_learningSpace2.jpg"},
                    {"x" : 1150, "y" : 820, "text" : "그룹스터디룸", "image_path" : ".\img\HoseoLibrary\_3F\_groupStudyRoom2.jpg"},
                    {"x" : 1400, "y" : 820, "text" : "일반열람실 B", "image_path" : ".\img\HoseoLibrary\_3F\eadingRoomB.jpg"},
                ]
            if is_button_clicked(button_x2, button_y2, button_radius, mouse_pos):
                roomImage = None
                current_text_key = '2F'
                current_image_key = 'img2'
                roomData = [
                    {"x" : 900,  "y" : 720, "text" : "24시간 열람실", "image_path" : ".\img\HoseoLibrary\_2F\_24readingRoom.jpg"},
                    {"x" : 1150, "y" : 720, "text" : "노트북 존", "image_path" : ".\img\HoseoLibrary\_2F\_notebookZone.jpg"},
                    {"x" : 1400, "y" : 720, "text" : "정보검색실", "image_path" : ".\img\HoseoLibrary\_2F\_searchRoom.jpg"},
                    {"x" : 900,  "y" : 820, "text" : "프린트실", "image_path" : ".\img\HoseoLibrary\_2F\printRoom.jpg"},
                    {"x" : 1150, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                    {"x" : 1400, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                ]
            if is_button_clicked(button_x1, button_y1, button_radius, mouse_pos):
                roomImage = None
                current_text_key = '1F'
                current_image_key = 'img1'
                roomData = [
                    {"x" : 900,  "y" : 720, "text" : "학습공간", "image_path" : ".\img\HoseoLibrary\_1F\_learningSpace1.jpg"},
                    {"x" : 1150, "y" : 720, "text" : "학습공간", "image_path" : ".\img\HoseoLibrary\_1F\_learningSpace2.jpg"},
                    {"x" : 1400, "y" : 720, "text" : "학습공간", "image_path" : ".\img\HoseoLibrary\_1F\_learningSpace3.jpg"},
                    {"x" : 900,  "y" : 820, "text" : "미끄럼틀", "image_path" : ".\img\HoseoLibrary\_1F\_slide.jpg"},
                    {"x" : 1150, "y" : 820, "text" : "시네마룸", "image_path" : ".\img\HoseoLibrary\_1F\_cinemaRoom.jpg"},
                    {"x" : 1400, "y" : 820, "text" : " ", "image_path" : ".\img\_blank.jpg"},
                ]
            if is_button_clicked(button_x0, button_y0, button_radius, mouse_pos):
                roomImage = None
                current_text_key = '1B'
                current_image_key = 'img0'
                roomData = [
                    {"x" : 900,  "y" : 720, "text" : "카페", "image_path" : ".\img\HoseoLibrary\_1B\_cafe.jpg"},
                    {"x" : 1150, "y" : 720, "text" : "편의점", "image_path" : ".\img\HoseoLibrary\_1B\_convenienceStore.jpg"},
                    {"x" : 1400, "y" : 720, "text" : "그룹스터디룸", "image_path" : ".\img\HoseoLibrary\_1B\_groupStudyRoom.jpg"},
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
    
    # 엘리베이터 버튼 표시
    draw_button(button_x6, button_y6, button_radius, button_color, button_font.render("6F", True, (0, 0, 0)))
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
