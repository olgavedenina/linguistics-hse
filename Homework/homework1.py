a = int(input())
b = int(input())
c = int(input())
if a + b == c and a*c + b == 0:
    print("conditions 1 and 4")
elif a + b == c and a*c + b != 0:
    print("only condition 1")
elif a + b != c and a*c + b == 0:
    print("only condition 4")
else:
    print("none of the conditions")
