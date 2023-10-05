import random

from pico2d import *


# Game object class here
class Grass:  # 클래스 이름은 대문자로 시작하는 명사
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)


class Ball:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.speed = random.randint(1, 10)
        self.size = random.randint(0, 1)

        if (self.size == 1):
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

    def update(self):
        if (self.size == 1):
            if (self.y >= 30 + 31):
                self.y -= self.speed
            if (self.y < 30 + 31):
                self.y = 30 + 31
        else:
            if (self.y >= 30 + 41):
                self.y -= self.speed
            if (self.y < 30 + 41):
                self.y = 30 + 41

    def draw(self):
        self.image.draw(self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global world
    global ball
    running = True
    world = []

    grass = Grass()  # 클래스를 이용해 객체를 찍어냄
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    ball = [Ball() for i in range(20)]
    world += ball


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


def update_world():
    for o in world:
        o.update()


open_canvas()

# initialization code
reset_world()

# game main loop code
while (running):
    handle_events()
    update_world()  # 객체의 상호작용 업데이트
    render_world()
    delay(0.05)

# finalization code

close_canvas()
