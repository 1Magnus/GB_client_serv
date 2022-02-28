from chardet import detect
import re
import csv


def get_data():
    list_files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]
    for i in list_files:
        with open(i, 'rb') as f:
            content = f.read()
            encoding = detect(content)['encoding']
            content = content.decode(encoding)

        # Найти все подряд по  строкам
        # match = re.findall(r'(\w[^:]+).*:\s+([^:\n,\r]+)\s\n', content)

        os_prod_list.append(re.findall(r'Изготовитель системы:\s+([^:\n,\r]+)\s\n', content))
        os_name_list.append(re.findall(r'Название ОС:\s+([^:\n,\r]+)\s\n', content))
        os_code_list.append(re.findall(r'Код продукта:\s+([^:\n,\r]+)\s\n', content))
        os_type_list.append(re.findall(r'Тип системы:\s+([^:\n,\r]+)\s\n', content))

    for i in range(len(os_prod_list)):
        main_data.append([os_prod_list[i][0], os_name_list[i][0], os_code_list[i][0], os_type_list[i][0]])

    return main_data


def write_to_csv(file_path):
    data = get_data()
    with open(file_path, 'w', encoding='utf-8') as f_n:
        writer_scv = csv.writer(f_n)
        for row in data:
            writer_scv.writerow(row)


if __name__ == '__main__':
    write_to_csv(r'F:\GB_client_serv\lesson_2\task_1\DATA.csv')
