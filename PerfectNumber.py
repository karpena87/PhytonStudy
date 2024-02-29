#перебрать числа по порядку до n-1
#находить остаток от деления n на каждое число
#если остаток от деления 0 - то прибавить к сумме
#если сумма итого равна n - выводить True
#счастливые числа 6 28 496 8128

n = int(input("Введите любое число "))

def is_perfect_number(n):
    s=0
    for a in range (1,n-1):
        if n % a == 0:
            s = s + a
    if n==s:
        return(True)
    else:
        return(False)

result = is_perfect_number(n)
print(result)