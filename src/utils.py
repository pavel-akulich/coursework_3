# В данном файле лежат наши функции
# импортируем необходимые библиотеки
import json
from datetime import datetime


def read_data(filename):
    """
    Читает json файл и возвращает данные, лежащие в нем
    """
    with open(filename) as file:
        data = json.load(file)
        return data


def sorted_operations(value):
    """
    Функция сортировки операций по дате
    """
    sorted_operation = []
    for op in value:
        if 'date' in op:
            try:
                sorted_operation.append(op)
            except KeyError:
                continue
    sort_data = sorted(sorted_operation, key=lambda operation: datetime.fromisoformat(op['date']), reverse=True)
    return sort_data


def sort_operations_executed(sorted_operation_value):
    """
    Функция сортировки выполненных операций
    """
    successful_operations = []
    for el in sorted_operation_value:
        try:
            if el['state'] == "EXECUTED":
                successful_operations.append(el)
        except KeyError:
            continue
    return successful_operations[1:6]


def output_info(operations_executed):
    """
    Вывод информации по последним 5 операциям пользователю
    """
    output_result = ""
    for el in operations_executed:
        date_operation = el['date'][8:10] + '.' + el['date'][5:7] + '.' + el['date'][0:4]
        try:
            x = el['from']
            element_from = x[0:-16] + x[-16:-12] + " " + x[-12:-10] + "** *** " + x[-4:]
        except KeyError:
            element_from = "Неизвестно"
        element_to = "**" + el['to'][-4:]
        info_for_user = f''' 
        {date_operation} {el['description']}
        {element_from} -> {element_to}
        {el['operationAmount']['amount']} {el['operationAmount']['currency']['name']}
        '''
        output_result += info_for_user
    return output_result
