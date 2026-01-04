def gpaScale(num):
    if num >= 84.5: return 4.00
    elif num >= 79.5: return 3.70 
    elif num >= 74.5: return 3.50
    elif num >= 69.5: return 3.00
    elif num >= 64.5: return 2.50
    elif num >= 59.5: return 2.00 
    elif num >= 54.5: return 1.50
    elif num >= 49.5: return 1.00
    else: return 0.00

def calculate_sgpa(marks, credits):
    total = 0
    for i in range(len(marks)):
        m = gpaScale(marks[i])
        c = credits[i]
        total += m * c
    return total / sum(credits)

def calculate_cgpa(sgpa, credits):
    total = 0
    for i in range(len(sgpa)):
        total += sgpa[i] * credits[i]
    return total / sum(credits)