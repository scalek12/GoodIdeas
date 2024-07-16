let showPic = 0
input.onButtonPressed(Button.A, function () {
    showPic = randint(1, 3)
    if (showPic == 1) {
        basic.showIcon(IconNames.Happy)
    } else if (showPic == 2) {
        music.playMelody("E B C5 A B G A F ", 500)
    } else if (showPic == 3) {
        basic.showIcon(IconNames.StickFigure)
    }
    basic.pause(1000)
    basic.clearScreen()
})
