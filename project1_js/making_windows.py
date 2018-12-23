import sys
# import tkinter
from tkinter import *
import docx
import re
# from docx import Document
from nltk import ngrams


# from gettext_from_docx import get_text
# from common_fourgrams import making_list_of_common_fourgrams_strings


def get_text(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    joined_text = ' '.join(full_text)
    whole_text_in_one_string = re.sub(' +', ' ', joined_text)
    return whole_text_in_one_string


def making_list_of_common_fourgrams_strings(text1, text2):
    fourgrams1 = ngrams(get_text(text1).split(' '), 4)
    list_of_fourgrams1 = list(fourgrams1)
    # print(len(get_text(text1).split()))
    fourgrams2 = ngrams(get_text(text2).split(' '), 4)
    list_of_fourgrams2 = list(fourgrams2)
    # print(len(get_text(text2).split()))
    list_of_common_fourgrams = []
    for gram1 in list_of_fourgrams1:
        for gram2 in list_of_fourgrams2:
            if gram1 == gram2:
                list_of_common_fourgrams.append(gram1)

    list_of_common_fourgrams_strings = []
    for gram in list_of_common_fourgrams:
        list_of_common_fourgrams_strings.append(' '.join(gram))
    return list_of_common_fourgrams_strings


document1 = get_text(sys.argv[1])
print(len(document1.split()))
document2 = get_text(sys.argv[2])
print(len(document2.split()))


root = Tk()
text1 = Text(width=50, height=25, bg="white", font=("Georgia"), wrap=WORD, padx=10, pady=100, relief=FLAT, bd=10)
text2 = Text(width=50, height=25, bg="white", font=("Georgia"), wrap=WORD, padx=10, pady=100, relief=FLAT, bd=10)
text1.pack(side=LEFT)
text2.pack(side=RIGHT)
text1.insert(1.0, document1)
text2.insert(1.0, document2)
list_of_common_fourgrams = making_list_of_common_fourgrams_strings(sys.argv[1],
                                                                   sys.argv[2])
for fourgram in list_of_common_fourgrams:
    str_gram = fourgram
    start_to_search_text1 = '1.0'  # "line 1, character 0"
    start_to_search_text2 = '1.0'
    start_pos_text1 = text1.search(str_gram, start_to_search_text1, stopindex=END)
    start_pos_text2 = text2.search(str_gram, start_to_search_text2, stopindex=END)
    if start_pos_text1:
        end_pos_text1 = '{}+{}c'.format(start_pos_text1, len(str_gram))
        # print('{!r}'.format(end_pos_text1))
        text1.tag_add('highlight', start_pos_text1, end_pos_text1)
        text1.tag_config('highlight', background='#ffc0cb')
        start_to_search_text1 = end_pos_text1
    if start_pos_text2:
        end_pos_text2 = '{}+{}c'.format(start_pos_text2, len(str_gram))
        # print('{!r}'.format(end_pos_text2))
        text2.tag_add('highlight', start_pos_text2, end_pos_text2)
        text2.tag_config('highlight', background='#ffc0cb')
        start_to_search_text1 = end_pos_text2
text_with_tag = text1.tag_ranges('highlight')  # начальная позиция, конечная, начальная, конечная, начальная...
words_with_tag = ''
for i in range(0, len(text_with_tag), 2):  # без шага 2 получается какая-то фигня
    tag_begins = text_with_tag[i]
    tag_ends = text_with_tag[i + 1]
    words_with_tag = words_with_tag + ' ' + text1.get(tag_begins, tag_ends)
print(words_with_tag)
print(len(words_with_tag.split()))

# text1.config(state=DISABLED)
# text2.config(state=DISABLED)
root.mainloop()
print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])

