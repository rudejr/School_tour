import pygame
import sys
import subprocess

# 초기화
pygame.init()

# 화면 크기 설정
screen_size=(1700,890)  #캐릭터 이동범위를 위한 사이즈
screen = pygame.display.set_mode((1720,900))  

background = pygame.image.load('./img/_background.jpg')
player = pygame.image.load('./img/_player.png')
player_rect = player.get_rect()
player_rect.center = (screen_size[0] // 2, screen_size[1] // 2)

# 움직임 속도 설정
player_speed = 1

# 버튼 상태 설정
button1 = False
button2 = False
button3 = False
button4 = False
button5 = False
button6 = False
button7 = False



# 버튼 위치 및 크기 설정
button_rect1 = pygame.Rect(850, 400, 140, 30)#강석규 교육관
button_rect2 = pygame.Rect(1070, 480, 50, 40)#1공
button_rect3 = pygame.Rect(1280, 380, 50, 40)#2공
button_rect4 = pygame.Rect(650, 710, 140, 30)#학술정보관
button_rect5 = pygame.Rect(1135, 760, 120, 30)#대학교회
button_rect6 = pygame.Rect(200, 200, 80, 30)#생활관
button_rect7 = pygame.Rect(1580, 700, 80, 30)#운동장



# 폰트 설정
font_path = "font/NanumGothicExtraBold.otf"
font = pygame.font.Font(font_path, 17)

# 게임 루프
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 마우스 왼쪽 버튼 클릭
            if button1 and button_rect1.collidepoint(event.pos):
                try:
                    subprocess.run(['python', 'KangSeokGyu_EducationCenter.py'], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing 'KangSeokGyu_EducationCenter.py': {e}")
                except FileNotFoundError:
                    print("Error: 'KangSeokGyu_EducationCenter.py' not found.")
            if button2 and button_rect2.collidepoint(event.pos):
                try:
                    subprocess.run(['python', 'EngineeringHall_1.py'], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing 'EngineeringHall_1.py': {e}")
                except FileNotFoundError:
                    print("Error: 'EngineeringHall_1.py' not found.")
                 
            if button3 and button_rect3.collidepoint(event.pos):
                try:
                    subprocess.run(['python', 'EngineeringHall_2.py'], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing 'EngineeringHall_2.py': {e}")
                except FileNotFoundError:
                    print("Error: 'EngineeringHall_2.py' not found.")
                    
            if button4 and button_rect4.collidepoint(event.pos):
                try:
                    subprocess.run(['python', 'HoseoLibrary.py'], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing 'HoseoLibrary.py': {e}")
                except FileNotFoundError:
                    print("Error: 'HoseoLibrary.py' not found.")

            if button5 and button_rect5.collidepoint(event.pos):
                try:
                    subprocess.run(['python', 'Church.py'], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing 'Church.py': {e}")
                except FileNotFoundError:
                    print("Error: 'Church.py' not found.")

            if button6 and button_rect6.collidepoint(event.pos):
                try:
                    subprocess.run(['python', 'Dormitory.py'], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing 'Dormitory.py': {e}")
                except FileNotFoundError:
                    print("Error: 'Dormitory.py' not found.")

            if button7 and button_rect7.collidepoint(event.pos):
                try:
                    subprocess.run(['python', 'Playground.py'], check=True)
                except subprocess.CalledProcessError as e:
                    print(f"Error executing 'Playground.py': {e}")
                except FileNotFoundError:
                    print("Error: 'Playground.py' not found.")
                    

    keys = pygame.key.get_pressed()           
    if keys[pygame.K_UP]:
        player_rect.y -= player_speed
    if keys[pygame.K_DOWN]:
        player_rect.y += player_speed
    if keys[pygame.K_LEFT]:
        player_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_rect.x += player_speed

    # 스크린 경계 검사
    if player_rect.left < 0:
        player_rect.left = 0
    if player_rect.right > screen_size[0]:
        player_rect.right = screen_size[0]
    if player_rect.top < 0:
        player_rect.top = 0
    if player_rect.bottom > screen_size[1]:
        player_rect.bottom = screen_size[1]
        

    # 버튼을 활성화하고 버튼을 그립니다.
    if player_rect.colliderect(button_rect1) and not button1:
        button1 = True

    if player_rect.colliderect(button_rect2) and not button2:
        button2 = True

    if player_rect.colliderect(button_rect3) and not button3:
        button3 = True

    if player_rect.colliderect(button_rect4) and not button4:
        button4 = True

    if player_rect.colliderect(button_rect5) and not button5:
        button5 = True

    if player_rect.colliderect(button_rect6) and not button6:
        button6 = True

    if player_rect.colliderect(button_rect7) and not button7:
        button7 = True


    screen.blit(background, (0, 0))
    screen.blit(player, player_rect.topleft)

    # 버튼 그리기
    if button1:
        pygame.draw.rect(screen, (169, 169, 169), button_rect1)
        text1 = font.render("강석규 교육관", True, (0, 0, 0))
        screen.blit(text1, (870, 407))

    if button2:
        pygame.draw.rect(screen, (169, 169, 169), button_rect2)
        text2 = font.render("1공", True, (0, 0, 0))
        screen.blit(text2, (1080, 490))

    if button3:
        pygame.draw.rect(screen, (169, 169, 169), button_rect3)
        text3 = font.render("2공", True, (0, 0, 0))
        screen.blit(text3, (1290, 390))

    if button4:
        pygame.draw.rect(screen, (169, 169, 169), button_rect4)
        text4 = font.render("학술정보관", True, (0, 0, 0))
        screen.blit(text4, (675,715))

    if button5:
        pygame.draw.rect(screen, (169, 169, 169), button_rect5)
        text5 = font.render("대학교회", True, (0, 0, 0))
        screen.blit(text5, (1160,767))

    if button6:
        pygame.draw.rect(screen, (169, 169, 169), button_rect6)
        text6 = font.render("생활관", True, (0, 0, 0))
        screen.blit(text6, (215,207))

    if button7:
        pygame.draw.rect(screen, (169, 169, 169), button_rect7)
        text7 = font.render("운동장", True, (0, 0, 0))
        screen.blit(text7, (1595,705))

    pygame.display.flip()


# 게임 종료
pygame.quit()
sys.exit()