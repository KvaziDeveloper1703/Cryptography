"""
The Vigenère Cipher is a polyalphabetic encryption method that uses a keyword to determine the shifting of the alphabet. Each letter of the plaintext is encrypted using a separate shift dictated by the corresponding letter of the keyword.

Algorithm:
+ Choose a keyword;
+ Repeat or truncate the keyword to match the length of the plaintext;
+ For each letter in the plaintext:
    + Identify its position in the alphabet;
    + Use the corresponding letter of the keyword to determine the shift value;
    + Shift the position of the plaintext letter by the value of the keyword letter;
    + If the shift exceeds the alphabet's boundaries, wrap around to the beginning;
+ Replace the plaintext letter with the one at the computed position;
+ Non-alphabetic characters are typically left unchanged.

Шифр Виженера — это метод полиалфавитного шифрования, основанный на использовании ключевого слова для задания сдвига алфавита. Каждая буква открытого текста шифруется с использованием отдельного сдвига, определяемого соответствующей буквой ключевого слова.

Алгоритм работы:
+ Выбирается ключевое слово;
+ Ключ повторяется или обрезается до длины открытого текста;
+ Для каждой буквы открытого текста:
    + Определяется её позиция в алфавите;
    + Значение буквы ключевого слова задаёт величину сдвига;
    + Позиция буквы открытого текста сдвигается на указанное значение;
    + Если сдвиг выходит за границы алфавита, осуществляется переход к началу;
+ Буква заменяется на новую, находящуюся на вычисленной позиции;
+ Прочие символы обычно остаются без изменений.
"""