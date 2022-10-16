list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

max_index = 0  # индекс первого элемента для начала
max_numbers = list_numbers[max_index]  # его значения
last_index = -1  # индекс который нужно поменять

for i in range(len(list_numbers)):  # перебераем все индексы
    if list_numbers[i] > list_numbers[max_index]:  # сравниваем текущий индекс с начальным
        max_index = i  # перезадаем индекс максимального
list_numbers[max_index], list_numbers[last_index] = list_numbers[last_index], list_numbers[max_index] # меняем местами максимальный и последний элементы.

print(list_numbers)
