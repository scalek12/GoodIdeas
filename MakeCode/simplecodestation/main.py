showPic = 0

def on_button_pressed_a():
    global showPic
    showPic = randint(1, 5)
    if showPic == 1:
        basic.show_icon(IconNames.HAPPY)
    elif showPic == 2:
        music.play_tone(262, music.beat(BeatFraction.BREVE))
    elif showPic == 3:
        basic.show_icon(IconNames.STICK_FIGURE)
    elif showPic == 4:
        basic.show_icon(IconNames.TARGET)
    elif showPic == 5:
        music.play_melody("E B C5 A B G A F ", 500)
    basic.pause(1000)
    basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)
