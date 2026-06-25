import pygame
import time
import traceback

# ==================== 配置 ====================
WIDTH, HEIGHT = 1920, 1080
SCALE = 4.0 / 540.0
IMAGE_PATH = "/home/jzwalliser/桌面/temporary/Unpublished/arduino2/media/images/main/LED_ManimCE_v0.19.1.png"
FPS = 60
RELOAD_INTERVAL = 1.0  # 秒

# ==================== 工具函数 ====================
def screen_to_custom(x, y):
    cx = (x - WIDTH // 2) * SCALE
    cy = (HEIGHT // 2 - y) * SCALE
    return round(cx, 2), round(cy, 2)

# ==================== 初始化 pygame ====================
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Image Viewer")
pygame.mouse.set_visible(False)

font = pygame.font.SysFont(None, 36)

# ==================== 状态变量 ====================
image = None
last_reload_time = 0

mouse_x = mouse_y = 0

dragging = False
drag_start = None      # (screen_x, screen_y)
drag_end = None        # (screen_x, screen_y)

clock = pygame.time.Clock()

# ==================== 主循环 ====================
running = True
while running:
    clock.tick(FPS)
    now = time.time()

    # ---------- 事件处理 ----------
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEMOTION:
            mouse_x, mouse_y = event.pos

            if dragging:
                drag_end = event.pos

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                dragging = True
                drag_start = event.pos
                drag_end = event.pos

        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                dragging = False
                drag_end = event.pos

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # 打印所有自定义坐标
                cur = screen_to_custom(mouse_x, mouse_y)
                print("==== ENTER ====")
                print(f"鼠标自定义坐标: {cur}")

                if drag_start and drag_end:
                    sx, sy = screen_to_custom(*drag_start)
                    ex, ey = screen_to_custom(*drag_end)
                    dx = round(ex - sx, 2)
                    dy = round(ey - sy, 2)
                    mx = round((sx + ex) / 2, 2)
                    my = round((sy + ey) / 2, 2)
                    print(f"拖拽起点: ({sx}, {sy})")
                    print(f"拖拽终点: ({ex}, {ey})")
                    print(f"自定义偏移量: dx={dx}, dy={dy}")
                    print(f"自定义中点: ({mx}, {my})")

    # ---------- 定时重新加载图片 ----------
    if now - last_reload_time > RELOAD_INTERVAL:
        last_reload_time = now
        try:
            img = pygame.image.load(IMAGE_PATH).convert()
            if img.get_size() == (WIDTH, HEIGHT):
                image = img
        except Exception as exc:
            pass  # 图片正在写入中，跳过本次

    # ---------- 绘制 ----------
    screen.fill((0, 0, 0))

    if image:
        screen.blit(image, (0, 0))

    # 鼠标小圆点
    pygame.draw.circle(screen, (255, 0, 0), (mouse_x, mouse_y), 4)

    # 左上角：鼠标自定义坐标
    cx, cy = screen_to_custom(mouse_x, mouse_y)
    text1 = font.render(f"Cursor: ({cx}, {cy})", True, (255, 255, 0))
    screen.blit(text1, (10, 10))

    # 左下角：拖拽信息
    if drag_start and drag_end:
        sx, sy = screen_to_custom(*drag_start)
        ex, ey = screen_to_custom(*drag_end)
        dx = round(ex - sx, 2)
        dy = round(ey - sy, 2)
        mx = round((sx + ex) / 2, 2)
        my = round((sy + ey) / 2, 2)

        info = [
            f"Drag start : ({sx}, {sy})",
            f"Drag end   : ({ex}, {ey})",
            f"Offset     : dx={dx}, dy={dy}",
            f"Mid point  : ({mx}, {my})"
        ]

        for i, line in enumerate(info):
            txt = font.render(line, True, (0, 255, 0))
            screen.blit(txt, (10, HEIGHT - 160 + i * 32))

    pygame.display.flip()

pygame.quit()
