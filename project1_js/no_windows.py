import tkinter
from tkinter import *
import docx
from docx import Document
from gettext_from_docx import get_text
from common_fourgrams import making_list_of_common_fourgrams_strings
document1 = get_text('тестовыйЮриспруденцияgoogle.docx')
words_in_doc1 = len(document1.split())
print(len(document1.split()))
document2 = get_text('тестовыйЮриспруденция_Anna Babayan(en).docx')
words_in_doc2 = len(document2.split())
print(len(document2.split()))
from tkinter import Text

root = Tk()
text1 = Text(width=50, height=25, bg="white", font=("Georgia"), wrap=WORD, padx=10, pady=100, relief=FLAT, bd=10)
text2 = Text(width=50, height=25, bg="white", font=("Georgia"), wrap=WORD, padx=10, pady=100, relief=FLAT, bd=10)
text1.pack(side=LEFT)
text2.pack(side=RIGHT)
text1.insert(1.0, document1)
text2.insert(1.0, document2)
list_of_common_fourgrams = making_list_of_common_fourgrams_strings('тестовыйЮриспруденцияgoogle.docx', 'тестовыйЮриспруденция_Anna Babayan(en).docx')
for fourgram in list_of_common_fourgrams:
    str_gram = fourgram
    start_to_search_text1 = '1.0' #"line 1, character 0"
    start_to_search_text2 = '1.0'
    start_pos_text1 = text1.search(str_gram, start_to_search_text1, stopindex=END)
    start_pos_text2 = text2.search(str_gram, start_to_search_text2, stopindex=END)
    if start_pos_text1:
        end_pos_text1 = '{}+{}c'.format(start_pos_text1, len(str_gram))
        #print('{!r}'.format(end_pos_text1))
        text1.tag_add('highlight', start_pos_text1, end_pos_text1)
        text1.tag_config('highlight', background='#F5BCA9')
        start_to_search_text1=end_pos_text1
    if start_pos_text2:
        end_pos_text2 = '{}+{}c'.format(start_pos_text2, len(str_gram))
        #print('{!r}'.format(end_pos_text2))
        text2.tag_add('highlight', start_pos_text2, end_pos_text2)
        text2.tag_config('highlight', background='#F7BE81')
        start_to_search_text1 = end_pos_text2
text_with_tag = text1.tag_ranges('highlight')  # начальная позиция, конечная, начальная, конечная, начальная...
words_with_tag = ''
for i in range(0, len(text_with_tag), 2):  # без шага 2 получается какая-то фигня
        tag_begins = text_with_tag[i]
        tag_ends = text_with_tag[i+1]
        words_with_tag = words_with_tag + ' ' + text1.get(tag_begins, tag_ends)
print(words_with_tag)
number_words_with_tag = len(words_with_tag.split())
print(len(words_with_tag.split()))
ident = number_words_with_tag / ((words_in_doc1 + words_in_doc2) // 2)
print(number_words_with_tag)
print(words_in_doc1)
print(words_in_doc2)
print(ident)
# root.mainloop()
