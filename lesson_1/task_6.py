# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет»,
# «декоратор». Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл в
# неизвестной кодировке. Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.


from chardet import detect

words = ['сетевое программирование', 'сокет', 'декоратор']

with open('test_file.txt', 'w', encoding='utf-8') as f:
    for i in words:
        f.write(i + '\n')

with open('test_file.txt', 'rb') as f:
    content = f.read()
encoding = detect(content)['encoding']
print('encoding: ', encoding)


with open('test_file.txt', encoding=encoding) as f_n:
    for el_str in f_n:
        print(el_str, end='')
    print()