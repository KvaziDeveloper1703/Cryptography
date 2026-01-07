'''
The Atbash cipher is a substitution cipher that replaces each letter with its opposite counterpart in the alphabet.

Encryption / Decryption:
    - Use the standard 26-letter Latin alphabet;
    - Match each letter with the one in the reverse position;
    - For each letter in the text:
        - Find its reverse equivalent in the alphabet;
        - Replace it with that letter.
    - The result is a reversed-alphabet substitution;
    - Non-letter characters are skipped or left unchanged;
    - The cipher is symmetric - the same process is used for both encryption and decryption.

Шифр Атбаш - это подстановочный шифр, в котором каждая буква заменяется на противоположную по положению в алфавите.

Зашифровка / Расшифровка:
    - Используется стандартный латинский алфавит из 26 букв;
    - Каждой букве ставится в соответствие буква с противоположного конца алфавита;
    - Для каждой буквы в тексте:
        - Определяется "зеркальная" буква;
        - Выполняется замена.
    - В результате получается замена по принципу отражения алфавита;
    - Неалфавитные символы пропускаются или остаются без изменений;
    - Шифр симметричен - один и тот же алгоритм используется как для шифрования, так и для расшифровки.

Atbash-salaus on korvaussalaus, jossa jokainen kirjain korvataan aakkoston vastakkaisella kirjaimella.

Salaus / purku:
    - Käytetään tavallista 26-kirjaimista latinalaista aakkostoa;
    - Jokainen kirjain yhdistetään aakkoston käänteisessä järjestyksessä olevaan vastineeseensa;
    - Jokaiselle tekstin kirjaimelle:
        - Etsitään sen käänteinen vastine aakkostossa;
        - Korvataan se tällä kirjaimella.
    - Tuloksena on käänteisen aakkoston mukainen korvaus;
    - Muut kuin kirjaimet ohitetaan tai jätetään muuttumattomiksi;
    - Salaus on symmetrinen – samaa prosessia käytetään sekä salauksessa että purussa.
'''

class AtbashCipher:
    def __init__(self):
        self.alphabet = [   'A', 'B', 'C', 'D', 'E',
                            'F', 'G', 'H', 'I', 'J',
                            'K', 'L', 'M', 'N', 'O',
                            'P', 'Q', 'R', 'S', 'T',
                            'U', 'V', 'W', 'X', 'Y', 'Z'
                    ]

        self.mapping = {}
        for i in range(len(self.alphabet)):
            letter = self.alphabet[i]
            reverse_letter = self.alphabet[-(i + 1)]
            self.mapping[letter] = reverse_letter

    def encode(self, text: str) -> str:
        result = []

        for character in text.upper():
            if character in self.mapping:
                result.append(self.mapping[character])
            else:
                result.append(character)

        return ''.join(result)

    def decode(self, text: str) -> str:
        return self.encode(text)

if __name__ == "__main__":
    cipher = AtbashCipher()

    plain_text = "HELLO, WORLD!"
    encoded_text = cipher.encode(plain_text)

    print(f"Plain text:    {plain_text}")
    print(f"Encoded text:  {encoded_text}")

    decoded_text = cipher.decode(encoded_text)
    print(f"Decoded text:  {decoded_text}")