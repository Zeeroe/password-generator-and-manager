plain_text = """CORRECT
Website1,Username,Password
Website2,Username,Password
Website3,Username,Password
Website4,Username,Password
Website5,Username,Password
Website6,Username,Password
Website7,Username,Password
Website8,Username,Password
Website9,Username,Password
Website10,Username,Password
Website11,Username,Password
Website12,Username,Password
Website13,Username,Password
Website14,Username,Password
Website15,Username,Password
Website16,Username,Password
Website17,Username,Password
Website18,Username,Password
Website19,Username,Password
Website20,Username,Password
Website21,Username,Password
Website22,Username,Password
Website23,Username,Password
Website24,Username,Password
Website25,Username,Password
Website26,Username,Password
Website27,Username,Password
Website28,Username,Password
Website29,Username,Password
Website30,Username,Password
"""


def encrypt(logins, num1, num2, num3, num4):
    ascii_list = []

    for i in logins:
        encrypt_value = ord(i)
        encrypt_value = (((encrypt_value + num1) - num2) * num3) * num4
        ascii_list.append(encrypt_value)

    with open('logins.txt', 'w', newline='') as logins_file:
        ascii_list = map(str, ascii_list)
        x = ' '.join(ascii_list)
        logins_file.write(x)
        print('Encrypted: ' + x)


def decrypt(data, num1, num2, num3, num4):
    decoded_list = []
    for i in data:
        decrypt_value = i
        decrypt_value = (((decrypt_value // num4) // num3) + num2) - num1
        decoded_list.append(chr(decrypt_value))
    decrypted_text = ''.join(decoded_list)

    if decrypted_text.split('\n')[0] == 'CORRECT':
        print('Correct code')
        return decrypted_text
    else:
        print('Wrong code')


encrypt(plain_text, 5, 8, 1, 7)  # plain_text is encrypted and written to logins.txt


with open('logins.txt', 'r', newline='') as logins_file:
    read = logins_file.read()
    print('Decrypting... ' + read)
    data1 = list(map(int, read.split(' ')))

print(decrypt(data1, 5, 8, 1, 7))
