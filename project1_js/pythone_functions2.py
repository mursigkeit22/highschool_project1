from nltk import ngrams
n = 5

import re



def marking_indentations(text):
    text = re.sub('\n+', '\n', text)
    list_paragraphs = text.split('\n')
    indentation_marks_list = []
    summ = 0
    for paragraph in list_paragraphs:
        words_in_paragraph = len(paragraph.split())
        indentation_marks_list.append(summ)
        summ += words_in_paragraph
    return indentation_marks_list


def making_set_of_common_grams(text1, text2):
    text1 = text1.split()
    text2 = text2.split()
    grams1 = ngrams(text1, n)
    set_of_grams1 = set(grams1)
    grams2 = ngrams(text2, n)
    set_of_grams2 = set(grams2)
    set_of_common_grams = set_of_grams1.intersection(set_of_grams2)
    return set_of_common_grams

def making_list_of_reapeated_gramms(text1, text2, set_common_grams):
    more_than_once_list1 = []
    more_than_once_list2 = []
    grams1 = ngrams(text1.split(), n)
    list_of_grams1 = list(grams1)
    grams2 = ngrams(text2.split(), n)
    list_of_grams2 = list(grams2)
    to_exclude = set()
    for gramm in set_common_grams:
        if list_of_grams1.count(gramm) > 1:
            to_exclude.add(gramm)
            more_than_once_list1.append((gramm, list_of_grams1.count(gramm)))
        if list_of_grams2.count(gramm) > 1:
            to_exclude.add(gramm)
            more_than_once_list2.append((gramm, list_of_grams2.count(gramm)))

    return more_than_once_list1, more_than_once_list2, to_exclude

# def more_than_once(list_common_grams):
#     more_than_once_list = []
#     set_to_compare = set()
#     for gramm in list_common_grams:
#         if list_common_grams.count(gramm) > 1:
#             if gramm not in set_to_compare:
#                 more_than_once_list.append((gramm, list_common_grams.count(gramm)))
#                 set_to_compare.add(gramm)
#     return more_than_once_list, set_to_compare



def adding_tags(text, set_of_common_grams, set_to_exclude):

    def what_current_ngramm(current_pos, split_text):
        current_ngramm = []
        for i in range(n):
            current_ngramm.append(split_text[current_pos + i])
        current_ngramm = tuple(current_ngramm)
        return current_ngramm

    text_split1 = list(text.split())
    tagged_list = list(text.split())
    start_tag = '<span style="background-color: #afdfe1">'
    end_tag = '</span>'
    for gramm in set_of_common_grams.difference(set_to_exclude):
        current_pos = 0
        current_ngramm = what_current_ngramm(current_pos, text_split1)
        while current_ngramm != gramm and current_pos < len(text.split()) - n:
            current_pos += 1
            current_ngramm = what_current_ngramm(current_pos, text_split1)
        else:
            for i in range(n):
                tagged_list[current_pos + i] = start_tag + text_split1[current_pos + i] + end_tag
    for el in set_to_exclude:
        current_pos = 0
        while current_pos < len(text.split()) - n:
            current_ngramm = what_current_ngramm(current_pos, text_split1)
            if el == current_ngramm:
                for i in range(n):
                    tagged_list[current_pos + i] = start_tag + text_split1[current_pos + i] + end_tag
            current_pos += 1

    return tagged_list


def percentage(tagged_list1, tagged_list2): # после def_with_tags, до placing_ident
    number_words1 = len(tagged_list1)
    number_words2 = len(tagged_list2)
    number_tags1 = 0
    number_tags2 = 0
    for el in tagged_list1:
        if '<span style="background-color:' in el:
            number_tags1 += 1
    for el in tagged_list2:
        if '<span style="background-color:' in el:
            number_tags2 += 1
    result_float1 = number_tags1 / ((number_words1+number_words2) // 2)
    result_twoafterdot1 = float("{0:.2f}".format(result_float1))
    percent_identical1 = str(int(result_twoafterdot1 * 100))
    result_float2 = number_tags2 / ((number_words1 + number_words2) // 2)
    result_twoafterdot2 = float("{0:.2f}".format(result_float2))
    percent_identical2 = str(int(result_twoafterdot2 * 100))
    return percent_identical1, percent_identical2


def making_paragraphs(indentation_marks_list, tagged_list):
    list_with_tags_and_indents = []
    for j in range(len(indentation_marks_list) - 1):
        for i in range(indentation_marks_list[j], indentation_marks_list[j + 1]):
            list_with_tags_and_indents.append(tagged_list[i])
        list_with_tags_and_indents.append('<br>')
    for i in range(indentation_marks_list[-1], len(tagged_list)):
        list_with_tags_and_indents.append(tagged_list[i])
    return list_with_tags_and_indents


def creating_html(list_with_tags_and_indents1, list_with_tags_and_indents2, filename):
    text_withtags_google = ' '.join(list_with_tags_and_indents1)
    text_withtags_trans = ' '.join(list_with_tags_and_indents2)
    name_txt = 'tempFiles\\' + str(filename) + '.html'
    with open(name_txt, 'w', encoding='utf-8') as future_html:
        future_html.write("""
        <!DOCTYPE html>
<html lang="">
<head>
    <meta charset="UTF-8">
    <title>""" + filename + """</title>
    <style>
        .gross {

            background: #ffffff; /* Цвет фона */
            border: 1px solid #93e2e8;
            padding: 20px; /* Поля вокруг текста */
            overflow: hidden;
            font-family: "Helvetica Neue", Helvetica, sans-serif;
        }
    .left-col, /* левая колонка */
    .right-col/* правая колонка */
    {
    width: 50%;    /* ширина */
    min-width: 180px;  /* минимальная ширина сужения */
    height: 80%;  /* высота */
    box-sizing: border-box;
    /*outline: 1px solid #ff7878;*/
    /*border: 8px solid #aaffaa;*/
    margin-bottom: 2px;
    float: left; /* плавающие блоки */
    font: Helvetica

    }
    .left-col{
    padding-right: 20px; /* отступ справа */
    }
    .right-col{
    padding-left: 20px; /* отступ слева */
    }

    </style>
</head>
<body>
<div class="gross">
<div class="left-col" align="justify">""" + text_withtags_google + """</div>
<div class="right-col" align="justify">""" + text_withtags_trans + """</div>
</div>
</body>
</html>""")
