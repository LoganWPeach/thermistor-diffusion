# thermistor-diffusion
Code for an ESP32; Manages a heater and monitors the temperature of two thermistors over time.

Various parameters to edit if using this:

"heater" should be changed to be whatever pin is being used to heat your apparatus. 

Likewise, adc_1 and adc_2 should be changed to whichever pins connect to the thermistors in question. 

The end section of code runs a few trials; "Runtrial" will gather data for an amount of seconds equivalent to the inputted value.
The default setting is leaving the heater off for 5 seconds, turning the heater on for 2 seconds, then turning it off and gathering data for 240 seconds.

The gathered data is saved into a text file by the name of "final_experiment.txt". Text is not overwritten from experiment to experiment, and text is only saved if the code runs in full.
