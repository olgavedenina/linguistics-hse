x = input("Enter a word: ")
i = 1
while x != "":
    x = input("Enter a word: ")
    i+=1
with open("text.txt", "w", encoding="utf-8") as f:
    for y in range(i):
        lines = list(len[i::])
        for line in lines:
            f.writelines(lines)
 
        
        
