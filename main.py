# credits

def on_button_pressed_ab():
    basic.show_string("code written by jovan see :)")
input.on_button_pressed(Button.AB, on_button_pressed_ab)

# boot icon
basic.show_icon(IconNames.HAPPY)
# reads the value from the moisture sensor (analog pin 1) and assigns it to the moisture_sensor_reading
moisture_sensor_reading = pins.analog_read_pin(AnalogPin.P1)
# forever loop

def on_forever():
    global moisture_sensor_reading
    # rereads the value from the moisture sensor (analog pin 1) and reassigns it to the moisture_sensor_reading
    moisture_sensor_reading = pins.analog_read_pin(AnalogPin.P1)
    # compares the reading to a fixed value for moisture (511)
    if moisture_sensor_reading == 511:
        # turns on led (digital pin 0) by setting its value to 1
        pins.digital_write_pin(DigitalPin.P0, 1)
    else:
        # waits awhile (2 secs) before repeating the loop
        basic.pause(2000)
basic.forever(on_forever)