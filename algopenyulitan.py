from secretpy.ciphers.autokey import Autokey
from secretpy import Caesar, Vigenere
import math

pilihan = input('''Sila Pilih algo mana yang anda mahu guna
[1] Caesar cipher
[2] Monoalphabetic cipher
[3] Rail fence cipher
[4] Row transposition cipher
[5] Vigenere Cipher
[6] Vigenere AutoKey System
[7] Vernam Cipher
''')

print(f'\nAnda masukkan pilihan {pilihan}\n\nPastikan plaintext tiada jarak!')


def railfence(plaintext, key):
    rail = [['\n' for i in range(len(plaintext))]
            for j in range(key)]

    dir_down = False
    row, col = 0, 0

    for i in range(len(plaintext)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = plaintext[i]
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    result = []
    for i in range(key):
        for j in range(len(plaintext)):
            if rail[i][j] != '\n':
                result.append(rail[i][j])

    return("" . join(result))


def rowtransposition(plaintext, key):
    cipher = ""

    k_indx = 0

    msg_len = float(len(plaintext))
    msg_lst = list(plaintext)
    key_lst = sorted(list(key))

    col = len(key)

    row = int(math.ceil(msg_len / col))

    fill_null = int((row * col) - msg_len)
    msg_lst.extend('_' * fill_null)

    matrix = [msg_lst[i: i + col]
              for i in range(0, len(msg_lst), col)]

    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        cipher += ''.join([row[curr_idx]
                           for row in matrix])
        k_indx += 1

    return cipher


if int(pilihan) == 1:
    pt = input('Masukkan plaintext: ')
    kc = int(input('Masukkan key: '))
    kesar = Caesar().encrypt(pt, kc)
    print(f'\nCiphertext: {kesar.upper()}')

elif int(pilihan) == 3:
    pt = input('Masukkan plaintext: ')
    kc = int(input('Masukkan depth: '))
    keretapi = railfence(pt, kc)
    print(f'\nCiphertext: {keretapi.upper()}')

elif int(pilihan) == 4:
    pt = input('Masukkan plaintext: ')
    kc = input('Masukkan key: ')
    tukarbaris = rowtransposition(pt, kc)
    print(f'\nCiphertext: {tukarbaris.upper()}')

elif int(pilihan) == 5:
    pt = input('Masukkan plaintext: ')
    kc = input('Masukkan key: ')
    virgin = Vigenere().encrypt(pt, kc)
    print(f'\nCiphertext: {virgin.upper()}')

elif int(pilihan) == 6:
    pt = input('Masukkan plaintext: ')
    kc = input('Masukkan key: ')
    auto = Autokey()
    enc = auto.encrypt(pt, kc)
    print(f'\nCiphertext: {enc.upper()}')

else:
    pt = int(input('Masukkan plaintext: '), 2)
    kc = int(input('Masukkan key: '), 2)
    output = pt ^ kc
    print(bin(output))
