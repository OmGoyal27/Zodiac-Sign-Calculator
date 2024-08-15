from signs import findZodiacSign

date_of_birth = input("Enter DOB in the form of dd/mm: ")

DOB = date_of_birth.split("/")

def main(date, month):
    date = int(date)
    month = int(month)
    zodiac_sign_and_qualities = findZodiacSign(date, month)
    sign = zodiac_sign_and_qualities[0]
    qualities = zodiac_sign_and_qualities[1]
    print(f"Your Zodiac sign is {sign} and they are {qualities}")

date = DOB[0]
month = DOB[1]
main(date, month)