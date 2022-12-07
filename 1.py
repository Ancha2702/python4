# 1 - Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
n= int(input('Введите натуральное число \n'))
def find_multiplier(n)->int: 
    """Нахождение простых множителей для натуральных чисел

    Args:
        n (int): натуральное число

    Returns:
      i=2  первый простой множитель
      multiplier - список, куда записываюся простые множители
    
    """
    multiplier = []
    for i in range(2,n+1):
        while not n % i:
            if not multiplier.count(i): # проверка на неповторяемость
                multiplier.append(i)
            n = n / i
        else:
            i=i+1  
    return multiplier
print(find_multiplier(n))
