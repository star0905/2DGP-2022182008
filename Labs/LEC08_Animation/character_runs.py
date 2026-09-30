from pico2d import *

open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('hero_sheet.png')
# fill here
frame = 0

# 프레임마다 크기가 달라서, 프레임 좌표/크기는 JSON 에서 불러옴
with open('hero_sheet.json', 'r', encoding='utf-8') as f:
    sheet_info = json.load(f)

def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            close_canvas()
            raise SystemExit

# 재생할 애니메이션 순서
animations = ['idle', 'walk', 'run', 'jump', 'attack']

# 애니메이션 순서를 계속 반복
while True:
    for name in animations:
        frames = sheet_info['animations'][name]['frames']
        # 각 애니메이션을 5번 반복
        for repeat in range(5):
            # 현재 애니메이션의 프레임 수만큼 재생 (애니메이션마다 프레임 수가 다름)
            for frame in frames:
                handle_events()
                clear_canvas()
                grass.draw(400, 30)
                character.clip_draw(
                left, bottom,
                width, height,
                x, y
            ) 
            update_canvas()
            frame = (frame + 1) % 8

    handle_events()

    delay(0.05)
    
close_canvas()
