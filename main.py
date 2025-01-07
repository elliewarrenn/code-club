def on_button_pressed_a():
    basic.show_leds("""
        . # # # .
        # . # . #
        # # # # #
        # . # . #
        . # # # .
        """)
    music.play(music.string_playable("- - F D D - C5 A ", 120),
        music.PlaybackMode.UNTIL_DONE)
input.on_button_pressed(Button.A, on_button_pressed_a)

basic.clear_screen()

def on_forever():
    pass
basic.forever(on_forever)
