pins.touchSetMode(TouchTarget.LOGO, TouchTargetMode.Capacitive)
basic.forever(function () {
    while (input.logoIsPressed()) {
        basic.showIcon(IconNames.Heart)
        music.playTone(175, music.beat(BeatFraction.Whole))
    }
    basic.clearScreen()
})
