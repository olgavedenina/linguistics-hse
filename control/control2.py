a = 0
with open("Extinct_languages.txt", encoding = "utf-8") as f:
    text = f.read()
    text = text.replace (".", "")
    text = text.replace (",", "")
    text = text.replace ("–", "")
    words = text.split("\t")
    for word in words:
        if word == "Critically endangered":
            a += 1
    print(a)

   
