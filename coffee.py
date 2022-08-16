import math

_coffeeCaps = int(input("How much caps "))

if _coffeeCaps > 6:

    print("Hold your " + str(_coffeeCaps) + " caps of coffee " +
          "+" + str(math.floor(_coffeeCaps / 6)) + " bonus caps")

else:

    print("Hold your " + str(_coffeeCaps) + " caps of coffee")