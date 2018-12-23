import docx
import re
import sys
from nltk import ngrams
from tkinter import Tk, Text, RIGHT, LEFT, END

def get_text(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    joined_text = ' '.join(full_text)
    whole_text_in_one_string = re.sub(' +', ' ', joined_text)
    return whole_text_in_one_string

def count_fourgrams(text_from_google, text_from_docx): # кажется, не надо
    fourgrams1 = ngrams(text_from_google.split(' '), 4)
    list_of_fourgrams1 = list(fourgrams1)
    a = len(list_of_fourgrams1)
    fourgrams2 = ngrams(text_from_docx.split(' '), 4)
    list_of_fourgrams2 = list(fourgrams2)
    b = len(list_of_fourgrams2)
    list_of_common_fourgrams = []
    for gram1 in list_of_fourgrams1:
        for gram2 in list_of_fourgrams2:
            if gram1 == gram2:
                list_of_common_fourgrams.append(gram1)
    c = len(list_of_common_fourgrams)
    return (a, b, c)

def making_list_of_common_fourgrams_strings(text_from_google, text_from_docx):
    fourgrams1 = ngrams(text_from_google.split(' '), 4)
    list_of_fourgrams1 = list(fourgrams1)
    fourgrams2 = ngrams(text_from_docx.split(' '), 4)
    list_of_fourgrams2 = list(fourgrams2)
    list_of_common_fourgrams = []
    for gram1 in list_of_fourgrams1:
        for gram2 in list_of_fourgrams2:
            if gram1 == gram2:
                list_of_common_fourgrams.append(gram1)
    list_of_common_fourgrams_strings = []
    for gram in list_of_common_fourgrams:
        list_of_common_fourgrams_strings.append(' '.join(gram)) # изначально в грамах лежат тьюплы
    return list_of_common_fourgrams_strings


text_from_google = str(sys.argv[-1])
words_in_text_from_google = len(text_from_google.split())

names_and_paths = dict() # имя файла: путь до файла
filenames_and_texts = dict() # имя файла: текст файла

for i in range(1, len(sys.argv)-1, 2):
    names_and_paths[sys.argv[i]] = sys.argv[i+1]
for name, path in names_and_paths.items():
        filenames_and_texts[name] = get_text(path)

filenames_and_commongrams = dict() # имя файла: общие 4-граммы с text_from_google
for filename, text in filenames_and_texts.items():
    filenames_and_commongrams[filename] = making_list_of_common_fourgrams_strings(text_from_google, text)
number_words_with_tag = int
ident = float
words_in_doc2 = int
with open('newfile.txt', 'w', encoding='utf-8') as made_file:
    made_file.write('<!DOCTYPE html> <html> <head> <meta charset="UTF-8"> '
                    '<title> Результаты сравнения </title> <style> .indent{ padding-left: 100px }</style> </head>  <body>')

for key in filenames_and_texts:
    root = Tk()
    text1 = Text()
    text2 = Text()
    text1.pack(side=LEFT)
    text2.pack(side=RIGHT)
    text1.insert(1.0, text_from_google)
    text2.insert(1.0, filenames_and_texts[key])
    list_of_common_fourgrams = filenames_and_commongrams[key]
    for fourgram in list_of_common_fourgrams:
        str_gram = fourgram
        start_to_search_text1 = '1.0'  # "line 1, character 0"
        start_to_search_text2 = '1.0'
        start_pos_text1 = text1.search(str_gram, start_to_search_text1, stopindex=END)
        start_pos_text2 = text2.search(str_gram, start_to_search_text2, stopindex=END)
        if start_pos_text1:
            end_pos_text1 = '{}+{}c'.format(start_pos_text1, len(str_gram))
            text1.tag_add('highlight', start_pos_text1, end_pos_text1)
            text1.tag_config('highlight', background='#F5BCA9')
            start_to_search_text1=end_pos_text1
        if start_pos_text2:
            end_pos_text2 = '{}+{}c'.format(start_pos_text2, len(str_gram))
            text2.tag_add('highlight', start_pos_text2, end_pos_text2)
            text2.tag_config('highlight', background='#F7BE81')
            start_to_search_text1 = end_pos_text2
    text_with_tag = text1.tag_ranges('highlight')  # начальная позиция, конечная, начальная, конечная, начальная...
    words_with_tag = ''
    for i in range(0, len(text_with_tag), 2):  # без шага 2 получается какая-то фигня
        tag_begins = text_with_tag[i]
        tag_ends = text_with_tag[i + 1]
        words_with_tag = words_with_tag + ' ' + text1.get(tag_begins, tag_ends)
    number_words_with_tag = len(words_with_tag.split())
    words_in_doc2 = len(filenames_and_texts[key].split())
    ident_float = number_words_with_tag / ((words_in_text_from_google + words_in_doc2) // 2)
    ident = float("{0:.2f}".format(ident_float))
    print(key, ' ', ident*100, '%', sep='')
    ident_to_write = str(int(ident * 100))
    with open('newfile.txt', 'a', encoding='utf-8') as made_file:
        made_file.write('<p>' + key + '<span class="indent"> </span>' + ident_to_write + '% identical''</p>')

with open('newfile.txt', 'a', encoding='utf-8') as made_file:
        made_file.write('</body> </html>')
#results
print(len(sys.argv), type(sys.argv))
print(len(names_and_paths))
print(len(filenames_and_texts))
# print(names_and_paths)
# print(words_in_text_from_google)
# print(words_in_doc2)
# print(number_words_with_tag)


