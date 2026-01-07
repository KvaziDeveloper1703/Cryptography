'''
The Gronsfeld Cipher is a variation of the Vigenère Cipher, where the shifts are determined by a numerical key. The key is repeated or truncated to match the length of the plaintext, and each digit of the key is used to shift the corresponding letter of the plaintext.

Encryption:
    - Choose a numerical keyword;
    - Repeat or truncate the keyword to match the length of the plaintext;
    - For each letter in the plaintext:
        - Determine its position in the alphabet;
        - Use the corresponding digit of the keyword to determine the shift value;
        - Shift the position of the plaintext letter by the value of the corresponding digit;
        - If the shift exceeds the alphabet's boundaries, wrap around to the beginning;
        - Replace the letter with the one at the new position.
    - Non-alphabetic characters are usually left unchanged.

Decryption:
    - Repeat or truncate the keyword to match the length of the ciphertext;
    - For each letter in the ciphertext:
        - Determine its position in the alphabet;
        - Use the corresponding digit of the keyword to reverse the shift;
        - Subtract the corresponding digit from the position of the letter;
        - Wrap around if necessary to stay within the alphabet's boundaries;
        - Replace the encrypted letter with the one at the computed position.

Шифр Гронсфельда - это вариация шифра Виженера, где сдвиги определяются числовым ключом. Ключ повторяется или обрезается до длины открытого текста, и каждая цифра ключа используется для сдвига соответствующей буквы текста.

Зашифровка:
    - Выбирается числовое ключевое слово;
    - Ключ повторяется или обрезается до длины открытого текста;
    - Для каждой буквы открытого текста:
        - Определяется её позиция в алфавите;
        - Используется соответствующая цифра ключа для определения величины сдвига;
        - Позиция буквы открытого текста сдвигается на значение соответствующей цифры;
        - Если сдвиг выходит за границы алфавита, осуществляется переход к его началу;
        - Буква заменяется на ту, что находится на новой позиции.
    - Прочие символы обычно остаются без изменений.

Расшифровка:
    - Ключ повторяется или обрезается до длины зашифрованного текста;
    - Для каждой буквы зашифрованного текста:
        - Определяется её позиция в алфавите;
        - Используется соответствующая цифра ключа для обратного сдвига;
        - Из позиции буквы вычитается соответствующая цифра ключа;
        - Если результат выходит за границы алфавита, выполняется переход к его концу;
        - Буква заменяется на ту, что находится на вычисленной позиции.

Gronsfeldin salaus on Vigenère-salauksen muunnelma, jossa siirrot määräytyvät numeerisen avaimen perusteella. Avain toistetaan tai lyhennetään vastaamaan selvätekstin pituutta, ja kutakin avaimen numeroa käytetään vastaavan selvätekstin kirjaimen siirtämiseen.

Salaus:
    - Valitaan numeerinen avainsana;
    - Avainsana toistetaan tai lyhennetään vastaamaan selvätekstin pituutta;
    - Jokaiselle selvätekstin kirjaimelle:
        - Määritetään sen sijainti aakkostossa;
        - Käytetään avaimen vastaavaa numeroa siirron suuruuden määrittämiseen;
        - Siirretään selvätekstin kirjaimen sijaintia vastaavan numeron verran;
        - Jos siirto ylittää aakkoston rajat, kierretään aakkoston alkuun;
        - Korvataan kirjain sillä kirjaimella, joka on uudessa sijainnissa.
    - Muut kuin aakkosmerkit jätetään yleensä muuttumattomiksi.

Purku:
    - Avainsana toistetaan tai lyhennetään vastaamaan salatekstin pituutta;
    - Jokaiselle salatekstin kirjaimelle:
        - Määritetään sen sijainti aakkostossa;
        - Käytetään avaimen vastaavaa numeroa siirron kääntämiseen;
        - Vähennetään vastaava numero kirjaimen sijainnista;
        - Kierretään tarvittaessa, jotta pysytään aakkoston rajojen sisällä;
        - Korvataan salattu kirjain sillä kirjaimella, joka on lasketussa sijainnissa.
'''

class GronsfeldCipher:

    def __init__(self, keyword: str):
        self.keyword = []
        for digit in keyword:
            self.keyword.append(int(digit))

    def shift_character(self, character: str, shift: int, encrypt: bool) -> str:
        if character.isalpha():
            alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            character = character.upper()

            current_position = alphabet.index(character)

            if encrypt:
                new_position = (current_position + shift) % 26
            else:
                new_position = (current_position - shift) % 26

            return alphabet[new_position]

        return character

    def format_text(self, text: str) -> str:
        formatted_text = []
        for character in text:
            if character.isalpha():
                formatted_text.append(character)

        return ''.join(formatted_text)

    def encrypt(self, text: str) -> str:
        text = self.format_text(text)
        ciphertext = []

        full_repeats = len(text) // len(self.keyword)
        remainder = len(text) % len(self.keyword)
        repeated_keyword = self.keyword * full_repeats
        repeated_keyword += self.keyword[:remainder]
        keyword_repeated = repeated_keyword

        for i, character in enumerate(text):
            shift = keyword_repeated[i]
            encrypted_character = self.shift_character(character, shift, encrypt=True)
            ciphertext.append(encrypted_character)

        return ''.join(ciphertext)

    def decrypt(self, text: str) -> str:
        ciphertext = self.format_text(text)
        plaintext = []

        full_repeats = len(ciphertext) // len(self.keyword)
        remainder = len(ciphertext) % len(self.keyword)
        repeated_keyword = self.keyword * full_repeats
        repeated_keyword += self.keyword[:remainder]
        keyword_repeated = repeated_keyword

        for i, character in enumerate(ciphertext):
            shift = keyword_repeated[i]
            decrypted_char = self.shift_character(character, shift, encrypt=False)
            plaintext.append(decrypted_char)

        return ''.join(plaintext)

if __name__ == "__main__":

    keyword = "1703"
    cipher = GronsfeldCipher(keyword)

    plaintext = "HELLO WORLD"
    encrypted_text = cipher.encrypt(plaintext)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted text: {encrypted_text}")
    
    decrypted_text = cipher.decrypt(encrypted_text)

    print(f"Decrypted text: {decrypted_text}")