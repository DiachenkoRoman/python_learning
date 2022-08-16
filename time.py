
_minutes = int(input("Enter minutes (0-59) "))

if 0 <= _minutes <= 15:
    print("first quarter")

elif 15 < _minutes < 30:
    print("second quarter")

elif 30 < _minutes < 45:
    print("third quarter")

elif 45 < _minutes < 59:
    print("fourth quarter")

else:

    print("bad input")
