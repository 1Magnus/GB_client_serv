# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на
# кириллице.

import chardet   # необходима предварительная инсталляция: pip install chardet
import subprocess
import platform
import locale


default_encoding = locale.getpreferredencoding()
print(default_encoding)

param = '-n' if platform.system().lower() == 'windows' else '-c'
args = ['ping', param, '2', 'yandex.ru']
args2 = ['ping', param, '2', 'youtube.com']

process = subprocess.Popen(args, stdout=subprocess.PIPE)
process2 = subprocess.Popen(args2, stdout=subprocess.PIPE)

for line in process.stdout:
    print(line.decode(default_encoding))
for line in process2.stdout:
    print(line.decode(default_encoding))

