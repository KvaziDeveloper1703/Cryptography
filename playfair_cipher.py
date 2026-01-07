'''
The Playfair Cipher is a digraph substitution cipher that encrypts text using a 5x5 matrix created from a keyword. Each pair of letters in the plaintext is encrypted based on the position of the letters in the matrix. If the pair consists of two identical letters, a filler letter is inserted between them.

Encryption:
    - Choose a keyword;
    - Remove duplicate letters from the keyword and append the remaining letters of the alphabet (excluding 'J') to complete the 5x5 matrix;
    - For each pair of letters in the plaintext:
        - If the letters are the same, insert a filler letter between them;
        - Locate the letters in the matrix:
            - If the letters appear in the same row, shift each letter to the right;
            - If the letters appear in the same column, shift each letter down;
            - If the letters form a rectangle, replace each letter with the one on the same row but in the opposite corner of the rectangle.
        - Replace each letter with the one at the new position.
    - Non-alphabetic characters are usually left unchanged.

Decryption:
    - For each pair of letters in the ciphertext:
        - Locate the letters in the matrix:
            - If the letters appear in the same row, shift each letter to the left;
            - If the letters appear in the same column, shift each letter up;
            - If the letters form a rectangle, replace each letter with the one on the same row but in the opposite corner of the rectangle.
        - Replace each letter with the one at the new position.

Шифр Плейфера - это шифр подстановки для пар букв, который использует таблицу 5x5, созданную на основе ключевого слова. Каждая пара букв открытого текста шифруется в зависимости от их положения в таблице. Если пара состоит из одинаковых букв, между ними вставляется вспомогательная буква.

Зашифровка:
    - Выбирается ключевое слово;
    - Из ключа удаляются повторяющиеся буквы, а оставшиеся буквы алфавита (кроме 'J') добавляются для формирования таблицы 5x5;
    - Для каждой пары букв открытого текста:
        - Если буквы одинаковые, между ними вставляется вспомогательная буква;
        - Найдите буквы в таблице:
            - Если буквы находятся в одной строке, сдвигайте каждую букву вправо;
            - Если буквы находятся в одном столбце, сдвигайте каждую букву вниз;
            - Если буквы образуют прямоугольник, замените каждую букву на ту, что находится на противоположных углах прямоугольника в таблице.
        - Замените каждую букву на букву, находящуюся на новой позиции.
    - Прочие символы обычно остаются без изменений.

Расшифровка:
    - Для каждой пары букв зашифрованного текста:
        - Найдите буквы в таблице:
            - Если буквы находятся в одной строке, сдвигайте каждую букву влево;
            - Если буквы находятся в одном столбце, сдвигайте каждую букву вверх;
            - Если буквы образуют прямоугольник, замените каждую букву на ту, что находится на противоположных углах прямоугольника в таблице.
        - Замените каждую букву на букву, находящуюся на новой позиции.

Playfair-salaus on digrafinen korvaussalaus, joka salaa tekstin 5×5-matriisin avulla. Matriisi muodostetaan avainsanasta, ja selvätekstin kirjainparit salataan kirjainten sijainnin perusteella. Jos pari koostuu kahdesta samasta kirjaimesta, niiden väliin lisätään täytekirjain.

Salaus:
    - Valitaan avainsana;
    - Poistetaan avainsanasta toistuvat kirjaimet ja lisätään aakkoston jäljellä olevat kirjaimet (poislukien J) 5×5-matriisin täydentämiseksi;
    - Jokaiselle selvätekstin kirjainparille:
        - Jos kirjaimet ovat samat, lisätään niiden väliin täytekirjain;
        - Etsitään kirjainten sijainti matriisissa:
            - Jos kirjaimet ovat samalla rivillä, kumpaakin siirretään yhden askeleen verran oikealle;
            - Jos kirjaimet ovat samassa sarakkeessa, kumpaakin siirretään yhden askeleen verran alaspäin;
            - Jos kirjaimet muodostavat suorakulmion, kumpikin kirjain korvataan samalla rivillä olevalla mutta suorakulmion vastakkaisessa kulmassa sijaitsevalla kirjaimella.
        - Korvataan kirjaimet niiden uusissa sijainneissa olevilla kirjaimilla.
    - Muut kuin aakkosmerkit jätetään yleensä muuttumattomiksi.

Purku:
    - Jokaiselle salatekstin kirjainparille:
    - Etsitään kirjainten sijainti matriisissa:
        - Jos kirjaimet ovat samalla rivillä, kumpaakin siirretään yhden askeleen verran vasemmalle;
        - Jos kirjaimet ovat samassa sarakkeessa, kumpaakin siirretään yhden askeleen verran ylöspäin;
        - Jos kirjaimet muodostavat suorakulmion, kumpikin kirjain korvataan samalla rivillä olevalla mutta suorakulmion vastakkaisessa kulmassa sijaitsevalla kirjaimella;
        - Korvataan kirjaimet niiden lasketuissa sijainneissa olevilla kirjaimilla.
'''

