import pygame
from random import randrange, randint
from time import sleep
from pygame.locals import *


class Bird:
    def __init__(self, height, posh, speed = -7):
        self.speed = speed
        self.height = height
        self.posh = posh
        self.posfin = None

    def print_bird(self):
        pygame.draw.rect(screen, yellow, [self.posh+5, self.height-1, 10, 22])
        pygame.draw.rect(screen, yellow, [self.posh, self.height, 2*pix, 2*pix])
        pygame.draw.rect(screen, black, [self.posh+14, self.height+3, 3, 3])
        pygame.draw.rect(screen, red, [self.posh+17, self.height+9, 8, 4])
        pygame.draw.rect(screen, yellow, [self.posh-3, self.height+12, 3, 5])
        pygame.draw.rect(screen, yellow, [self.posh-1, self.height+8, 1, 10])
        self.posfin = pygame.draw.rect(screen, yellow, [self.posh+5, self.height-1, 10, 22])

    def print_wing(self):
        pygame.draw.rect(screen, whitew, [self.posh+5, self.height+9, 6, 3])
        if self.speed < -6:
            pass
        elif self.speed <= 0:
            pygame.draw.rect(screen, whitew, [self.posh+5, self.height+12, 5, 3])
            pygame.draw.rect(screen, whitew, [self.posh+4, self.height+15, 4, 1])
        elif self.speed > 0:
            pygame.draw.rect(screen, whitew, [self.posh+5, self.height+6, 5, 3])
            pygame.draw.rect(screen, whitew, [self.posh+4, self.height+5, 4, 1])

    def chang_speed(self):
        self.speed = -10

    def att_altura(self):
        self.height += self.speed

    def att_velocidade(self):
        self.speed += 1
    
    def restart(self, height, posh, speed = -7):
        self.speed = speed
        self.height = height
        self.posh = posh
        self.posfin = None


class Cloud:
    def __init__(self, height_cloud = randint(0, int(400/3*2)), pos_cloud = 600+30):
        self.height_cloud = height_cloud
        self.pos_cloud = pos_cloud
        self.num = randint(0, 2)

    def print_cloud(self):
        if self.num == 0:
            pygame.draw.rect(screen, white, [self.pos_cloud,self.height_cloud, 50, 30])
            pygame.draw.rect(screen, white, [self.pos_cloud+20,self.height_cloud-15, 70, 25])
            pygame.draw.rect(screen, white, [self.pos_cloud+50,self.height_cloud+5, 50, 20])
            pygame.draw.rect(screen, white, [self.pos_cloud-5,self.height_cloud+5, 5, 20])
            pygame.draw.rect(screen, white, [self.pos_cloud+5,self.height_cloud-10, 15, 10])
            pygame.draw.rect(screen, white, [self.pos_cloud+25,self.height_cloud-19, 55, 4])
        if self.num == 1:
            pygame.draw.rect(screen, white, [self.pos_cloud, self.height_cloud, 20, 20])
            pygame.draw.rect(screen, white, [self.pos_cloud+10, self.height_cloud+5, 30, 25])
            pygame.draw.rect(screen, white, [self.pos_cloud+30, self.height_cloud+5, 20, 20])
            pygame.draw.rect(screen, white, [self.pos_cloud+40, self.height_cloud+7, 40, 28])
            pygame.draw.rect(screen, white, [self.pos_cloud+60, self.height_cloud+3, 30, 25])
        if self.num == 2:
            pygame.draw.rect(screen, white, [self.pos_cloud, self.height_cloud, 70, 50])
            pygame.draw.rect(screen, white, [self.pos_cloud+5, self.height_cloud-5, 40, 5])
            pygame.draw.rect(screen, white, [self.pos_cloud-5, self.height_cloud+5, 5, 40])
            pygame.draw.rect(screen, white, [self.pos_cloud+55, self.height_cloud-5, 20, 45])
            pygame.draw.rect(screen, white, [self.pos_cloud+75, self.height_cloud, 5, 35])
            pygame.draw.rect(screen, white, [self.pos_cloud+10, self.height_cloud+50, 50, 5])
    
    def att_cloud(self):
        self.pos_cloud -= 2

    def cloud_reset(self):
        self.height_cloud = randint(0, int(400/4*3))
        self.pos_cloud = 600+30
        self.num = randint(0, 2)


def text(text, color, size, width, height):
    font = pygame.font.SysFont(None, size)
    text1 = font.render(text, True, color)
    screen.blit(text1, (int(width), int(height)))


