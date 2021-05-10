a = set()
b = set()
with open("Beyondsleep.txt",encoding = 'utf-8') as file:
    for line in file:
        for word in line.split():
           a.add(word)
           
           
with open("pride&prejudice.txt",encoding = 'utf-8') as f:
    for l in f:
        for w in l.split():
           b.add(w)
           
           

for w in a.intersection(b):
    print (w)