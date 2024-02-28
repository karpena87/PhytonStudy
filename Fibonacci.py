n = int(input("Введите любое число: "))

a = 1
f2 = 0
summ = 0

print ("Последовательность Фибоначчи до " + str(n) + " числа:")

while a <= n:
    if a == 1:
        f1=1
        summ = f1 + f2
        f2 = summ
        a = a + 1
        print (f1)
    elif a == 2:
        f1 = 1
        summ = f1 + f2
        #f2 = summ
        a = a + 1
        print (f1)
    else:
        summ = f1 + f2
        f1 = f2
        f2 = summ
        a = a + 1
        print (summ)

print (str(int(n)) + ' число в последовательности Фибоначчи: ' + str(summ))