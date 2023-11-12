import pygame
from math import sqrt

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
GRAY = (108, 110, 110)
WHITE = (150, 183, 190)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FPS = 60
PATH = []
START_COORD = [100, 300]
END_COORD = [500, 150]
P1_COORD = [50, 100]
P2_COORD = [150, 100]
P3_COORD = [250, 100]
P4_COORD = [350, 100]
P5_COORD = [450, 100]
RADIUS = 10
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 18)
pygame.display.set_caption("COURSE WORK")


def dist(xy1, xy2):
    return sqrt(((xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2))


def DrawBezier(x0, y0, x1, y1, x2, y2, x3, y3, x4, y4, x5, y5, x6, y6):
    global PATH
    x = x0
    y = y0
    # Define the step by which the parameter "t" is changed
    ts = 0.001

    # We calculate pixel values while the parameter "t" is greated than 0 and less than 1
    t = 0
    PATH = []
    while t <= 1.0:
        # Calculate Bernstein polynomials for the current pixel with a given parameter "t" value
        # The amount of Bernstein polynomials is always the same as the amount of control points
        B0 = (1 - t) ** 6
        B1 = 6 * (1 - t) ** 5 * t
        B2 = 15 * (1 - t) ** 4 * t ** 2
        B3 = 30 * (1 - t) ** 3 * t ** 3
        B4 = 15 * (1 - t) ** 2 * t ** 4
        B5 = 6 * (1 - t) * t ** 5
        B6 = t ** 6

        # Calculate pixel coordinates by multiplying all the controlpoints with a corresponding Bernstein polynomial
        # and summing it all together
        x = int(x0 * B0 + x1 * B1 + x2 * B2 + x3 * B3 + x4 * B4 + x5 * B5 + x6 * B6)
        y = int(y0 * B0 + y1 * B1 + y2 * B2 + y3 * B3 + y4 * B4 + y5 * B5 + y6 * B6)

        # Change the color of the current calculated pixel
        PATH.append((x, y))
        WIN.set_at((x, y), RED)

        # Increment the parameter "t" value with a predefined step
        t = t + ts
        # Close the drawing method
    return


def draw_window():
    WIN.fill(WHITE)
    for i in range(WIDTH//50):
        pygame.draw.line(WIN,GRAY,(50*i,50),(50*i,500),3)
        if i >0:
            text_surface = my_font.render(str(50*i-50), False, (0, 0, 0))
            WIN.blit(text_surface, (50*i, 10))
    for j in range(HEIGHT//50):
        pygame.draw.line(WIN, GRAY, (50, 50*(j+1)), (900, 50*(j+1)),3)
        if j >0:
            text_surface = my_font.render(str(50*j-50), False, (0, 0, 0))
            WIN.blit(text_surface, (10, 50*j))

    start = pygame.draw.circle(WIN, BLUE, START_COORD, RADIUS)
    end = pygame.draw.circle(WIN, BLUE, END_COORD, RADIUS)
    control_point1 = pygame.draw.circle(WIN, BLUE, P1_COORD, RADIUS)
    control_point2 = pygame.draw.circle(WIN, BLUE, P2_COORD, RADIUS)
    control_point3 = pygame.draw.circle(WIN, BLUE, P3_COORD, RADIUS)
    control_point4 = pygame.draw.circle(WIN, BLUE, P4_COORD, RADIUS)
    control_point5 = pygame.draw.circle(WIN, BLUE, P5_COORD, RADIUS)
    DrawBezier(START_COORD[0], START_COORD[1], P1_COORD[0], P1_COORD[1], P2_COORD[0], P2_COORD[1], P3_COORD[0],
               P3_COORD[1], P4_COORD[0], P4_COORD[1], P5_COORD[0], P5_COORD[1], END_COORD[0],
               END_COORD[1])


def main():
    global P1_COORD, START_COORD, P2_COORD, END_COORD, P5_COORD, P4_COORD, P3_COORD
    run = True
    clock = pygame.time.Clock()
    k = 0
    flag = 0
    incr = 1
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[2]:
                    flag = 0
                if pygame.mouse.get_pressed()[0] and dist(pygame.mouse.get_pos(), P1_COORD) <= RADIUS:
                    P1_COORD = pygame.mouse.get_pos()
                    flag = 3
                if pygame.mouse.get_pressed()[0] and dist(pygame.mouse.get_pos(), P2_COORD) <= RADIUS:
                    P2_COORD = pygame.mouse.get_pos()
                    flag = 4
                if pygame.mouse.get_pressed()[0] and dist(pygame.mouse.get_pos(), P3_COORD) <= RADIUS:
                    P3_COORD = pygame.mouse.get_pos()
                    flag = 5
                if pygame.mouse.get_pressed()[0] and dist(pygame.mouse.get_pos(), P4_COORD) <= RADIUS:
                    P4_COORD = pygame.mouse.get_pos()
                    flag = 6
                if pygame.mouse.get_pressed()[0] and dist(pygame.mouse.get_pos(), P5_COORD) <= RADIUS:
                    P5_COORD = pygame.mouse.get_pos()
                    flag = 7
                if pygame.mouse.get_pressed()[0] and dist(pygame.mouse.get_pos(), START_COORD) <= RADIUS:
                    START_COORD = pygame.mouse.get_pos()
                    flag = 1
                if pygame.mouse.get_pressed()[0] and dist(pygame.mouse.get_pos(), END_COORD) <= RADIUS:
                    END_COORD = pygame.mouse.get_pos()
                    flag = 2

        if k == len(PATH) - 1:
            incr = -1
        elif k==0:
            incr=1


        match flag:
            case 1:
                START_COORD = pygame.mouse.get_pos()
            case 2:
                END_COORD = pygame.mouse.get_pos()
            case 3:
                P1_COORD = pygame.mouse.get_pos()
            case 4:
                P2_COORD = pygame.mouse.get_pos()
            case 5:
                P3_COORD = pygame.mouse.get_pos()
            case 6:
                P4_COORD = pygame.mouse.get_pos()
            case 7:
                P5_COORD = pygame.mouse.get_pos()
        draw_window()
        mv_circle = pygame.draw.circle(WIN, RED, PATH[k - 1], 10)
        k += incr

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
