a=input("Введите слово: ")
res= ""
for i in range(len(a)):
    for letter in a:
        if letter != "з" and letter != "я":
            res += letter
    break
print(res[::-1])
