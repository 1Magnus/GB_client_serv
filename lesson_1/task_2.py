# Каждое из слов «class», «function», «method» записать в байтовом типе. Сделать это необходимо в автоматическом,
# а не ручном режиме, с помощью добавления литеры b к текстовому значению, (т.е. ни в коем случае не используя методы
# encode, decode или функцию bytes) и определить тип, содержимое и длину соответствующих переменных.

words = ['class', 'function', 'method']
for i in words:
    print(f'содержимое - {i}, тип - {type(i)}, длина - {len(i)}')
    result = eval(f'b"{i}"')
    print(f'содержимое - {result}, тип - {type(result)}, длина - {len(result)}')
