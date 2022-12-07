#В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, 
# которые имеют средний балл более «4».
#Нужно перезаписать файл.
from typing import List

f=open('stud.txt', mode='r', encoding='utf-8')
string_stud=f.read().split('\n')
f.close()

def upper_registr(strs: List[str])->str:
    """_summary_

    Args:
        strs (List[str]): _первоначальный список студентов(из файла)

    Returns:
        str:  обновленный список(в верхнем регистре, если строка содержит 5)
    """
    f=''
    for li in strs:
        if li.count('5'):
            li=li.upper()
        string=li+'\n'
        f+=string
    return f

f_new = upper_registr(string_stud)
f=open('stud.txt', mode='w', encoding='utf-8')
f.write(f_new)
f.close()


# upper_registr("stud.txt")
# while True:
#     line=f.readline()
#     str=line.split()
#     if '5' in str:
#         print(line.upper())
#         # f.seek(0)
#         # f.write(line.upper())  
#     else:
#         print(line)
#         # f.seek(10)
#         # f.write(line)      
#     if not line:
#         break
# f.seek(0)
# f.write(line)  
# # f.close()
# with open('stud.txt',mode='r', encoding='utf-8') as f1, open('stud1.txt',mode='w', encoding='utf-8') as f2:
#     lines = f1.readline()
#     print(lines)
#     for line in lines:
#         line = line.split(' ')
#         if str == '5':
#             f2.write(str(line.upper()))
#         else:
#             f2.write(str(line))