class PlayfairCipher:

    def __init__(self, keyword: str):

        self.keyword = keyword.upper().replace('J', 'I')
        self.alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
        self.matrix = self.create_matrix()

    def create_matrix(self):
        seen = set()
        matrix = []

        for character in self.keyword:
            character = character.upper()

            if character not in seen:
                seen.add(character)
                matrix.append(character)

        for character in self.alphabet:
            if character not in seen:
                seen.add(character)
                matrix.append(character)

        rows = []
        for i in range(0, 25, 5):
            row = matrix[i:i + 5]
            rows.append(row)

        return rows

    def find_position(self, character: str):
        for row_index, row in enumerate(self.matrix):
            if character in row:
                return row_index, row.index(character)
        raise ValueError(f"Character {character} not found in matrix!")

    def format_text(self, text: str):
        text = text.upper().replace('J', 'I')
        formatted_text = []

        text = ''.join([c for c in text if c.isalpha()])

        i = 0
        while i < len(text):
            if i + 1 < len(text):
                if text[i] == text[i + 1]:
                    formatted_text.append(text[i] + 'X')
                    i += 1
                else:
                    formatted_text.append(text[i] + text[i + 1])
                    i += 2
            else:
                formatted_text.append(text[i] + 'X')
                i += 1
        return formatted_text

    def encrypt(self, text: str) -> str:
        formatted_text = self.format_text(text)
        ciphertext = []

        for pair in formatted_text:
            row_1, column_1 = self.find_position(pair[0])
            row_2, column_2 = self.find_position(pair[1])

            if row_1 == row_2:
                next_column_1 = (column_1 + 1) % 5
                next_column_2 = (column_2 + 1) % 5
                new_char_1 = self.matrix[row_1][next_column_1]
                new_char_2 = self.matrix[row_2][next_column_2]
                ciphertext.append(new_char_1 + new_char_2)

            elif column_1 == column_2:
                next_row_1 = (row_1 + 1) % 5
                next_row_2 = (row_2 + 1) % 5
                new_char_1 = self.matrix[next_row_1][column_1]
                new_char_2 = self.matrix[next_row_2][column_2]
                ciphertext.append(new_char_1 + new_char_2)

            else:
                new_char_1 = self.matrix[row_1][column_2]
                new_char_2 = self.matrix[row_2][column_1]
                ciphertext.append(new_char_1 + new_char_2)

        return ''.join(ciphertext)

    def decrypt(self, text: str) -> str:
        formatted_text = []
        plaintext = []

        i = 0
        while i < len(text):
            formatted_text.append(text[i:i+2])
            i += 2

        for pair in formatted_text:
            row_1, column_1 = self.find_position(pair[0])
            row_2, column_2 = self.find_position(pair[1])

            if row_1 == row_2:
                next_column_1 = (column_1 - 1) % 5
                next_column_2 = (column_2 - 1) % 5
                new_char_1 = self.matrix[row_1][next_column_1]
                new_char_2 = self.matrix[row_2][next_column_2]
                plaintext.append(new_char_1 + new_char_2)

            elif column_1 == column_2:
                next_row_1 = (row_1 - 1) % 5
                next_row_2 = (row_2 - 1) % 5
                new_char_1 = self.matrix[next_row_1][column_1]
                new_char_2 = self.matrix[next_row_2][column_2]
                plaintext.append(new_char_1 + new_char_2)

            else:
                new_char_1 = self.matrix[row_1][column_2]
                new_char_2 = self.matrix[row_2][column_1]
                plaintext.append(new_char_1 + new_char_2)

        return ''.join(plaintext).replace('X', '')

if __name__ == "__main__":

    keyword = "KEYWORD"
    cipher = PlayfairCipher(keyword)
    
    plaintext = "HELLO WORLD"
    encrypted_text = cipher.encrypt(plaintext)
    
    print(f"Plaintext: {plaintext}")
    print(f"Encrypted text: {encrypted_text}")
    
    decrypted_text = cipher.decrypt(encrypted_text)

    print(f"Decrypted text: {decrypted_text}")