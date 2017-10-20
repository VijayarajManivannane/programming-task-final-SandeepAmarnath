l=[]
maxi=[]
with open('Book1.txt', encoding="utf8") as book_1:
     for line in book_1:
         line=line.split()
         for word in line:
             l.append(word)
     #print(l)
     book1_max=max(l,key=len)
     maxi.append(book1_max)

a=[]
with open('Book2.txt', encoding="utf8") as book_2:
    for line2 in book_2:
        line2=line2.split()
        for words in line2:
            a.append(words)
    #print(a)
    book2_max = max(a, key=len)
    maxi.append(book2_max)


c=[]

with open('Book3.txt', encoding="utf8") as book_3:
    for line3 in book_3:
        line3=line3.split()
        for words in line3:
            c.append(words)
    #print(c)
    book3_max = max(c, key=len)
    maxi.append(book3_max)
    print(maxi)

    print("The maximum of three books is "+str(max(maxi,key=len)))

