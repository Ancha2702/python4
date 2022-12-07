# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие
rand_list = list(map(int, input('Введите целые числа через пробел ').split()))
print(f'Исходный список: {rand_list}')
def find_duplicate(rand_list)-> list:
    """Список неповторяющихся элементов в массиве чисел

    Args:
        rand_list (_list_): _исходный массив
        list_new (_list_): _вспомогательный массив
    Returns:
        rand_list (list): _возвращает массив без дубликатов_
    """
    list_new=[]
    for i in rand_list:
        if i not in list_new:
            list_new.append(i)
    rand_list=list_new
    return rand_list

print(f'Список без дубликатов: {find_duplicate(rand_list)}')
