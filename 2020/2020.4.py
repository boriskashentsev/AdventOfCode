def checkForValidity(passport):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    correctFields = 0
    for key in passport.keys():
        if (key in fields):
            correctFields = correctFields + 1
    if(correctFields == 7):
        return 1
    else:
        return 0

def fieldCheck(field, value):
    if (field == "byr"):
        if (len(value) == 4 and value.isdigit() and int(value) >= 1920 and int(value) <= 2002):
            return True
    if (field == "iyr"):
        if (len(value) == 4 and value.isdigit() and int(value) >= 2010 and int(value) <= 2020):
            return True
    if (field == "eyr"):
        if (len(value) == 4 and value.isdigit() and int(value) >= 2020 and int(value) <= 2030):
            return True
    if (field == "hgt"):
        if(len(value.split("cm"))==2):
            number = value.split("cm")[0]
            if (number.isdigit() and int(number) >= 150 and int(number)<= 193):
                return True
        if(len(value.split("in"))==2):
            number = value.split("in")[0]
            if (number.isdigit() and int(number) >= 59 and int(number)<= 76):
                return True
    if (field == "hcl"):
        color = value.split("#")
        if len(color)==2 and color[0] == "" and len(color[1]) == 6:
            for char in color[1]:
                if char not in "0123456789abcdef":
                    return False
            return True
    if (field == "ecl"):
        if value in ["amb", "blu","brn", "gry", "grn", "hzl", "oth"]:
            return True
    if (field == "pid"):
        if (len(value) == 9 and value.isdigit()):
            return True
    
    return False

def checkForValidityStrict(passport):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    correctFields = 0
    for key in passport.keys():
        if (key in fields):
            if fieldCheck(key, passport[key]):
                correctFields = correctFields + 1
    if(correctFields == 7):
        return 1
    else:
        return 0

filename = "2020/4.input"

f = open(filename, "r")

inpt = f.read().split("\n")

passports = []
passport = {}


for line in inpt :
    if line != "" :
        parts = line.split(" ")
        for part in parts :
            entry = part.split(":")
            if (entry[0] in passport.keys()):
                print("WARNING: double field")
            passport[entry[0]] = entry[1]
    else :
        passports.append(passport)
        passport = {}
passports.append(passport)

answer1 = 0
answer2 = 0
for passport in passports:
    answer1 = answer1 + checkForValidity(passport)
    answer2 = answer2 + checkForValidityStrict(passport)

print("first part: ", answer1)
print("second part: ", answer2)