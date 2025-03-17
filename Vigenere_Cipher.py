"""
The Vigenère Cipher is a polyalphabetic substitution cipher that encrypts text using a keyword-based shifting mechanism. Each letter in the plaintext is shifted by an amount determined by the corresponding letter in the keyword.

Encryption:
+ Choose a keyword;
+ Extend or truncate the keyword to match the length of the plaintext;
+ For each letter in the plaintext:
    + Determine its position in the alphabet;
    + Identify the corresponding letter in the keyword and its position in the alphabet;
    + Shift the plaintext letter by the value of the keyword letter;
    + Wrap around if the shift exceeds the alphabet boundaries;
    + Replace the letter with the one at the new position;
+ Non-alphabetic characters are usually left unchanged.

Decryption:
+ Extend or truncate the keyword to match the length of the ciphertext;
+ For each letter in the ciphertext:
    + Determine its position in the alphabet;
    + Identify the corresponding letter in the keyword and its position in the alphabet;
    + Reverse the shift by subtracting the keyword letter's value;
    + Wrap around if necessary to stay within the alphabet;
    + Replace the encrypted letter with the one at the computed position.

Шифр Виженера — это полиалфавитный подстановочный шифр, который шифрует текст, используя механизм сдвига на основе ключевого слова. Каждая буква открытого текста сдвигается на значение, определяемое соответствующей буквой ключа.

Зашифровка:
+ Выбирается ключевое слово;
+ Ключ повторяется или обрезается до длины открытого текста;
+ Для каждой буквы открытого текста:
    + Определите её позицию в алфавите;
    + Найдите соответствующую букву ключа и её позицию в алфавите;
    + Сдвиньте букву открытого текста на значение буквы ключа;
    + Если сдвиг выходит за границы алфавита, выполните переход к его началу;
    + Замените букву на ту, что находится на новой позиции;
+ Остальные символы обычно остаются без изменений.

Расшифровка:
+ Повторите или обрежьте ключевое слово до длины зашифрованного текста;
+ Для каждой буквы зашифрованного текста:
    + Определите её позицию в алфавите;
    + Найдите соответствующую букву ключа и её позицию в алфавите;
    + Обратный сдвиг выполняется вычитанием значения буквы ключа;
    + Если результат выходит за границы алфавита, выполните переход к его концу;
    + Замените зашифрованную букву на ту, что находится на вычисленной позиции.
"""

class VigenereCipher:

    def __init__(self, keyword: str):

        self.keyword = keyword.upper()
        
        self.alphabet = {
            'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8,
            'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
            'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22,
            'W': 23, 'X': 24, 'Y': 25, 'Z': 26
        }

        self.reverse_alphabet = {
            1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H',
            9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O',
            16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V',
            23: 'W', 24: 'X', 25: 'Y', 26: 'Z'
        }

        self.alphabet_size = 26

    def extend_keyword(self, text: str) -> str:
        repetitions_needed = len(text) // len(self.keyword)
        remainder = len(text) % len(self.keyword)
        keyword_extended = self.keyword * (repetitions_needed + 1)
        keyword_extended = keyword_extended[:len(text)]
        return keyword_extended

    def shift_character(self, character: str, shift: int, encrypt: bool) -> str:
        if character.upper() in self.alphabet:
            position = self.alphabet[character.upper()]
            shift = shift if encrypt else -shift
            new_position = (position + shift - 1) % self.alphabet_size + 1

            if character.isupper():
                return self.reverse_alphabet[new_position]
            else:
                return self.reverse_alphabet[new_position].lower()

        return character

    def process_text(self, text: str, encrypt: bool) -> str:
        keyword_extended = self.extend_keyword(text)
        result = []
        keyword_index = 0

        for character in text:
            if character.isalpha():
                shift = self.alphabet[keyword_extended[keyword_index].upper()]
                result.append(self.shift_character(character, shift, encrypt))
                keyword_index += 1
            else:
                result.append(character)
        
        return "".join(result)

    def encrypt(self, text: str) -> str:
        result = []
        keyword_extended = self.extend_keyword(text)
        keyword_index = 0

        for character in text:
            if character.isalpha():
                shift = self.alphabet[keyword_extended[keyword_index].upper()]
                encrypted_character = self.shift_character(character, shift, encrypt=True)
                result.append(encrypted_character)
                keyword_index += 1
            else:
                result.append(character)

        return ''.join(result)

    def decrypt(self, text: str) -> str:
        result = []
        keyword_extended = self.extend_keyword(text)
        keyword_index = 0

        for character in text:
            if character.isalpha():
                shift = self.alphabet[keyword_extended[keyword_index].upper()]
                decrypted_chararacter = self.shift_character(character, shift, encrypt=False)
                result.append(decrypted_chararacter)
                keyword_index += 1
            else:
                result.append(character)

        return ''.join(result)

if __name__ == "__main__":

    keyword = "KEY"
    cipher = VigenereCipher(keyword)

    plaintext = "HELLO, WORLD!"
    encrypted_text = cipher.encrypt(plaintext)

    print(f"Plain text: {plaintext}")
    print(f"Encrypted text: {encrypted_text}")

    decrypted_text = cipher.decrypt(encrypted_text)

    print(f"Decrypted text: {decrypted_text}")