from pico2d import *

open_canvas(800, 600)

grass = load_image('grass.png')
character = load_image('hero_sheet.png')
# fill here
frame = 0

def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT or (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
            close_canvas()
            raise SystemExit

# 현재 애니메이션의 프레임 수만큼 재생 (애니메이션마다 프레임 수가 다름)
for frame in frames:
    for x in range(0, 800, 5):
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
