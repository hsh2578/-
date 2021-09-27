#기본 게임 만들때의 틀 매우매우 중요 
import random
import pygame

##############################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("혁이")

# FPS
clock = pygame.time.Clock()
##############################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)
backgrond = pygame.image.load("C:/Users/user/OneDrive/바탕 화면/python/pygame/images/배경1.png")

character = pygame.image.load("C:/Users/user/OneDrive/바탕 화면/python/pygame/images/o.png")
character_size = character.get_rect().size 
character_width = character_size[0] 
character_height = character_size[1]  
character_x_pos = (screen_width / 2) -(character_width/2) 
character_y_pos = screen_height - character_height

#똥만들기
enemy = pygame.image.load("C:\\Users\\user\\OneDrive\\바탕 화면\\python\\pygame\\images\\enemy.png")
enemy_size = enemy.get_rect().size # 이미지의 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터의 가로크기
enemy_height = enemy_size[1]  # 캐릭터의 세로 크기
enemy_x_pos = random.randrange(0,screen_width + 1 - enemy_width)
enemy_y_pos = 0
enemy_speed = 5 # 이걸 놓침 

#이동위치
to_x = 0
character_speed = 0.6

running = True
while running:
    dt = clock.tick(60)
    
    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
        
        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed      
        
        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            
    
    
    character_x_pos += to_x * dt 
    
    
    # 3.>게임 캐릭터 위치 정의
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos =random.randrange(0,screen_width + 1 - enemy_width)
    
    enemy_y_pos += enemy_speed
   
   # 4. 충돌 처리
    character_react = character.get_rect()
    character_react.left = character_x_pos
    character_react.top = character_y_pos
    
    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    
    if character_react.colliderect(enemy_rect):
        print("충돌했어요")
        running = False   
    
    # 5. 화면에 그리기
    screen.blit(backgrond, (0,0))
    
    screen.blit(character , (character_x_pos , character_y_pos)) 
    
    screen.blit(enemy , (enemy_x_pos, enemy_y_pos))
    
    
    
    pygame.display.update()

pygame.quit()