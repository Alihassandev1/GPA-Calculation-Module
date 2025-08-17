# Sample Data of Students
studentData = {
    "003": {"name": "ABDUL REHMAN", "oop": 64, "dld": 77, "ew": 68, "ds": 76, "math": 50, "is": 78,"totalCH" : 18, "mathType": "MATH-110"},
    "004": {"name": "ANAS MAJEED", "oop": 80, "dld": 91, "ew": 76, "ds": 64, "math": 57, "is": 87,"totalCH" : 18, "mathType": "MATH-110"},
    "005": {"name": "ABDUL BASIT", "oop": 62, "dld": 65, "ew": 71, "ds": 78, "math": 56, "is": 83,"totalCH" : 18, "mathType": "MATH-110"},
    "006": {"name": "MUHAMMAD SHOAIB", "oop": 63, "dld": 64, "ew": 73, "ds": 76, "math": 45, "is": 89,"totalCH" : 18, "mathType": "MATH-110"},
    "007": {"name": "TALHA SHABBIR", "oop": 49, "dld": 78, "ew": 76, "ds": 68, "math": 58, "is": 89,"totalCH" : 18, "mathType": "MATH-110"},
    "009": {"name": "ARHAM", "oop": 51, "dld": 70, "ew": 74, "ds": 85, "math": 70, "is": 88,"totalCH" : 18, "mathType": "MATH-110"},
    "010": {"name": "SAQIB ALI", "oop": 51, "dld": 71, "ew": 65, "ds": 80, "math": 65, "is": 88,"totalCH" : 18, "mathType": "MATH-110"},
    "011": {"name": "MUNEEB ALI", "oop": 61, "dld": 88, "ew": 76, "ds": 69, "math": 54, "is": 88,"totalCH" : 18, "mathType": "MATH-110"},
    "012": {"name": "FURQAN", "oop": 67, "dld": 80, "ew": 67, "ds": 60, "math": 55, "is": 88,"totalCH" : 18, "mathType": "MATH-110"},
    "013": {"name": "MUHAMMAD TAHA RASHEED", "oop": 67, "dld": 79, "ew": 73, "ds": 61, "math": 57, "is": 90,"totalCH" : 18, "mathType": "MATH-110"},
    "014": {"name": "MIRZA SUBHAN TAYIB", "oop": 66, "dld": 68, "ew": 63, "ds": 64, "math": 50, "is": 86,"totalCH" : 18, "mathType": "MATH-110"},
    "015": {"name": "DAWOOD AHMAD", "oop": 62, "dld": 72, "ew": 66, "ds": 75, "math": 50, "is": 86,"totalCH" : 18, "mathType": "MATH-110"},
    "018": {"name": "ALI HUSNAIN", "oop": 63, "dld": 86, "ew": 74, "ds": 80, "math": 57, "is": 88,"totalCH" : 18, "mathType": "MATH-110"},
    "019": {"name": "ABDULLAH ASIF", "oop": 48, "dld": 49, "ew": 59, "ds": 74, "math": 60, "is": 73,"totalCH" : 18, "mathType": "MATH-110"},
    "020": {"name": "HANZLA AMANAT", "oop": 49, "dld": 49, "ew": 65, "ds": 76, "math": 65, "is": 70,"totalCH" : 18, "mathType": "MATH-110"},
    "021": {"name": "ABDULLAH IMRAN", "oop": 48, "dld": 39, "ew": 68, "ds": 67, "math": 70, "is": 74,"totalCH" : 18, "mathType": "MATH-110"},
    "008": {"name": "MUHAMMAD ABDULLAH", "oop": 49, "dld": 60, "ew": 75, "ds": 80, "math": 40, "is": 76,"totalCH" : 15, "mathType": "MATH-128"},
    "016": {"name": "FAHAD SAEED", "oop": 45, "dld": 64, "ew": 72, "ds": 84, "math": 40, "is": 90,"totalCH" : 15, "mathType": "MATH-128"},
    "017": {"name": "MUHAMMAD ABU BAKAR CHEEMA", "oop": 60, "dld": 66, "ew": 72, "ds": 79, "math": 40, "is": 88,"totalCH" : 15, "mathType": "MATH-128"}
}

# GPA scale according to UOG
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

# Sample Credit Hours of Calculus and Pre-Calculus Students
# Credit Hours of Calculus Students
creditHoursEng = [4, 3, 3, 3, 3, 2]
# Credit Hours of Pre-Calculus Students
creditHoursPre = [4, 3, 3, 3, 0, 2]

# Calculation of GPA of every Student
def calculateGPA(studentData, creditHoursEng, creditHoursPre):
    for std in studentData.values():
        tempChSum = 0
        count = 0
        for i in ["oop", "dld", "ew", "ds", "math", "is"]:
            if std["mathType"] == "pre":
                tempChSum += gpaScale(std[i]) * creditHoursPre[count]
            else:
                tempChSum += gpaScale(std[i]) * creditHoursEng[count]
            count += 1
        std["gpa"] = round(tempChSum / std["totalCH"], 1)
    else:

        return studentData
