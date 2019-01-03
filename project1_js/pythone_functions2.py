from nltk import ngrams
n = 5
import docx


def get_text(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    joined_text = ' '.join(full_text)
    split_text_from_docx = joined_text.split()
    return split_text_from_docx



def making_set_of_common_grams(text1, text2):
    grams1 = ngrams(text1, n)
    set_of_grams1 = set(grams1)
    grams2 = ngrams(text2, n)
    set_of_grams2 = set(grams2)
    set_of_common_grams = set_of_grams1.intersection(set_of_grams2)
    return set_of_common_grams

def making_list_of_reapeated_gramms(text1, text2, set_common_grams):
    more_than_once_list1 = []
    more_than_once_list2 = []
    grams1 = ngrams(text1, n)
    list_of_grams1 = list(grams1)
    grams2 = ngrams(text2, n)
    list_of_grams2 = list(grams2)
    to_exclude = set()
    for gramm in set_common_grams:
        if list_of_grams1.count(gramm) > 1:
            to_exclude.add(gramm)
            more_than_once_list1.append((gramm, list_of_grams1.count(gramm)))
        if list_of_grams2.count(gramm) > 1:
            to_exclude.add(gramm)
            more_than_once_list2.append((gramm, list_of_grams2.count(gramm)))

    return len(more_than_once_list1),len(more_than_once_list2), to_exclude

# def more_than_once(list_common_grams):
#     more_than_once_list = []
#     set_to_compare = set()
#     for gramm in list_common_grams:
#         if list_common_grams.count(gramm) > 1:
#             if gramm not in set_to_compare:
#                 more_than_once_list.append((gramm, list_common_grams.count(gramm)))
#                 set_to_compare.add(gramm)
#     return more_than_once_list, set_to_compare


def what_current_ngramm(current_pos, split_text):
    current_ngramm = []
    for i in range(n):
        current_ngramm.append(split_text[current_pos+i])
    current_ngramm = tuple(current_ngramm)
    return current_ngramm



def adding_tags(split_text, set_of_common_grams, set_to_exclude):
    text_split1 = list(split_text)
    text_with_tags = list(split_text)
    start_tag = '<span style="background-color: #f38fd1">'
    end_tag = '</span>'
    for gramm in set_of_common_grams.difference(set_to_exclude):
        current_pos = 0
        current_ngramm = what_current_ngramm(current_pos, text_split1)
            # (text_split1[current_pos], text_split1[current_pos + 1], text_split1[current_pos + 2],
            #  text_split1[current_pos + 3], text_split1[current_pos + 4])

        while current_ngramm != gramm and current_pos < len(split_text) - n:

            current_pos += 1
            current_ngramm = what_current_ngramm(current_pos, text_split1)
                # \
                # (text_split1[current_pos], text_split1[current_pos + 1], text_split1[current_pos + 2],
                #  text_split1[current_pos + 3], text_split1[current_pos + 4])

        else:
            # if gramm not in set_to_compare:
            for i in range(n):
                text_with_tags[current_pos + i] = start_tag + text_split1[current_pos + i] + end_tag
    for el in set_to_exclude:
        current_pos = 0
        while current_pos < len(split_text) - n:
            current_ngramm = what_current_ngramm(current_pos, text_split1)
            if el == current_ngramm:
                for i in range(n):
                    text_with_tags[current_pos + i] = start_tag + text_split1[current_pos + i] + end_tag
            current_pos += 1


                # text_with_tags[current_pos] = start_tag + text_split1[current_pos] + end_tag
                # text_with_tags[current_pos + 1] = start_tag + text_split1[current_pos + 1] + end_tag
                # text_with_tags[current_pos + 2] = start_tag + text_split1[current_pos + 2] + end_tag
                # text_with_tags[current_pos + 3] = start_tag + text_split1[current_pos + 3] + end_tag
                # text_with_tags[current_pos + 4] = start_tag + text_split1[current_pos + 4] + end_tag
            # else:
            #     for i in range(len(more_than_once_list)):
            #         if more_than_once_list[i][0] == gramm:
            #             a = more_than_once_list[i][1]
            #             tagged_grams = 0
            #             while tagged_grams < a and current_pos < len(split_text) - 4:
            #                 if current_fourgramm == gramm:
            #                     text_with_tags[current_pos] = start_tag + text_split1[current_pos] + end_tag
            #                     text_with_tags[current_pos + 1] = start_tag + text_split1[current_pos + 1] + end_tag
            #                     text_with_tags[current_pos + 2] = start_tag + text_split1[current_pos + 2] + end_tag
            #                     text_with_tags[current_pos + 3] = start_tag + text_split1[current_pos + 3] + end_tag
            #                     current_pos += 1
            #                     tagged_grams += 1
            #                     current_fourgramm = \
            #                         (text_split1[current_pos], text_split1[current_pos + 1],
            #                          text_split1[current_pos + 2],
            #                          text_split1[current_pos + 3])
            #                 else:
            #                     current_pos += 1
            #                     current_fourgramm = \
            #                         (text_split1[current_pos], text_split1[current_pos + 1],
            #                          text_split1[current_pos + 2],
            #                          text_split1[current_pos + 3])


    return text_with_tags





def percentage(list_with_tags1, list_with_tags2):
    number_words1 = len(list_with_tags1)
    number_words2 = len(list_with_tags2)
    number_tags1 = 0
    number_tags2 = 0
    for el in list_with_tags1:
        if '<span style="background-color:' in el:
            number_tags1 += 1
    for el in list_with_tags2:
        if '<span style="background-color:' in el:
            number_tags2 += 1
    result_float1 = number_tags1 / ((number_words1+number_words2) // 2)
    result_twoafterdot1 = float("{0:.2f}".format(result_float1))
    percent_identicle1 = str(int(result_twoafterdot1 * 100))
    result_float2 = number_tags2 / ((number_words1 + number_words2) // 2)
    result_twoafterdot2 = float("{0:.2f}".format(result_float2))
    percent_identicle2 = str(int(result_twoafterdot2 * 100))
    return percent_identicle1, percent_identicle2


def creating_html(text_list_withtags1, text_list_withtags2, filename):
    text_withtags_google = ' '.join(text_list_withtags1)
    text_withtags_trans = ' '.join(text_list_withtags2)
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

            background: #fafefc; /* Цвет фона */
            border: 1px solid #c5ecf4;
            padding: 20px; /* Поля вокруг текста */
            overflow: hidden;
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
