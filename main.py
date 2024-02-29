def on_overlap_tile(sprite, location):
    game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile0
    """),
    on_overlap_tile)

def on_countdown_end():
    music.play(music.melody_playable(music.wawawawaa),
        music.PlaybackMode.IN_BACKGROUND)
    game.game_over(False)
info.on_countdown_end(on_countdown_end)

def on_on_overlap(sprite2, otherSprite):
    info.change_countdown_by(5)
    PowerUp.start_effect(effects.spray)
    sprites.destroy(PowerUp)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

PowerUp: Sprite = None
game.splash("Find the water!")
mySprite = sprites.create(img("""
        . . . . f f f f . . . . . 
            . . f f c c c c f f . . . 
            . f f c c c c c c f f . . 
            f f c c c c c c c c f f . 
            f f c c f c c c c c c f . 
            f f f f f c c c f c c f . 
            f f f f c c c f c c f f . 
            f f f f f f f f f f f f . 
            f f f f f f f f f f f f . 
            . f f f f f f f f f f . . 
            . f f f f f f f f f f . . 
            f e f f f f f f f f e f . 
            e 4 f 7 7 7 7 7 7 c 4 e . 
            e e f 6 6 6 6 6 6 f e e . 
            . . . f f f f f f . . . . 
            . . . f f . . f f . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
PowerUp = sprites.create(assets.image("""
    PowerUp
"""), SpriteKind.food)
tiles.set_tilemap(tilemap("""
    level1
"""))
tiles.place_on_random_tile(mySprite, sprites.dungeon.stair_ladder)
tiles.place_on_tile(PowerUp, tiles.get_tile_location(4, 3))
scene.camera_follow_sprite(mySprite)
info.start_countdown(8)

def on_forever():
    music.play(music.string_playable("G B A G C5 B A B ", 80),
        music.PlaybackMode.UNTIL_DONE)
forever(on_forever)

