a = int(input())
b = int(input())
c = int(input())
if a + b == c and a*c + b == 0:
    print("Conditions 1 and 4")
elif a + b == c and a*c + b != 0:
    print("Only condition 1")
elif a + b != c and a*c + b == 0:
    print("Only condition 4")
else:
    print("None of the conditions")
