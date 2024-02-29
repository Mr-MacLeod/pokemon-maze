scene.onOverlapTile(SpriteKind.Player, assets.tile`
        myTile0
    `, function on_overlap_tile(sprite: Sprite, location: tiles.Location) {
    game.over(true)
})
info.onCountdownEnd(function on_countdown_end() {
    music.play(music.melodyPlayable(music.wawawawaa), music.PlaybackMode.InBackground)
    game.gameOver(false)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function on_on_overlap(sprite2: Sprite, otherSprite: Sprite) {
    info.changeCountdownBy(5)
    PowerUp.startEffect(effects.spray)
    sprites.destroy(PowerUp)
})
let PowerUp : Sprite = null
game.splash("Find the water!")
let mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
controller.moveSprite(mySprite, 100, 100)
PowerUp = sprites.create(assets.image`
    PowerUp
`, SpriteKind.Food)
tiles.setTilemap(tilemap`
    level1
`)
tiles.placeOnRandomTile(mySprite, sprites.dungeon.stairLadder)
tiles.placeOnTile(PowerUp, tiles.getTileLocation(4, 3))
scene.cameraFollowSprite(mySprite)
info.startCountdown(8)
forever(function on_forever() {
    music.play(music.stringPlayable("G B A G C5 B A B ", 80), music.PlaybackMode.UntilDone)
})
