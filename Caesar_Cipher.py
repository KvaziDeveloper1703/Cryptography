"""
The Caesar Cipher is one of the simplest and most well-known methods of encrypting text. It works by replacing each letter of the alphabet with another letter, located a fixed number of positions ahead or behind. The shift is consistent for all characters in the text.

Algorithm:
+ Choose a key;
+ For each letter in the plaintext:
    + Determine its position in the alphabet;
    + Shift the position by the value of the key;
    + If the shift exceeds the alphabet boundaries, wrap around to the beginning;
+ Replace the letter with the one at the computed position;
+ Other characters are usually left unchanged.

Шифр Цезаря — это один из самых простых и известных методов шифрования текста. Он основан на замене каждой буквы алфавита другой буквой, расположенной на определённое фиксированное количество позиций вперед или назад. Это сдвиг одинаков для всех символов текста.

Алгоритм работы:
+ Выбирается ключ;
+ Для каждой буквы открытого текста:
    + Определяется её позиция в алфавите;
    + Позиция сдвигается на значение ключа;
    + Если сдвиг выходит за границы алфавита, переход осуществляется к его началу;
+ Буква заменяется на новую, находящуюся на вычисленной позиции;
+ Остальные символы обычно остаются без изменений.
"""

class Caesar_Cipher:
    
    def __init__(self, shift: int):

        self.shift = shift

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

    def shift_character(self, character: str, shift: int) -> str:
        character = character.upper()
        if character in self.alphabet:
            current_position = self.alphabet[character]
            new_position = (current_position + shift - 1) % 26 + 1
            return self.reverse_alphabet[new_position]
        return character

    def encode(self, text: str) -> str:
        encoded_text = []
        for character in text:
            if character.isalpha():
                shifted_character = self.shift_character(character, self.shift)
                encoded_text.append(shifted_character)
            else:
                encoded_text.append(character)
        return ''.join(encoded_text)

    def decode(self, text: str) -> str:
        decoded_text = []
        for character in text:
            if character.isalpha():
                shifted_character = self.shift_character(character, -self.shift)
                decoded_text.append(shifted_character)
            else:
                decoded_text.append(character)
        return ''.join(decoded_text)

if __name__ == "__main__":

    cipher = Caesar_Cipher(shift=3)

    plain_text = "HELLO, WORLD!"
    encoded_text = cipher.encode(plain_text)

    print(f"Plain text: {plain_text}")
    print(f"Encoded text: {encoded_text}")

    decoded_text = cipher.decode(encoded_text)
    print(f"Decoded text: {decoded_text}")
