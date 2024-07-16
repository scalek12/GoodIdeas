basic.show_leds("""
    # . . . .
    . # . . .
    . . # . .
    . . . # .
    . . . . #
    """)

def on_forever():
    while input.button_is_pressed(Button.A):
        pins.digital_write_pin(DigitalPin.P16, 1)
    pins.digital_write_pin(DigitalPin.P16, 0)
basic.forever(on_forever)
