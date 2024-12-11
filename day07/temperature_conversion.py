'''
Day 7 - Temparature Conversion
1. Write a program to convert temperature from Celsius to Fahrenheit. 
2. Write a program to convert temperature from Fahrenheit to Celsius 

USER: It's asking to write a program, but these could easily be different functions. I'm gonna make 2 different functions instead.
'''
print("Temperature conversion...")
select = None

while(select != 'c') & (select != 'f'):
    select = input("Would you like to convert the temperature from (C)elsius to Fahrenheit, or (F)ahrenheit to Celsius? (c/f) ")

temp = int(input("Input temperature: "))

def celsiusToFahrenheit(cel):
    convertedTemp = (cel * (9/5)) + 32
    print("{cTemp}°C to Fahrenheit = {fTemp:.1f}°F".format(
        cTemp=temp,
        fTemp=convertedTemp
    ))

def fahrenheitToCelsius(fah):
    convertedTemp = (fah - 32) * (5 / 9)
    print("{fTemp}°C to Celsius = {cTemp:.1f}°F".format(
        fTemp=temp,
        cTemp=convertedTemp
    ))

if(select == "c"):
    celsiusToFahrenheit(temp)
if(select == "f"):
    fahrenheitToCelsius(temp)

