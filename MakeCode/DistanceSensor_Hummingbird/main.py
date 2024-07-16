music.play_tone(175, music.beat(BeatFraction.WHOLE))

def on_forever():
    if hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.TWO) > 100 and hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.TWO) < 200:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.yawn),
            SoundExpressionPlayMode.UNTIL_DONE)
    elif hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.TWO) > 200 and hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.TWO) < 300:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.mysterious),
            SoundExpressionPlayMode.UNTIL_DONE)
    elif hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.TWO) > 300 and hummingbird.get_sensor(SensorType.DISTANCE, ThreePort.TWO) < 400:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.soaring),
            SoundExpressionPlayMode.UNTIL_DONE)
    else:
        music.stop_all_sounds()
basic.forever(on_forever)
