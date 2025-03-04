"""англо-русский словарь"""

from os import strerror

def main():
    dict_word = dict_loader()
    while True:
        word = input('Введите слово, или 0 для выхода').lower()
        if word == '0':
            break
        search_word(word, dict_word)


def search_word(word, dict_word):
    if word in dict_word:
        print(f'{word} - {dict_word[word]}')
    else:
        print('слово не найдено')
        choice = input('Введите 1, если хотите добавить слово с переводом в словарь')
        if choice == '1':
            eng = input('введите слово на английском')
            ru = input('введите слово на русском')
            word_add(eng, ru, dict_word)
search_word('cat', {'cat':'кот'}) # тест функции

def dict_loader():
    try:
        dict_word = {}
        with open('text.txt', 'r', encoding='utf-8') as file:
            for i in file:
                eng, ru = i.split(',')
                dict_word[eng] = ru.strip()
                dict_word[ru.strip()] = eng
        return dict_word
    except IOError as e:
        print(strerror(e.errno))
print(dict_loader()) # тест функции

def word_add(eng, ru, dict_word):
    dict_word[eng] = ru.strip()
    dict_word[ru.strip()] = eng
    try:
        with open('text.txt', 'a', encoding='utf-8') as dict:
            dict.write(f'{eng}, {ru}\n')
        return dict_word
    except IOError as e:
        print(strerror(e.errno))
#word_add('apple', "яблоко", {}) # тест функции

main()