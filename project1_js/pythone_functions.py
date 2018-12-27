import docx
import re
import sys
from nltk import ngrams

def get_text(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    joined_text = ' '.join(full_text)
    joined_text = joined_text.split()
    whole_text_in_one_string = ' '.join(joined_text)
    # whole_text_in_one_string = re.sub(' +', ' ', joined_text)
    return whole_text_in_one_string

def count_fourgrams(text_from_google, text_from_docx): # для отладки
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
