import re
from collections import Counter


## Загружает текст из файла, возвращает строку
def load_data(filepath):
    #text_file = open(filepath,'r')
    try:
        with open(filepath, 'r') as text_file:
            text_data = text_file.read()
            return text_data
    except FileNotFoundError:
    	return None


## Чистит текст, возвращает строку
def clear_text(strings):
    text_data = re.sub("\n|\t|\?|\!|\.|,|\-|\=|\:", '', strings)    
    text_data = re.sub("\s\s", '', text_data)
    return text_data

## Разделяет полученный текст на слова, возвращает список со всеми словами из текста
def split_text(strings):
    split_data = re.split("\s", strings)
    return split_data

## Приводит все слова к нижнему регистру, возвращает список
def normalize_words(words_array):
	return [word.lower() for word in words_array]

## Выдаёт список 10 слов, которые больше всего встречаются, вместе с числом их повторений
## Возвращает список
def get_most_frequent_words(text_array):
    freq_dict = dict(Counter(text_array))
    I = lambda x:x[1]
    words_list = sorted(freq_dict.items(), key=I, reverse = True)[0:10]
    return words_list
    



def main():

    print("Введите путь до файла:")
    path = input()
    file_content = load_data(path)

    #Если файл существует
    if file_content is not None:
        string = clear_text(file_content)
        string = split_text(string)
        string = normalize_words(string)
        #print(string)
        freq_array = get_most_frequent_words(string) 
        for word_number, item in enumerate(freq_array):
        	print(str(word_number+1)+".", item[0])

    else:
    	print("Файла, путь до которого вы ввели, не существует")




if __name__ == '__main__':
	main()