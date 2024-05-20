# На вход программе подается строка текста на английском языке,
# в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать
# с помощью шифра Цезаря (циклического сдвига на длину этого слова).
# Строчные буквы при этом остаются строчными, а прописные – прописными.
# Гарантируется, что между различными словами присутствует один пробел.

# Пример:
# Input: 'Day, mice. "Year" is a mistake!'
#Output: 'Gdb, qmgi. "Ciev" ku b tpzahrl!'



const_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'                # Прописные буквы
const_lower = 'abcdefghijklmnopqrstuvwxyz'                # Строчные буквы

STRING_INPUT = 'Day, mice. "Year" is a mistake!'          # Ввод исходного текста

str_ = STRING_INPUT.split(' ')                           # Перевод строки в список символов, разделенных пробелом

print("Исходный текст:")
print(STRING_INPUT)
print(" ")
Upper_list = list(const_upper)                            # Перевод шаблонов в список символов
Lower_list = list(const_lower)


def len_word(word):                                 # Функция подсчета длины слова без учета знаков препинания и кавычек
    count = 0
    for i in word:
        if i in const_upper or i in const_lower:
            count += 1
    return count


def code(word, shift):                              # Функция формирования зашифрованного слова
    global Upper_list, Lower_list                   # Входные аргументы: исходное слово со знаками и размер сдвига
    str_new = []
    for i in word:
        if i.isalpha:
            if i in Upper_list:                                # Шифрование прописных букв
                for j in Upper_list:
                    if i == j:
                        count = Upper_list.index((j))
                        transfer = count + shift
                        if transfer < len(Upper_list):
                            str_new.append(Upper_list[transfer])
                        else:
                            transfer1 = shift - (len(Upper_list) - count)     # Если величина сдвига превосходит длину,
                            str_new.append(Upper_list[transfer1])             # то расчитывается сдвиг в начале
            elif i in Lower_list:                               # Шифрование строчных букв
                for j in Lower_list:
                    if i == j:
                        count = Lower_list.index((j))
                        transfer = count + shift
                        if transfer < len(Lower_list):
                            str_new.append((Lower_list[transfer]))
                        else:
                            transfer1 = shift - (len(Lower_list) - count)
                            str_new.append(Lower_list[transfer1])
            else:
                str_new.append(i)                             # Оставление без шифрования знаков препинания

    word1 = ''.join(str_new)                                  # Склейка зашифрованного слова
    return word1

shift = []
for i in range(0, len(str_)):                                  # Расчет длины шифроемых слов
    shift.append(len_word(str_[i]))


New_text = []
for i in range(0, len(str_)):                                 # Кодирование исходного текста и создание списка
    New_text.append(code(str_[i], shift[i]))

print("Зашифрованный текст:")
print(' '.join(New_text))                                    # Склейка текста через пробел и перевод его в строку

