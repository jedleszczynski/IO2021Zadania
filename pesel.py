def is_pesel_valid():
    pesel_number=input()
    weight = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    sum = 0
    for i in range(10):
        sum += int([char for char in pesel_number][i])*weight[i]
    check_digit = 10 - int(str(sum)[-1])
    if(str(check_digit)== str(pesel_number)[-1]):
        print(1)
    else:    
        print(0)        
if __name__ == "__main__":
    is_pesel_valid()