num=int(input("enter a number : "))
parells = 0
senars = 0
if num <= 0 :
    print("error")
elif num % 2 == 0 :
    print("NO")
else:
    while num != 0:
        resto = num % 10
        num = num // 10
        if resto % 2 == 0:
            parells += 1
        else:
            senars += 1
    if senars == parells:
        print("Si")
    else:
        print("NO")