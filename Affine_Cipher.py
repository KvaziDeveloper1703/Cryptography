"""
The Affine Cipher is a substitution cipher that encrypts text using a linear transformation. Each letter in the alphabet is replaced with another letter based on a mathematical rule. The transformation is consistent for all characters in the text.

Encryption:
    - Choose two keys: a and b;
    - Ensure that a is coprime with the size of the alphabet;
    - For each letter in the plaintext:
        - Determine its position in the alphabet;
        - Multiply this position by the first key a;
        - Add the second key b to the result;
        - Divide the total by the size of the alphabet and take the remainder to ensure the result stays within the alphabet range;
        - Replace the letter with the one at the new position.
    - Non-alphabetic characters are usually left unchanged.

Decryption:
    - Determine the position of the encrypted letter in the alphabet;
    - Subtract the second key b from this position;
    - Multiply the result by the modular inverse of the first key a, ensuring the result wraps around if it exceeds the alphabet size;
    - Replace the encrypted letter with the one at the calculated position.

Афинный шифр - это подстановочный шифр, который шифрует текст с использованием линейного преобразования. Каждая буква алфавита заменяется другой буквой на основе определенного правила. Преобразование одинаково для всех символов текста.

Зашифровка:
    - Выбираются два ключа: a и b;
    - Убедитесь, что a взаимно простое с размером алфавита;
    - Для каждой буквы открытого текста:
        - Определите её позицию в алфавите;
        - Умножьте эту позицию на первый ключ a;
        - Прибавьте второй ключ b к полученному результату;
        - Разделите итог на размер алфавита и возьмите остаток;
        - Замените букву на ту, что находится на новой позиции.
    - Остальные символы обычно остаются без изменений.

Расшифровка:
    - Найдите позицию зашифрованной буквы в алфавите;
    - Вычтите второй ключ b из этой позиции;
    - Умножьте результат на мультипликативно обратное значение первого ключа a, следя за тем, чтобы результат оставался в пределах алфавита;
    - Замените зашифрованную букву на ту, что находится на вычисленной позиции.

Affiininen salaus on korvaussalaus, joka salaa tekstin lineaarisen muunnoksen avulla. Jokainen aakkoston kirjain korvataan toisella kirjaimella ennalta määrätyn säännön mukaisesti. Muunnos on sama kaikille tekstin merkeille.

Salaus:
    - Valitaan kaksi avainta: a ja b;
    - Varmistetaan, että a on suhteellisesti alkuluku aakkoston koon kanssa;
    - Jokaiselle selvätekstin kirjaimelle:
        - Määritetään sen sijainti aakkostossa;
        - Kerrotaan tämä sijainti ensimmäisellä avaimella a;
        - Lisätään saatuun tulokseen toinen avain b;
        - Jaetaan tulos aakkoston koolla ja otetaan jakojäännös;
        - Korvataan kirjain sillä kirjaimella, joka on uudessa sijainnissa.
    - Muut merkit jätetään yleensä muuttumattomiksi.

Purku:
    - Määritetään salatun kirjaimen sijainti aakkostossa;
    - Vähennetään tästä sijainnista toinen avain b;
    - Kerrotaan tulos ensimmäisen avaimen a multiplikatiivisella käänteisluvulla siten, että tulos pysyy aakkoston rajoissa;
    - Korvataan salattu kirjain sillä kirjaimella, joka on lasketussa sijainnissa.
"""

class AffineCipher:

    def __init__(self, a: int, b: int):

        if self.greatest_common_divisor(a, 26) != 1:
            raise ValueError("The coefficient 'a' must be relatively prime to 26!")

        self.a = a
        self.b = b
        self.m = 26

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

    def greatest_common_divisor(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return a

    def multiplicative_inverse(self, a: int, m: int) -> int:
        for number in range(1, m):
            if (a * number) % m == 1:
                return number
        raise ValueError("Inverse element not found!")

    def encode_character(self, character: str) -> str:
        if character.isalpha():
            character = character.upper()
            position = self.alphabet[character]
            new_position = (self.a * position + self.b) % self.m
            return self.reverse_alphabet[new_position]
        return character

    def decode_character(self, character: str) -> str:
        if character.isalpha():
            chararacter = character.upper()
            position = self.alphabet[character]
            inverted_a = self.multiplicative_inverse(self.a, self.m)
            new_position = (inverted_a * (position - self.b)) % self.m
            return self.reverse_alphabet[new_position]
        return character

    def encode(self, text: str) -> str:
        encoded_text = []
        for character in text:
            encoded_text.append(self.encode_character(character))
        return ''.join(encoded_text)

    def decode(self, text: str) -> str:
        decoded_text = []
        for character in text:
            decoded_text.append(self.decode_character(character))
        return ''.join(decoded_text)

if __name__ == "__main__":

    a, b = 5, 8
    cipher = AffineCipher(a, b)
    
    plain_text = "HELLO, WORLD!"
    encoded_text = cipher.encode(plain_text)
    
    print(f"Plain text: {plain_text}")
    print(f"Encoded text: {encoded_text}")
    
    decoded_text = cipher.decode(encoded_text)

    print(f"Decoded text: {decoded_text}")