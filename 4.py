#4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция.
# Функция шифрования
key= int(input('Ключ шифрования: \n'))
def cipher_encrypt(plain_text, key)-> str:
    
    encrypted = ""
    for c in plain_text:
        if c.isupper(): #проверить, является ли символ прописным
            c_index = ord(c) - ord('А')
            # сдвиг текущего символа на позицию key
            c_shifted = (c_index + key) % 33 + ord('А')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.islower(): #проверка наличия символа в нижнем регистре
            # вычесть юникод 'a', чтобы получить индекс в диапазоне [0-32)
            c_index = ord(c) - ord('а')
            c_shifted = (c_index + key) % 33 + ord('а')
            c_new = chr(c_shifted)
            encrypted += c_new
        elif c.isdigit():
            # если это число, сдвинуть его фактическое значение 
            c_new = (int(c) + key) % 10
            encrypted += str(c_new)
        else:
            # если нет ни алфавита, ни числа, оставить все как есть
            encrypted += c
    return encrypted
# Функция дешифрования
def cipher_decrypt(ciphertext, key)-> str:
    decrypted = ""
    for c in ciphertext:
        if c.isupper():
            c_index = ord(c) - ord('А')
            # сдвинуть текущий символ влево на позицию клавиши, чтобы получить его исходное положение
            c_og_pos = (c_index - key) % 33 + ord('А')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.islower():
            c_index = ord(c) - ord('а')
            c_og_pos = (c_index - key) % 33 + ord('а')
            c_og = chr(c_og_pos)
            decrypted += c_og
        elif c.isdigit():
            # если это число, сдвинуть его фактическое значение 
            c_og = (int(c) - key) % 10
            decrypted += str(c_og)
        else:
            # если нет ни алфавита, ни числа, оставить все как есть
            decrypted += c
    return decrypted


plain_text = "Привет, шифр Цезаря!"
ciphertext = cipher_encrypt(plain_text, key)
ciphertext = input("Шифруем:")
decrypted_msg = cipher_decrypt(ciphertext, key)
print("Зашифрованный текст:\n", ciphertext)
print("Расшифровка:\n",decrypted_msg)
f=open('cript.txt', mode='w', encoding='utf-8')
f.write(ciphertext)
f.close()
f_decript=open('decript.txt', mode='w', encoding='utf-8')
f_decript.write(decrypted_msg)
f_decript.close()