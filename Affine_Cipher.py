"""
The Affine Cipher is a substitution cipher that encrypts text using a linear transformation. Each letter in the alphabet is replaced with another letter based on a mathematical rule. The transformation is consistent for all characters in the text.

Algorithm:

Encryption:
+ Choose two keys: a and b;
+ Ensure that a is coprime with the size of the alphabet;
+ For each letter in the plaintext:
    + Determine its position in the alphabet;
    + Multiply this position by the first key a;
    + Add the second key b to the result;
    + Divide the total by the size of the alphabet and take the remainder (modulo operation) to ensure the result stays within the alphabet range;
    + Replace the letter with the one at the new position;
+ Non-alphabetic characters are usually left unchanged.

Decryption:
+ Determine the position of the encrypted letter in the alphabet;
+ Subtract the second key b from this position;
+ Multiply the result by the modular inverse of the first key a, ensuring the result wraps around if it exceeds the alphabet size;
+ Replace the encrypted letter with the one at the calculated position.

Афинный шифр — это подстановочный шифр, который шифрует текст с использованием линейного преобразования. Каждая буква алфавита заменяется другой буквой на основе определенного правила. Преобразование одинаково для всех символов текста.

Алгоритм работы:

Зашифровка:
+ Выбираются два ключа: a и b;
+ Убедитесь, что a взаимно простое с размером алфавита;
+ Для каждой буквы открытого текста:
    + Определите её позицию в алфавите (начиная с 0);
    + Умножьте эту позицию на первый ключ a;
    + Прибавьте второй ключ b к полученному результату;
    + Разделите итог на размер алфавита и возьмите остаток (чтобы результат остался в пределах алфавита);
    + Замените букву на ту, что находится на новой позиции;
Остальные символы обычно остаются без изменений.

Расшифровка:
+ Найдите позицию зашифрованной буквы в алфавите;
+ Вычтите второй ключ b из этой позиции;
+ Умножьте результат на мультипликативно обратное значение первого ключа a, следя за тем, чтобы результат оставался в пределах алфавита;
+ Замените зашифрованную букву на ту, что находится на вычисленной позиции.
"""