
number =int(input("Please enter a number: ")) 
def Is_Prime(number):
    if number > 1:
        for i in range(2,number):
            if number % i ==0.0: 
                print("Not a prime number")
                break
            else:
                print("Prime number")
                break
    else:
        print("Not a prime number")
