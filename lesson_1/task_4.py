# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в
# байтовое и выполнить обратное преобразование (используя методы encode и decode)
words = ['разработка', 'администрирование', 'protocol', 'standard']
for i in words:
    print(i, type(i))
    i_bytes = i.encode('utf-8')
    print(i_bytes, type(i_bytes))
    i_dec = i_bytes.decode('utf-8')
    print(i, type(i), '- декодировали обратно')
    print('-' * 100)
