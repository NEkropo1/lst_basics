import random
import timeit
import numpy as np
import pandas as pd

# Генерування великого масиву випадкових чисел
data_size = 10000000
data = [random.randint(1, 1000000) for _ in range(data_size)]


def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        return result, execution_time

    return wrapper


# Звичайний список
def list_operations(data):
    data_copy = data.copy()

    # Додавання елементу
    list_append_timed = measure_time(lambda x: x.append(999))
    result, time_taken = list_append_timed(data_copy)
    print(f"Додавання елементу у список: {time_taken:.8f} секунд")

    # Вставка елементу
    list_insert_timed = measure_time(lambda x: x.insert(5000, 999))
    result, time_taken = list_insert_timed(data_copy)
    print(f"Вставка елементу у список: {time_taken:.8f} секунд")

    # Сортування
    list_sort_timed = measure_time(lambda x: x.sort())
    result, time_taken = list_sort_timed(data_copy)
    print(f"Сортування списку: {time_taken:.8f} секунд")


# NumPy масив
def numpy_operations(data):
    data_copy = np.array(data)

    # Додавання елементу
    numpy_append_timed = measure_time(lambda x: np.append(x, 999))
    result, time_taken = numpy_append_timed(data_copy)
    print(f"Додавання елементу у NumPy масив: {time_taken:.8f} секунд")

    # Вставка елементу
    numpy_insert_timed = measure_time(lambda x: np.insert(x, 5000, 999))
    result, time_taken = numpy_insert_timed(data_copy)
    print(f"Вставка елементу у NumPy масив: {time_taken:.8f} секунд")

    # Сортування
    numpy_sort_timed = measure_time(lambda x: np.sort(x))
    result, time_taken = numpy_sort_timed(data_copy)
    print(f"Сортування NumPy масиву: {time_taken:.8f} секунд")


# Pandas DataFrame
def pandas_operations(data):
    data_copy = pd.DataFrame(data, columns=['value'])

    # Додавання рядку
    data_to_append = pd.DataFrame({'value': [999]})
    pandas_append_timed = measure_time(lambda x, y: x._append(y))
    result, time_taken = pandas_append_timed(data_copy, data_to_append)
    print(f"Додавання рядку у Pandas DataFrame: {time_taken:.8f} секунд")

    # Вставка рядку
    data_to_insert = pd.DataFrame({'value': [999]})
    pandas_insert_timed = measure_time(lambda x, y: x.loc[5000] == y.iloc[0])
    result, time_taken = pandas_insert_timed(data_copy, data_to_insert)
    print(f"Вставка рядку у Pandas DataFrame: {time_taken:.8f} секунд")

    # Сортування
    pandas_sort_timed = measure_time(lambda x: x.sort_values('value'))
    result, time_taken = pandas_sort_timed(data_copy)
    print(f"Сортування Pandas DataFrame: {time_taken:.8f} секунд")


# Виклик функцій для різних представлень масивів
print("Для звичайного списку:")
list_operations(data)
print("\nДля NumPy масиву:")
numpy_operations(data)
print("\nДля Pandas DataFrame:")
pandas_operations(data)
