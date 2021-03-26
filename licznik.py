print("Wprowadź 5 wyrazów. Licznik sprawdzi które z nich zacznają się od wielkiej litery")
counter=0
for i in range(5):
    print("Wyraz {}:".format(i+1))
    wyraz=str(input())
    if(wyraz[0].isupper()):
        counter+=1
print(counter)        

