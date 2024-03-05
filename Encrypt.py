#определелить переменную word
#определить длину слова  word.__len__()
#привести строку к списку list(word)
#цикл для каждой пары символов [n,n+1] делать перестановку
#проверка что символ нечетный
#преобразовать список в строку


word = input('Введите любое слово или последовательность букв: ')
word_lenth = int(word.__len__())
l = list(word)
def encrypt():
    for n in range (1, word_lenth):
        if n % 2 == 1:
          l[n], l[n-1] = l[n-1], l[n]
        n = n + 1
    return ''.join(l)

result = encrypt()
print(result)

