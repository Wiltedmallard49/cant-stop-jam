"""
Title: Can't Stop Game Jam
Creator: Adam L
Description: A game for the game jam about jumping between pillars
"""
# Begin adding your game below.
#Scene
game.splash("Press A to jump")
scene.set_background_color(128)
#Creating Character
man = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . 2 2 2 2 . . . . . .
    . . . . . . 2 2 2 2 . . . . . .
    . . . . . . 2 2 2 2 . . . . . .
    . . . . . . 2 2 2 2 . . . . . .
    . . . . . . 2 2 2 2 . . . . . .
    . . . . . . 2 2 2 2 . . . . . .
    . . . . . . 2 2 2 2 . . . . . .
    . . . . . . 2 2 2 2 . . . . . .
"""))
man.x = 35
man.y = 120
man.ay = 150
man.set_flag(SpriteFlag.StayInScreen, True)
#Creating Obsticles
spike = sprites.create(img("""
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . b b . . . . . . .
    . . . . . . b b b b . . . . . .
    . . . . . b b b b b b . . . . .
    . . . . b b b b b b b b . . . .
    . . . b b b b b b b b b b . . .
    . . b b b b b b b b b b b b . .
    . b b b b b b b b b b b b b b .
    b b b b b b b b b b b b b b b b
"""))
big_spike = sprites.create(img("""
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
    ..........bbbbbbbbb...........
"""))
spike_ball = sprites.create(img("""
    . . . . . . . b b b . . . . . .
    . . . . . . . b . b . . . . . .
    . . . . . . . b b b . . . . . .
    . . . . . . . . b . . . . . . .
    . . . . . . . b b b . . . . . .
    . . . . . . . b . b . . . . . .
    . . . . . . . b b b . . . . . .
    . . . . . . . c b c . . . . . .
    . . . . . . c c c c c . . . . .
    . . . . . c c c c c c c . . . .
    . . . . . . c c c c c . . . . .
    . . . . . c c c c c c c . . . .
    . . . . . . c c c c c . . . . .
    . . . . . . c . c . c . . . . .
    . . . . . . . . . . . . . . . .
    . . . . . . . . . . . . . . . .
"""))

#Controls
def on_jump():
    man.vy = -100
controller.A.on_event(ControllerButtonEvent.PRESSED, on_jump)
#Scoring and lives
info.set_life(3)
info.set_score(0)

