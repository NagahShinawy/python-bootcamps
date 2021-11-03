# BMI = (weight in Kg)/(Height in Meters)^2.


def calc_bmi(weight: float, height: float) -> float:
    return weight / height ** 2


print(calc_bmi(60, 186))
