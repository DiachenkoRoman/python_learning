
# _stars = int(input("How much stars "))
#
# for i in range(_stars):
#     print("*" * (i+1))
#_________________________________________________________

_stars = int(input("How much stars "))
i = 0

while i < _stars:

    print("*" * (i+1))

    i += 1

    if i == _stars:
        break
