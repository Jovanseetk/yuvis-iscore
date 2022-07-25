# boot icon
basic.show_icon(IconNames.HAPPY)
# reads the value from the moisture sensor (analog pin 1) and assigns it to the moisture_sensor_reading
moisture_sensor_reading = pins.analog_read_pin(AnalogPin.P1)
# sets mode value to 0 (default mode)
mode = 0
# clears led screen
basic.clear_screen()
# controls

def on_forever():
    global mode
    # credits
    if input.button_is_pressed(Button.A):
        basic.show_string("code written by jovan see :)")
    if input.button_is_pressed(Button.AB):
        # sets mode value to 1 (debug mode)
        mode = 1
basic.forever(on_forever)

# forever loop

def on_forever2():
    global moisture_sensor_reading, mode
    # forever loop for default mode
    # checks for default mode value
    while mode == 0:
        # rereads the value from the moisture sensor (analog pin 1) and reassigns it to the moisture_sensor_reading
        moisture_sensor_reading = pins.analog_read_pin(AnalogPin.P1)
        # compares the reading to a fixed value for moisture (511)
        if moisture_sensor_reading == 511:
            # turns on led (digital pin 0) by setting its value to 1
            pins.digital_write_pin(DigitalPin.P0, 1)
        else:
            # waits awhile (3 secs) before repeating the loop
            basic.pause(3000)
    # checks for debug mode value (1)
    if mode == 1:
        # displays debug mode intro
        basic.show_string("DEBUG MODE ENABLED")
        # displays moisture sensor reading
        basic.show_string("the moisture sensor reading is: " + str(pins.analog_read_pin(AnalogPin.P0)))
        # turns led (digital pin 0) off
        pins.digital_write_pin(DigitalPin.P0, 0)
        # shows led off message
        basic.show_string("the led is currently set to OFF")
        # turns led (digital pin 0) on
        pins.digital_write_pin(DigitalPin.P0, 1)
        # shows led on message
        basic.show_string("the led is currently set to ON")
        # waits awhile (3 secs) before repeating the loop
        basic.pause(3000)
        # sets mode value to 0 (default mode)
        mode = 0
basic.forever(on_forever2)
