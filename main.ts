/** 
Title: Can't Stop Game Jam
Creator: Adam L
Description: A game for the game jam about jumping between pillars

 */
//  Begin adding your game below.
// Scene
game.splash("Press A to jump")
scene.setBackgroundColor(128)
// Creating Character
let man = sprites.create(img`
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
`)
man.x = 35
man.y = 120
man.ay = 150
man.setFlag(SpriteFlag.StayInScreen, true)
// Creating Obsticles
let spike = sprites.create(img`
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
`)
let big_spike = sprites.create(img`
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
`)
let spike_ball = sprites.create(img`
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
`)
// Controls
controller.A.onEvent(ControllerButtonEvent.Pressed, function on_jump() {
    man.vy = -100
})
// Scoring and lives
info.setLife(3)
info.setScore(0)
