basic.showLeds(`
    # . . . .
    . # . . .
    . . # . .
    . . . # .
    . . . . #
    `)
basic.forever(function () {
    while (input.buttonIsPressed(Button.A)) {
        pins.digitalWritePin(DigitalPin.P2, 1)
    }
    pins.digitalWritePin(DigitalPin.P2, 0)
})
