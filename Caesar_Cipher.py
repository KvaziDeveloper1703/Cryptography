"""
The Caesar Cipher is a substitution cipher that encrypts text by shifting each letter in the alphabet by a fixed number of positions. The shift is uniform for all characters in the text.

Encryption:
    - Choose a key;
    - For each letter in the plaintext:
        - Determine its position in the alphabet;
        - Add the key to this position;
        - Wrap around if the shift exceeds the alphabet boundaries;
        - Replace the letter with the one at the new position.
    - Non-alphabetic characters are usually left unchanged.

Decryption:
    - Determine the position of the encrypted letter in the alphabet;
    - Subtract the key from this position;
    - Wrap around if the result is outside the alphabet boundaries;
    - Replace the encrypted letter with the one at the calculated position.

Шифр Цезаря - это подстановочный шифр, который шифрует текст, сдвигая каждую букву алфавита на фиксированное количество позиций. Сдвиг одинаков для всех символов текста.

Зашифровка:
    - Выбирается ключ;
    - Для каждой буквы открытого текста:
        - Определите её позицию в алфавите;
        - Прибавьте к этой позиции ключ;
        - Если сдвиг выходит за границы алфавита, выполните переход к его началу;
        - Замените букву на ту, что находится на новой позиции.
    - Остальные символы обычно остаются без изменений.

Расшифровка:
    - Определите позицию зашифрованной буквы в алфавите;
    - Вычтите из неё значение ключа;
    - Если результат выходит за границы алфавита, выполните переход к его концу;
    - Замените зашифрованную букву на ту, что находится на вычисленной позиции.

Caesarin salaus on korvaussalaus, joka salaa tekstin siirtämällä jokaista aakkoston kirjainta kiinteän määrän verran. Siirto on sama kaikille tekstin merkeille.

Salaus:
    - Valitaan avain;
    - Jokaiselle selvätekstin kirjaimelle:
        - Määritetään sen sijainti aakkostossa;
        - Lisätään tähän sijaintiin avain;
        - Kierretään aakkoston alkuun, jos siirto ylittää aakkoston rajat;
        - Korvataan kirjain sillä kirjaimella, joka on uudessa sijainnissa.
    - Muut kuin aakkosmerkit jätetään yleensä muuttumattomiksi.

Purku:
    - Määritetään salatun kirjaimen sijainti aakkostossa;
    - Vähennetään tästä sijainnista avain;
    - Kierretään tarvittaessa aakkoston loppuun, jos tulos menee aakkoston rajojen ulkopuolelle;
    - Korvataan salattu kirjain sillä kirjaimella, joka on lasketussa sijainnissa.
"""

class CaesarCipher:
    
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

    cipher = CaesarCipher(shift=3)

    plain_text = "HELLO, WORLD!"
    encoded_text = cipher.encode(plain_text)

    print(f"Plain text: {plain_text}")
    print(f"Encoded text: {encoded_text}")

    decoded_text = cipher.decode(encoded_text)
    print(f"Decoded text: {decoded_text}")