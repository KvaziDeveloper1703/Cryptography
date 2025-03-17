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