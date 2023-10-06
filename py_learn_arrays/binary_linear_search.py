import random
import timeit


# Функція для виконання послідовного пошуку
def sequential_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1


# Функція для виконання бінарного пошуку
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# Декоратор для вимірювання часу виконання функції
def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = timeit.default_timer()
        result = func(*args, **kwargs)
        end_time = timeit.default_timer()
        execution_time = end_time - start_time
        return result, execution_time
    return wrapper


# Створення відсортованого масиву різного розміру
array_sizes = [1000, 10000, 100000, 1000000]

# Виконання експериментів для кожного розміру масиву
for size in array_sizes:
    # Generate a sorted array
    array = [i for i in range(size)]
    target = random.randint(1, size - 1)  # Random target within the range of the array

    # Вимірювання часу для послідовного пошуку
    sequential_search_timed = measure_time(sequential_search)
    result, time_taken = sequential_search_timed(array, target)
    print(f"result id = {result}")
    print(f"Послідовний пошук {target} у відсортованому масиві розміру {size} зайняв {time_taken:.8f} секунд")

    # Вимірювання часу для бінарного пошуку
    binary_search_timed = measure_time(binary_search)
    result, time_taken = binary_search_timed(array, target)
    print(f"Бінарний пошук {target} у відсортованому масиві розміру {size} зайняв {time_taken:.8f} секунд")
    print('-' * 50)
