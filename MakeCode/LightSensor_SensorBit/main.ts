music.playTone(262, music.beat(BeatFraction.Whole))
OLED.init(64, 128)
basic.forever(function () {
    OLED.clear()
    OLED.newLine()
    OLED.writeString("light: ")
    OLED.writeNum(Environment.ReadLightIntensity(AnalogPin.P1))
})
