# В данном файле прописана основная логика программы
# импортируем функции
from src.utils import *

# Переменная, хранящая список операций
transactions = "operations.json"


def main():
    get_transactions_list = read_data(transactions)
    sort_operations = sorted_operations(get_transactions_list)
    executed_operations = sort_operations_executed(sort_operations)
    print(output_info(executed_operations))


if __name__ == '__main__':
    main()
