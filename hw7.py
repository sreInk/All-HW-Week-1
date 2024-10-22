td = {'Shreyas' : 2,'is' : 2, 'the': 1, 'best' : 2}
k = int(input("Enter A NUmber Between 1 to 2 For Best Experience : "))
r = 0
for key in td:
    if td[key] == k:
        r = r + 1
print("Frez is :", str(r))