def play(point_pass, point, time):
    quit_game = False
    dif = 0
    spaces = 0
    while quit_game != True:
        timer.tick(fps)
        screen.fill(blue)
        bird.att_velocidade()
        if len(clouds)<3 and (randint(0,100) == 1):
            clouds.append(Cloud())
            clouds[-1].height_cloud = randint(0, 300)
        try:
            for i in range(-1, len(clouds)-1):
                clouds[i].print_cloud()
                clouds[i].att_cloud()
            if clouds[i].pos_cloud < -100:
                del clouds[i]
        except:
            clouds.append(Cloud())
        bird.print_bird()
        bird.print_wing()

        try:
            dif += 7
            ret1 = [WIDTH-pix-dif, 0, int(4*pix), spaces]
            barriers[0][0] = ret1
            ret2 = [WIDTH-pix-dif, spaces+8*pix, int(4*pix), height-pix]
            barriers[0][1] = ret2
        except:
            pass 

        if int(time - 2.8) % 4 == 0:
            point_pass+=1/fps
        if int(time) % 4 == 0:
            dif = 0
            spaces = randrange(pix, height-10*pix, 5)
            ret1 = [WIDTH, 0, int(4*pix), spaces]
            ret2 = [WIDTH, spaces+8*pix, int(4*pix), height-pix]
            barriers[0] = ([ret1, ret2])

        try:
            pygame.draw.rect(screen, brown, barriers[0][0])
            pygame.draw.rect(screen, brown, barriers[0][1])
        except:
            pass

        pygame.draw.rect(screen, green, [0, height-10, WIDTH, 10])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game = True
                if event.key == pygame.K_SPACE:
                    bird.chang_speed()
                if event.key == pygame.K_UP:
                    bird.chang_speed()
        
        if bird.posfin.colliderect(ret1) or bird.posfin.colliderect(ret2) or bird.height<0 or bird.height>height-20:
            quit_game = True
            screen.fill(brown)
            pygame.draw.rect(screen, yellow, (int((WIDTH/2-7*7)), int((height/2-15)), 7*14, 35))
            text('Lose!', red, 50, WIDTH/2-7*7, height/2-15)
            pygame.display.update()
            try:
                sound_dead.play()
            except:
                pass
            sleep(1)
            continue
        bird.att_altura()
        time += 1/fps
        if point_pass > 0 and int(point_pass) != point:
            try:
                sound_point.play()
            except:
                pass
            point = int(point_pass)
        text(f'{point}', black, 50, WIDTH-60, 20)
        pygame.display.update()
    return point


def menu(time):
    sair2 = False
    while sair2 != True:
        timer.tick(fps)
        interface_menu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair2 = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sair2 = True
                if event.key == pygame.K_q:
                    sair2 = True
                if event.key == pygame.K_SPACE:
                    point = play(-1, 0, time)
                    bird.restart(int(height/4), 50)
                    bird.print_bird()
                    time = 0
                    barriers[0] = None
                    print(f'pontuação:{point}')
        pygame.display.update()


def interface_menu():
    screen.fill(blue)
    if len(clouds)<3 and (randint(0,100) == 1):
        clouds.append(Cloud())
        clouds[-1].height_cloud = randint(0, 300)
    try:
        for i in range(-1, len(clouds)-1):
            clouds[i].print_cloud()
            clouds[i].att_cloud()
        if clouds[i].pos_cloud < -100:
            del clouds[i]
    except:
        clouds.append(Cloud())
    bird.print_bird()
    bird.print_wing()
    pygame.draw.rect(screen, green, [0, height-10, WIDTH, 10])
    text('press space to play', black, 50, WIDTH/2-7*20, height/2-50)
    text('or', black, 50, WIDTH/2-7*20, height/2-15)
    text('"q" to quit', black, 50, WIDTH/2-7*20, height/2+20)


pygame.init()
pygame.font.init()
pygame.mixer.init()

WIDTH = 600
height = 400
pix = 10
brown = (120, 60, 10, 255)
blue = (130, 130, 255, 255)
yellow = (255, 255, 10, 255)
black = (0, 0, 0, 255)
white = (255, 255, 255, 255)
red = (200, 0, 0, 255)
green = (0, 200, 0, 255)
whitew = (170, 170, 60, 255)
screen = pygame.display.set_mode((WIDTH, height))
pygame.display.set_caption('Flappy Bird')
try:
    sound_point = pygame.mixer.Sound('point.wav')
except:
    pass
try:
    sound_dead = pygame.mixer.Sound('mgs.wav')
except:
    pass
timer = pygame.time.Clock()
fps = 30
time = 0
dif = 0

bird = Bird(int(height/4), 50)
bird.print_bird()
barriers = []
barriers.append([])
spaces = 0
clouds = []
clouds.append(Cloud())

menu(time)

pygame.mixer.quit()
pygame.font.quit()
pygame.quit()
