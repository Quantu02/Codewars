'''Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"
'''
def bmi(weight, height):
    index= weight/(height**2)
    if index <= 18.5:
        return "Underweight"
    elif index <= 25.0:
        return "Normal"
    elif index <= 30.0:
        return "Overweight"
    elif index > 30:
        return "Obese"