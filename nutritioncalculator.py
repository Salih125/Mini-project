class Nutritioncalculator:
    # calculates daily protein
    def procalc(weight):
        pro = weight * 1.5
        return pro
    
    # calculates daily calories
    def calcalc(gender, weight, height, age):
        calories = 0
        # if gender is true calories calulated is for women
        if gender == 'f':
            calories = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
        else:
            calories = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
        return calories

