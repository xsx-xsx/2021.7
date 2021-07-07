import pygame
from pygame.sprite import Group
from pygame.sprite import Sprite
import sys
import PyInstaller


class qiu():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.qiu_x = 300
        self.qiu_y = 300
        self.qiu_banjin = 10
        self.qiu_color = 0, 0, 0


class Fangkuai(Sprite):
    def __init__(self, screen, rect_x, rect_y):
        super(Fangkuai, self).__init__()

        self.bian = 10
        self.rect = pygame.Rect(rect_x, rect_y, self.bian, self.bian)
        self.rect_1 = pygame.Rect(self.rect.x + 1, self.rect.y - 1, self.bian - 2, 1)
        self.rect_2 = pygame.Rect(self.rect.x - 1, self.rect.y - 1, 1, self.bian - 2)
        self.rect_3 = pygame.Rect(self.rect.x + self.bian + 1, self.rect.y + 1, 1, self.bian - 2)
        self.rect_4 = pygame.Rect(self.rect.x + 1, self.rect.y + self.bian + 1, self.bian - 2, 1)

        self.screen = screen
        # self.rect = pygame.Rect(0, 0, 10, 10)
        # self.rect.centerx = 0
        # self.rect.top = 0
        self.y = float(self.rect.y)

        self.color = (100, 200, 200)


    def huizhi(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


def main():
    '''矩形容器在外边定义，图像在循环内绘制'''
    rect = pygame.Rect(290, 590, 100, 20)  # 正方形矩形容器
    circle = pygame.Rect(qiu().qiu_x, qiu().qiu_y, 10, 10)  # 制作小球矩形容器

    rect_color = (200, 200, 200)
    screen = pygame.display.set_mode((600, 600))
    bian = 10
    # fangkuai = pygame.Rect(0, 0, 10, 10)

    rect_x_left = False
    rect_x_right = False
    rect_y_left = False
    rect_y_right = False

    qiu_x = False
    qiu_y = False
    qiu_x_left = False
    qiu_y_right = False

    fangkuais = Group()

    '''产生方块的容器以及sprite'''
    for hangshu in range(10):
        for fk in range(int(600 / (10 + 2))):
            rect_y = hangshu * (10 + 2) * 2
            rect_x = fk * (10 + 2)
            fangkuai = Fangkuai(screen, rect_x, rect_y)  # 需要每次循环创建一个新的sprite
            rongqi = fangkuai

            fangkuais.add(rongqi)




    while 1:
        screen.fill(rect_color)

        pygame.draw.rect(screen, qiu().qiu_color, rect)  # 绘制底盘
        pygame.draw.circle(screen, qiu().qiu_color, (circle.x, circle.y), qiu().qiu_banjin)  # 小球绘制

        '''碰撞时反弹'''
        for zhuan in fangkuais.sprites():
            if zhuan.rect_4.colliderect(circle):
                fangkuais.remove(zhuan)
                qiu_y = False
            elif zhuan.rect_1.colliderect(circle):
                fangkuais.remove(zhuan)
                qiu_y = True
            elif zhuan.rect_2.colliderect(circle):
                fangkuais.remove(zhuan)
                qiu_x = True
            elif zhuan.rect_3.colliderect(circle):
                fangkuais.remove(zhuan)
                qiu_x = False

            zhuan.huizhi()
            # print(len(fangkuais))

        # fangkuais.huizhi()

        if rect.colliderect(circle):
            qiu_y = not qiu_y

        '''小球的移动'''
        if circle.x == 0:
            qiu_x = False
        elif circle.x == screen.get_rect().right:
            qiu_x = True

        if qiu_x and circle.x > 0:
            circle.x -= 1
        elif circle.x < screen.get_rect().right:
            circle.x += 1

        if circle.y == 0:
            qiu_y = False
        elif circle.y == screen.get_rect().height:
            qiu_y = True

        if qiu_y and circle.x > 0:
            circle.y -= 1
        elif circle.x < screen.get_rect().height:
            circle.y += 1

        '''控制矩形左右移动'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RIGHT:
                    rect_x_right = True
                elif event.key == pygame.K_LEFT:
                    rect_x_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    rect_x_right = False
                elif event.key == pygame.K_LEFT:
                    rect_x_left = False
        if rect_x_left and rect.x + rect.width / 2 > 0:
            rect.x -= 1 / 2
        elif rect_x_right and rect.x + rect.width < screen.get_rect().right:
            rect.x += 1

        pygame.display.flip()  # 刷新


def pmsx():
    pygame.display.flip()


main()