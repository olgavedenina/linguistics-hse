a = 0
b = 0
with open("text.txt", encoding = "utf-8") as f:
    text = f.read()
text = text.replace (".", "")
text = text.replace (",", "")
text = text.replace ("–", "")
words = text.split()
for word in words:
    if len(word)==1:
        a += 1
    if len(word)==3:
        b += 1
if a == 0:
    print("NO")
else:
    print(b/a)
    
    
