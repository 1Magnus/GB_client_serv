# Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом,
# а не ручном режиме, с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы
# encode, decode или функцию bytes) и определить тип, содержимое и длину соответствующих переменных.

words = ['class', 'function', 'method']
for i in words:
    print('содержимое - ', i)
    print('тип - ', type(i))
    print('длина - ', len(i))
    result = eval(f'b"{i}"')
    print('содержимое - ', result)
    print('тип - ', type(result))
    print('длина - ', len(result))