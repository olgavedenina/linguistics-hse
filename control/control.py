with open("Extinct_languages.txt", encoding="utf-8") as f:
    lines = f.readlines()
    #for line in lines:        
        #if len(line)>35:
            #print(line)
   
    
    
    a = 0
    b = "Critically endangered"
    for line in f:
        for word in line.split("\t"):
            if word[-1] == b:
                a += 1
    print(a)
            
    
        
    
                    
