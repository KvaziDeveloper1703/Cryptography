'''
The Rail Fence cipher is a transposition cipher that rearranges the characters of the plaintext by writing them in a zigzag pattern across multiple "rails".

Encryption:
+ Choose the number of rails;
+ Write the plaintext in a zigzag pattern across the rails;
+ After finishing, read the characters row by row to get the ciphertext;
+ No substitution occurs — only the positions of the characters are changed.

Decryption:
+ Reconstruct the zigzag pattern based on the number of rails and the length of the message;
+ Fill in the characters row by row;
+ Read the characters in a zigzag order to recover the original plaintext.

Железнодорожный шифр — это шифр перестановки, в котором символы текста записываются по зигзагообразной линии на нескольких уровнях (рельсах), а затем считываются построчно.

Зашифровка:
+ Выбирается количество «рельсов»;
+ Текст записывается по диагонали вниз и вверх, чередуя рельсы, образуя зигзаг;
+ После записи весь текст считывается по строкам — сначала верхний рельс, затем следующий, и так далее;
+ Символы не заменяются — меняется только их порядок.

Расшифровка:
+ Воссоздаётся зигзагообразный шаблон на основе длины сообщения и числа рельсов;
+ Символы вставляются по строкам в соответствующие позиции;
+ Текст восстанавливается, считывая символы по зигзагообразному маршруту.
'''

class RailFenceCipher:
    def __init__(self, rails: int):
        self.rails = rails

    def encode(self, text: str) -> str:
        text = text.replace(" ", "")
        fence = []
        for i in range(self.rails):
            fence.append([])
        rail = 0
        direction = 1

        for character in text:
            fence[rail].append(character)
            rail += direction

            if rail == 0 or rail == self.rails - 1:
                direction *= -1

        result = []
        for row in fence:
            result.extend(row)

        return ''.join(result)

    def decode(self, text: str) -> str:
        pattern = self.get_pattern(len(text))
        fence = []
        for i in range(len(text)):
            fence.append('')

        index = 0
        for rail in range(self.rails):
            for i in range(len(text)):
                if pattern[i] == rail:
                    fence[i] = text[index]
                    index += 1

        result = ''.join(fence)
        return result

    def get_pattern(self, length: int) -> list:
        pattern = []
        rail = 0
        direction = 1

        for _ in range(length):
            pattern.append(rail)
            rail += direction

            if rail == 0 or rail == self.rails - 1:
                direction *= -1

        return pattern

if __name__ == "__main__":
    cipher = RailFenceCipher(rails=3)

    plain_text = "HELLO, WORLD!"
    encoded_text = cipher.encode(plain_text)

    print(f"Plain text:    {plain_text}")
    print(f"Encoded text:  {encoded_text}")

    decoded_text = cipher.decode(encoded_text)
    print(f"Decoded text:  {decoded_text}")