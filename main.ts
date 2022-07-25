//  boot icon
basic.showIcon(IconNames.Happy)
//  reads the value from the moisture sensor (analog pin 1) and assigns it to the moisture_sensor_reading
let moisture_sensor_reading = pins.analogReadPin(AnalogPin.P1)
//  clears led screen
basic.clearScreen()
//  sets mode value to 0 (default mode)
let mode = 0
//  controls
basic.forever(function on_forever() {
    
    //  credits
    if (input.buttonIsPressed(Button.A)) {
        basic.showString("code written by jovan see :)")
    }
    
    if (input.buttonIsPressed(Button.AB)) {
        //  sets mode value to 1 (debug mode)
        mode = 1
    }
    
})
//  forever loop
basic.forever(function on_forever2() {
    
    //  forever loop for default mode
    //  checks for default mode value
    while (mode == 0) {
        //  rereads the value from the moisture sensor (analog pin 1) and reassigns it to the moisture_sensor_reading
        moisture_sensor_reading = pins.analogReadPin(AnalogPin.P1)
        //  compares the reading to a fixed value for moisture (511)
        if (moisture_sensor_reading == 511) {
            //  turns on led (digital pin 0) by setting its value to 1
            pins.digitalWritePin(DigitalPin.P0, 1)
        } else {
            //  waits awhile (3 secs) before repeating the loop
            basic.pause(3000)
        }
        
    }
    //  checks for debug mode value (1)
    if (mode == 1) {
        //  displays debug mode intro
        basic.showString("DEBUG MODE ENABLED")
        //  displays moisture sensor reading
        basic.showString("the moisture sensor reading is: " + ("" + ("" + pins.analogReadPin(AnalogPin.P0))))
        //  turns led (digital pin 0) off
        pins.digitalWritePin(DigitalPin.P0, 0)
        //  shows led off message
        basic.showString("the led is currently set to OFF")
        //  turns led (digital pin 0) on
        pins.digitalWritePin(DigitalPin.P0, 1)
        //  shows led on message
        basic.showString("the led is currently set to ON")
        //  waits awhile (3 secs) before repeating the loop
        basic.pause(3000)
        //  sets mode value to 0 (default mode)
        mode = 0
    }
    
})
