# By hefei
"""
@File : all_class.py
"""
import pygame


# 用于存放所有游戏相关类

class Scene:
    # 游戏场景基本设置类
    def __init__(self):
        self.__width = 1280
        self.__height = 720
        self.__bgcolor = (230, 220, 210)

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_color(self):
        return self.__bgcolor


class Snake:
    def __init__(self, screen):
        self.screen = screen
        self.snake = pygame.image.load(r"C:\Users\Hasee\OneDrive\图片\1626323897044.jpg")  # 设置玩家的外形



    def blitme(self):
        # 在指定位置绘画玩家
        # 关键语句xxx.blit(绘画对象,窗口坐标,Rect对象,special_flags)
        self.screen.blit(self.snake,(200,200),)
