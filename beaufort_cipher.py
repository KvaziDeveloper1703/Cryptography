'''
The Beaufort cipher is a polyalphabetic substitution cipher that is closely related to the Vigenère cipher, but uses a different encryption formula.

Encryption:
    - Use a repeating keyword to match the length of the plaintext;
    - For each letter in the plaintext:
        - Find the corresponding letter in the keyword;
        - The Beaufort table is used to find the encrypted letter;
    - Non-letter characters are usually left unchanged;
    - The result is a cipher that is symmetric - the same process is used for decryption.

Decryption:
    - Same as encryption;
    - Apply the Beaufort formula using the keyword and the ciphertext to retrieve the original message.

Шифр Бофорта - это полиалфавитный шифр подстановки, тесно связанный с шифром Виженера, но использующий иную формулу шифрования.

Зашифровка:
    - Используется повторяющееся ключевое слово, длина которого соответствует длине открытого текста;
    - Для каждой буквы открытого текста:
        - Определяется соответствующая буква ключа;
        - По таблице Бофорта находится зашифрованная буква;
    - Неалфавитные символы, как правило, не изменяются;
    - Шифр симметричен - тот же процесс используется для расшифровки.

Расшифровка:
    - Процесс идентичен зашифровке;
    - Используется та же формула с тем же ключом для восстановления исходного сообщения.
'''

class BeaufortCipher:
    def __init__(self, key: str):
        self.alphabet = [
            'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        self.alphabet_size = 26
        self.key = key.upper()

        self.letter_to_index = {}
        self.index_to_letter = {}

        index = 0
        for character in self.alphabet:
            self.letter_to_index[character] = index
            self.index_to_letter[index] = character
            index += 1

    def encode(self, text: str) -> str:
        result = []
        key_length = len(self.key)
        key_index = 0

        for character in text.upper():
            if character in self.letter_to_index:
                character_index = self.letter_to_index[character]
                key_character = self.key[key_index % key_length]
                key_character_index = self.letter_to_index[key_character]

                encoded_index = (key_character_index - character_index + self.alphabet_size) % self.alphabet_size
                encoded_character = self.index_to_letter[encoded_index]
                result.append(encoded_character)

                key_index += 1
            else:
                result.append(character)

        return ''.join(result)

    def decode(self, text: str) -> str:
        return self.encode(text)

if __name__ == "__main__":
    cipher = BeaufortCipher(key="KEYWORD")

    plain_text = "HELLO, WORLD!"
    encoded_text = cipher.encode(plain_text)

    print(f"Plain text:    {plain_text}")
    print(f"Encoded text:  {encoded_text}")

    decoded_text = cipher.decode(encoded_text)
    print(f"Decoded text:  {decoded_text}")