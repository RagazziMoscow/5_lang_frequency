import os.path
import re
from collections import Counter


# Загружает текст из файла
def load_data(filepath):
    if(os.path.exists(filepath)):
        with open(filepath, 'r') as text_file:
            load_text = text_file.read()
    else:
        load_text = None
    return load_text


# Чистит текст, возвращает строку
def clear_text(strings):
    text_data = re.sub("\n|\t|\?|\!|\.|,|\-|\=|\:", '', strings)
    text_data = re.sub("\s\s", '', text_data)
    return text_data


# Разделяет полученный текст на слова, возвращает список со всеми словами
def split_text(strings):
    split_data = re.split("\s", strings)
    return split_data


# Приводит все слова к нижнему регистру, возвращает список
def normalize_words(words_array):
    return [word.lower() for word in words_array]


# Выдаёт список 10 самых частых слов, вместе с числом их повторений
def get_most_frequent_words(text_array):
    words_counter = Counter(text_array)
    words_list = words_counter.most_common(10)
    return words_list


def main():

    path = input("Введите путь до файла:\n")
    file_content = load_data(path)

    # Если файл существует
    if file_content is not None:
        string = clear_text(file_content)
        split_string = split_text(string)
        norm_string = normalize_words(split_string)
        freq_array = get_most_frequent_words(norm_string)
        print("Самые встречающиеся слова в тексте:")
        for word_number, item in enumerate(freq_array):
            print("{point_num}. {word}".format(point_num=word_number+1, word=item[0]))

    else:
        print("Файла, путь до которого вы ввели, не существует")


if __name__ == '__main__':
    main()
