// credits
input.onButtonPressed(Button.AB, function () {
    basic.showString("code written by jovan see :)")
})
// boot icon
basic.showIcon(IconNames.Happy)
// reads the value from the moisture sensor (analog pin 1) and assigns it to the moisture_sensor_reading
let moisture_sensor_reading = pins.analogReadPin(AnalogPin.P1)
// forever loop
basic.forever(function () {
    // rereads the value from the moisture sensor (analog pin 1) and reassigns it to the moisture_sensor_reading
    moisture_sensor_reading = pins.analogReadPin(AnalogPin.P1)
    // compares the reading to a fixed value for moisture (511)
    if (moisture_sensor_reading == 511) {
        // turns on led (digital pin 0) by setting its value to 1
        pins.digitalWritePin(DigitalPin.P0, 1)
    } else {
        // waits awhile (3 secs) before repeating the loop
        basic.pause(3000)
    }
})
