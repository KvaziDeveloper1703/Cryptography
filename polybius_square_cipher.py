'''
The Polybius cipher is a substitution cipher that encrypts each letter as a pair of digits based on its position in a fixed 5×5 grid.

Encryption:
    - Use a 5×5 grid filled with the letters of the alphabet;
    - Number the rows and columns from 1 to 5;
    - For each letter in the plaintext:
        - Locate the letter in the grid;
        - Replace it with its row and column numbers.
    - The result is a series of digit pairs;
    - Non-letter characters are skipped or processed separately.

Decryption:
    - Split the ciphertext into pairs of digits;
    - For each pair:
        - The first digit is the row number, the second is the column number;
        - Find the letter located at that position in the 5×5 grid.
    - Combine the letters to recover the original message.

Шифр Полибия - это подстановочный шифр, в котором каждая буква заменяется парой цифр, указывающих её координаты в постоянной таблице 5×5.

Зашифровка:
    - Используется таблица 5×5, заполненная буквами алфавита;
    - Строки и столбцы нумеруются от 1 до 5;
    - Для каждой буквы открытого текста:
        - Определяется её место в таблице;
        - Буква заменяется на пару цифр: номер строки и номер столбца.
    - В результате получается последовательность пар чисел;
    - Неалфавитные символы пропускаются или обрабатываются отдельно.

Расшифровка:
    - Шифртекст делится на пары цифр;
    - Для каждой пары:
        - Первая цифра - номер строки, вторая - номер столбца;
        - Определяется буква, находящаяся в данной позиции таблицы 5×5.
    - Из этих букв собирается исходное сообщение.

Polybiuksen neliö on korvaussalaus, jossa jokainen kirjain salataan numeroparina sen sijainnin perusteella kiinteässä 5×5-ruudukossa.

Salaus:
    - Käytetään 5×5-ruudukkoa, joka on täytetty aakkoston kirjaimilla;
    - Numeroidaan rivit ja sarakkeet luvuilla 1–5;
    - Jokaiselle selvätekstin kirjaimelle:
        - Etsitään kirjaimen sijainti ruudukossa;
        - Korvataan kirjain sen rivi- ja sarakenumeroilla.
    - Tuloksena on numerosarjoista koostuva parijono;
    - Muut kuin kirjaimet ohitetaan tai käsitellään erikseen.

Purku:
    - Jaetaan salateksti numeropareihin;
    - Jokaiselle parille:
        - Ensimmäinen numero on rivinumero ja toinen sarakenumero;
        - Etsitään kirjain, joka sijaitsee kyseisessä kohdassa 5×5-ruudukossa.
    - Yhdistetään kirjaimet alkuperäisen viestin palauttamiseksi.
'''

class PolybiusCipher:
    def __init__(self):
        self.size = 5
        self.alphabet = [
            'A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I',
            'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
        ]

        self.grid = self.create_grid()
        self.reverse_grid = {}
        for letter in self.grid:
            coordinates = self.grid[letter]
            self.reverse_grid[coordinates] = letter

    def create_grid(self) -> dict:
        grid = {}
        row, column = 1, 1

        for letter in self.alphabet:
            grid[letter] = (row, column)
            column += 1
            if column > self.size:
                column = 1
                row += 1

        return grid

    def encode(self, text: str) -> str:
        result = []

        for character in text.upper():
            if character == 'J':
                character = 'I'

            if character in self.grid:
                row, column = self.grid[character]
                result.append(f"{row}{column}")
            else:
                result.append(character)

        return ' '.join(result)

    def decode(self, code: str) -> str:
        result = []
        i = 0

        code = code.replace(" ", "")

        while i < len(code):
            current_char_is_digit = code[i].isdigit()

            next_index_in_bounds = (i + 1) < len(code)

            next_char_is_digit = False
            if next_index_in_bounds:
                next_char_is_digit = code[i + 1].isdigit()

            if current_char_is_digit and next_index_in_bounds and next_char_is_digit:
                row = int(code[i])
                column = int(code[i + 1])
                letter = self.reverse_grid.get((row, column), '')
                result.append(letter)
                i += 2
            else:
                result.append(code[i])
                i += 1

        return ''.join(result)

if __name__ == "__main__":
    cipher = PolybiusCipher()

    plain_text = "HELLO, WORLD!"
    encoded_text = cipher.encode(plain_text)

    print(f"Plain text:    {plain_text}")
    print(f"Encoded text:  {encoded_text}")

    decoded_text = cipher.decode(encoded_text)
    print(f"Decoded text:  {decoded_text}")