'''
The Hill Cipher is a block cipher that encrypts text using linear algebra. It relies on a square matrix as the key, and the plaintext is divided into blocks of letters. These blocks are then transformed through matrix multiplication, using the key matrix to encrypt the data.

Encryption:
    - Choose a square matrix as the key;
    - The size of the matrix determines the block size;
    - For each block of plaintext:
        - Convert each letter into a numerical value;
        - Perform matrix multiplication with the key matrix and the plaintext block vector;
        - Apply the modulo operation to ensure the result stays within the bounds of the alphabet;
        - Convert the resulting numbers back to letters.
    - Non-alphabetic characters are usually left unchanged.

Decryption:
    - Find the inverse of the key matrix;
    - For each block of ciphertext:
        - Convert each letter into a numerical value;
        - Perform matrix multiplication with the inverse key matrix and the ciphertext block vector;
        - Apply the modulo operation to keep the result within the alphabet's range;
        - Convert the resulting numbers back to letters.

Шифр Хилла - это блочный шифр, основанный на линейной алгебре. Он использует квадратную матрицу в качестве ключа, а текст разбивается на блоки, которые затем шифруются с помощью умножения матриц.

Зашифровка:
    - Выбирается квадратная матрица в качестве ключа;
    - Размер матрицы определяет размер блока;
    - Для каждого блока открытого текста:
        - Каждая буква преобразуется в числовое значение;
        - Выполняется умножение матрицы ключа на вектор блока открытого текста;
        - Применяется операция взятия по модулю, чтобы результат оставался в пределах алфавита;
        - Результирующие числа преобразуются обратно в буквы.
    - Прочие символы обычно остаются без изменений.

Расшифровка:
    - Находится обратная матрица ключа;
    - Для каждого блока зашифрованного текста:
        - Каждая буква преобразуется в числовое значение;
        - Выполняется умножение обратной матрицы ключа на вектор блока зашифрованного текста;
        - Применяется операция взятия по модулю, чтобы результат оставался в пределах алфавита;
        - Результирующие числа преобразуются обратно в буквы.

Hill-salaus on lohkosalaus, joka salaa tekstin lineaarialgebran avulla. Se perustuu neliömatriisiin avaimena, ja selväteksti jaetaan kirjainlohkoihin. Nämä lohkot muunnetaan matriisikertolaskun avulla käyttäen avainmatriisia tiedon salaamiseen.

Salaus:
    - Valitaan neliömatriisi avaimena;
    - Matriisin koko määrittää lohkon koon;
    - Jokaiselle selvätekstin lohkolle:
        - Muutetaan jokainen kirjain numeeriseksi arvoksi;
        - Suoritetaan matriisikertolasku avainmatriisin ja selvätekstivektorin välillä;
        - Sovelletaan modulo-operaatiota, jotta tulos pysyy aakkoston rajoissa;
        - Muutetaan saadut numerot takaisin kirjaimiksi.
    - Muut kuin aakkosmerkit jätetään yleensä muuttumattomiksi.

Purku:
    - Etsitään avainmatriisin käänteismatriisi;
    - Jokaiselle salatekstin lohkolle:
        - Muutetaan jokainen kirjain numeeriseksi arvoksi;
        - Suoritetaan matriisikertolasku käänteisen avainmatriisin ja salatekstivektorin välillä;
        - Sovelletaan modulo-operaatiota, jotta tulos pysyy aakkoston alueella;
        - Muutetaan saadut numerot takaisin kirjaimiksi.
'''

class HillCipher:

    def __init__(self, key_matrix):
        self.key_matrix = key_matrix
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.modulus = 26

    def get_inverted_matrix(self, matrix):
        determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        determinant = determinant % self.modulus
        inverted_determinant = self.modular_inverse(determinant, self.modulus)

        if inverted_determinant is None:
            raise ValueError("Matrix is not invertible!")

        inverted_matrix = [
            [matrix[1][1] * inverted_determinant % self.modulus, (-matrix[0][1]) * inverted_determinant % self.modulus],
            [(-matrix[1][0]) * inverted_determinant % self.modulus, matrix[0][0] * inverted_determinant % self.modulus]
        ]

        return inverted_matrix

    def modular_inverse(self, a, m):
        gcd, inverse, _ = self.extended_gcd(a, m)
        if gcd != 1:
            return None
        else:
            return inverse % m

    def extended_gcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            gcd, x1, y1 = self.extended_gcd(b % a, a)
            x = y1 - (b // a) * x1
            y = x1
        return gcd, x, y

    def text_to_numbers(self, text):
        numbers = []
        for character in text.upper():
            if character.isalpha():
                numbers.append(self.alphabet.index(character))
        return numbers

    def numbers_to_text(self, numbers):
        text = ""
        for number in numbers:
            text += self.alphabet[number]
        return text

    def encrypt(self, text):
        plaintext_numbers = self.text_to_numbers(text)
        ciphertext_numbers = []

        if len(plaintext_numbers) % 2 != 0:
            plaintext_numbers.append(self.alphabet.index('X'))  # Padding with 'X' if necessary
        
        for i in range(0, len(plaintext_numbers), 2):
            block = plaintext_numbers[i:i + 2]
            encrypted_block = [
                (self.key_matrix[0][0] * block[0] + self.key_matrix[0][1] * block[1]) % self.modulus,
                (self.key_matrix[1][0] * block[0] + self.key_matrix[1][1] * block[1]) % self.modulus
            ]
            ciphertext_numbers.extend(encrypted_block)

        return self.numbers_to_text(ciphertext_numbers)

    def decrypt(self, text):
        ciphertext_numbers = self.text_to_numbers(text)
        plaintext_numbers = []

        inverse_key = self.get_inverted_matrix(self.key_matrix)

        for i in range(0, len(ciphertext_numbers), 2):
            block = ciphertext_numbers[i:i + 2]
            decrypted_block = [
                (inverse_key[0][0] * block[0] + inverse_key[0][1] * block[1]) % self.modulus,
                (inverse_key[1][0] * block[0] + inverse_key[1][1] * block[1]) % self.modulus
            ]
            plaintext_numbers.extend(decrypted_block)
        
        decrypted_text = self.numbers_to_text(plaintext_numbers)

        return decrypted_text.replace('X', '')

if __name__ == "__main__":

    key_matrix = [  [5, 8], 
                    [17, 3]
            ]

    cipher = HillCipher(key_matrix)

    plaintext = "HELLO, WORLD!"
    encrypted_text = cipher.encrypt(plaintext)
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = cipher.decrypt(encrypted_text)
    print(f"Decrypted text: {decrypted_text}")