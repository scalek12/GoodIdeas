hummingbird.startHummingbird()
music.playTone(175, music.beat(BeatFraction.Whole))
basic.forever(function () {
    basic.showString("" + (hummingbird.getSensor(SensorType.Distance, ThreePort.Two)))
    while (hummingbird.getSensor(SensorType.Distance, ThreePort.Two) <= 75) {
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.giggle), SoundExpressionPlayMode.InBackground)
    }
    if (hummingbird.getSensor(SensorType.Distance, ThreePort.Two) > 75) {
        music.stopAllSounds()
    }
})
