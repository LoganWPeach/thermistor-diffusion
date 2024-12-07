import time
from machine import Pin, Timer, ADC
import math

heater = Pin(2, Pin.OUT)

adc_1=ADC(Pin(36))
adc_1.atten(ADC.ATTN_11DB)
adc_1.width(ADC.WIDTH_12BIT)

adc_2=ADC(Pin(35))
adc_2.atten(ADC.ATTN_11DB)
adc_2.width(ADC.WIDTH_12BIT)

filename = "final_experiment.txt"



A = 3303.902
B = -3.729009
time_elapsed = 0
resistance_values_1 = []
temps_1 = []
resistance_values_2 = []
temps_2 = []
i_values = []
end_temperature = "blank"

answer = math.log(math.e)
print("answer = " + str(answer))

def funnyfunction(iterations):
    for i in range (iterations):
        global time_elapsed
        
        adcVal_1 = adc_1.read()
        voltage_1 = round(adcVal_1 / 4095.0 * 3.3 , 6)
        therm_val_1 = 1000/((3.3/voltage_1)-1)
        temp_1 = A/(math.log(therm_val_1)-B)
        print("\n" + str(time_elapsed) + " i-value\n" + str(therm_val_1) + " Ohms " + str(voltage_1) + " V " + str(adcVal_1) + " adc input " + str(temp_1) + " temperature")
        resistance_values_1.append(therm_val_1)
        temps_1.append(temp_1)
    
        adcVal_2 = adc_2.read()
        voltage_2 = round(adcVal_2 / 4095.0 * 3.3 , 6)
        therm_val_2 = 1000/((3.3/voltage_2)-1)
        temp_2 = A/(math.log(therm_val_2)-B)
        print(str(therm_val_2) + " Ohms " + str(voltage_2) + " V " + str(adcVal_2) + " adc input " + str(temp_2) + " temperature")
        resistance_values_2.append(therm_val_2)
        temps_2.append(temp_2)
        
        
        time_elapsed += 1
        i_values.append(time_elapsed)
        
        time.sleep(1)

heater.value(1)
funnyfunction(5)

print("\nHEATER ON!!")

heater.value(0)
funnyfunction(2)
heater.value(1)
    
print("\nHEATER OFF!!")
    
funnyfunction(241)
    
with open (filename, 'a') as file_object:
    file_object.write("\n thermistor 1 temperature values \n" + str(temps_1) + "\n thermistor 2 temperature values \n" + str(temps_2) + "\n time (seconds)\n " + str(i_values))
