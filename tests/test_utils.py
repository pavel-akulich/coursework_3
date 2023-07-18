# в данном файле прописаны тесты к проекту
#  импортируем наши функции для тестов
from src.main import *
from src.utils import *


def test_read_data():
    assert read_data("src/operations.json") != []
    assert read_data("src/operations.json") != False
    assert read_data("src/operations.json") != ""


def test_sorted_operations():
    assert sorted_operations([]) == []
    assert sorted_operations([{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}]) == [{'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'}]


def test_sort_operations_executed():
    assert sort_operations_executed([]) == []
    assert sort_operations_executed([{'id': 41428829, 'state': 'EXECUTED'}]) == []
    assert sort_operations_executed([{'id': 41428829, 'statisctic': 'EXECUTED'}]) == []


def test_output_info():
    assert output_info([]) == ""
    assert output_info([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364', 'operationAmount': {'amount': '8221.37', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'MasterCard 7158300734726758', 'to': 'Счет 35383033474447895560'}]) != ""


