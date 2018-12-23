import docx
import re
from nltk import ngrams
import gettext_from_docx
from gettext_from_docx import get_text


def making_list_of_common_fourgrams_strings(text1, text2):
    fourgrams1 = ngrams(get_text(text1).split(' '), 4)
    list_of_fourgrams1 = list(fourgrams1)
    #print(len(get_text(text1).split()))
    fourgrams2 = ngrams(get_text(text2).split(' '), 4)
    list_of_fourgrams2 = list(fourgrams2)
    #print(len(get_text(text2).split()))
    list_of_common_fourgrams = []
    for gram1 in list_of_fourgrams1:
        for gram2 in list_of_fourgrams2:
            if gram1 == gram2:
                list_of_common_fourgrams.append(gram1)

    list_of_common_fourgrams_strings = []
    for gram in list_of_common_fourgrams:
        list_of_common_fourgrams_strings.append(' '.join(gram))
    return list_of_common_fourgrams_strings
#a = making_list_of_common_fourgrams_strings('тестовыйЮриспруденцияgoogle.docx', 'тестовыйЮриспруденция_Anna Babayan(en).docx')
# for el in a:
#     if el in get_text('trbygoogle.docx'):
#         print(el, True)
#     else:
#         print(el, False)