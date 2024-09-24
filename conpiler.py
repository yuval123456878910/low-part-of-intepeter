text = input("Input: ")





num = 0
poc = list()

hen = str()

for i in text:
    if i in "+-*/":
        poc.append(hen)
        hen = str()
        poc.append(str(i))
    else:
        hen += i
if hen != "":
    poc.append(hen)

num = float(poc[0])
on = 0


for i in poc:
    try:
        if poc[on] == "+":
            num = num + float(poc[on+1])
            
            on += 1
        if poc[on] == "*":
            num = num * float(poc[on+1])
            
            on += 1
        if poc[on] == "/":
            num = num / float(poc[on+1])
            
            on += 1
        if poc[on] == "-":
            num = num - float(poc[on+1])
            
            on += 1
        else:
            on += 1
            
    except:
        pass
    
print(num)
