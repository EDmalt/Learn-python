# By hefei
"""
@File : main_scene.py
"""
import sys
import pygame
import all_class


# from all_class import Scene #当然all_class文件的Scene类

def run_game():
    s = all_class.Scene()  # 创建Scene对象
    # 初始化游戏窗口
    pygame.init()
    # 使用pygame.display渲染窗口，其中set_mode(size=(),flags=0)
    scene = pygame.display.set_mode((s.get_width(), s.get_height()))  # 设置窗口大小
    pygame.display.set_caption("game1")
    scene.fill(s.get_color())  # 绘制背景颜色
    player = all_class.Snake(scene)  # 创建Snake对象
    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        player.blitme()
        pygame.display.flip()  # 让最近绘制的屏幕可见


if __name__ == '__main__':
    run_game()
