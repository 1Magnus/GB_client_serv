# Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться доступность сетевых узлов.
# Аргументом функции является список, в котором каждый сетевой узел должен быть представлен именем хоста или
# ip-адресом. В функции необходимо перебирать ip-адреса и проверять их доступность с выводом соответствующего
# сообщения («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться с помощью
# функции ip_address(). (Внимание! Аргументом сабпроцеса должен быть список, а не строка!!! Крайне желательно
# использование потоков.)

import threading
import locale
import platform
from subprocess import Popen, PIPE
from ipaddress import ip_address
from tabulate import tabulate

ENCODING = locale.getpreferredencoding()
param = '-n' if platform.system().lower() == 'windows' else '-c'
available = {'Доступен': '', }
not_available = {'Недоступен': '', }


def check_ip(adres):
    try:
        ip = ip_address(adres)
    except ValueError:
        return False
    return ip


def ping(ip, flag=False):
    ip_adres = check_ip(ip) if check_ip(ip) else ip
    reply = Popen(['ping', param, '1', str(ip_adres)], stdout=PIPE)
    if reply.wait() == 0:
        if not flag:
            print(f'{ip} - Узел доступен')
        else:
            available['Доступен'] += f'{ip}\n'
    else:
        if not flag:
            print(f'{ip} - Узел недоступен')
        else:
            not_available['Недоступен'] += f'{ip}\n'


def host_ping(list_ip, flag=False):
    threads = []

    for host in list_ip:
        THR = threading.Thread(target=ping, args=(host, flag,), daemon=True)
        THR.start()
        threads.append(THR)

    for thread in threads:
        thread.join()


# Написать функцию host_range_ping() (возможности которой основаны на функции из примера 1) для перебора ip-адресов
# из заданного диапазона. Меняться должен только последний октет каждого адреса. По результатам проверки должно
# выводиться соответствующее сообщение.

def host_range_ping(flag=False):
    while True:
        start = input('Введите IP: ')
        if not start:
            start = '8.8.8.8'
        if check_ip(start):
            break

    ip = start.split('.')
    oct = int(ip[3])

    while True:
        rangeu = input('Введите дипазон: ')
        if rangeu.isdigit() and oct + int(rangeu) < 256:
            break
    rangeu = int(rangeu)
    resault = []
    for i in range(rangeu):
        new_oct = oct + i
        new_ip = ip[:3]
        new_ip.append(str(new_oct))
        resault.append('.'.join(new_ip))
    host_ping(resault, flag)


# Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2. Но в данном случае
# результат должен быть итоговым по всем ip-адресам, представленным в табличном формате (использовать модуль
# tabulate).
def host_range_ping_tab():
    host_range_ping(flag=True)
    print(tabulate([available, not_available], headers='keys', tablefmt='pipe', stralign='center'))


if __name__ == '__main__':
    # default_list_ip = ['192.168.1.1', 'yandex.ru', '8.8.8.8', 'aaaa', '12', ]
    # host_ping(default_list_ip)
    host_range_ping()
    host_range_ping_tab()
