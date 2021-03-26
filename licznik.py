print("Wprowadź 5 wyrazów. Licznik sprawdzi które z nich zacznają się od wielkiej litery")
counter=0
for i in range(5):
    print("Wyraz {}:".format(i+1))
    try:
        wyraz=str(input())
        if(wyraz[0].isupper()):
            counter+=1
    except (IOError, ValueError, IndexError):
        print("Błąd przy wprowadzaniu wyrazu. Wyraz {} pominięty".format(i+1))
print(counter)        

