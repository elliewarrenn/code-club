input.onButtonPressed(Button.A, function () {
    basic.showLeds(`
        . # # # .
        # . # . #
        # # # # #
        # . # . #
        . # # # .
        `)
    music.play(music.stringPlayable("- - F D D - C5 A ", 120), music.PlaybackMode.UntilDone)
})
basic.clearScreen()
basic.forever(function () {
	
})
