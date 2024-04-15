num=int(input('enter the number'))
if(num>1):
    for i in range(2,num):
        if(num%i)==0:
            print('given number is not prime number')
            break
    else:
        print('given number is prime number ')
else:
    print('given number is prime number')
    
    
