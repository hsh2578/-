import pygame

pygame.init() #초기화 반디시 필요

#화면 크기 설정 
screen_width = 240 # 가로크기 # 500이 최대여서 절반으로 줄임
screen_height = 480 # 세로 크기
screen = pygame.display.set_mode((screen_width , screen_height))
# 화면 타이틀 설정 
pygame.display.set_caption("성혁") # 게임 이름 여기서 실수했다 

#배경 이미지 불러오기
backgrond = pygame.image.load("C:/Users/user/OneDrive/바탕 화면/python/pygame/배경.png")
#캐릭터 이미지 불러오기
character = pygame.image.load("C:/Users/user/OneDrive/바탕 화면/python/pygame/character.png")
character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터의 가로 크기
character_height = character_size[1]  #캐리거의 세로크기
character_x_pos = (screen_width / 2) -(character_width/2) #화면 가로의 절반크기에 해당하는 곳에 위치(가로)
character_y_pos = screen_height - character_height #화면세로크기 가장아래에 해당하는 곳에 위치(세로)

#이벤트 루프 (닫히는 창을 유지하기 위해)
running = True #게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가?
        if event.type == pygame.QUIT:#창이 닫히는 이벤트가 발생하였는가?
            running = False  #게임이 진행중이 아님
            
    screen.blit(backgrond, (0,0))#배경그리기
    
    screen.blit(character , (character_x_pos , character_y_pos)) #캐릭터 그리기
    
    pygame.display.update() #게임화면을 다시 그리기

#파이게임 종료            
pygame.quit()
