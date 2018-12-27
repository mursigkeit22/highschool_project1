from nltk import ngrams
import docx


def get_text(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    joined_text = ' '.join(full_text)
    split_text_from_docx = joined_text.split()
    return split_text_from_docx


def making_list_of_common_grams(text1, text2):
    grams1 = ngrams(text1, 4)
    list_of_grams1 = list(grams1)
    grams2 = ngrams(text2, 4)
    list_of_grams2 = list(grams2)
    list_of_common_grams = []
    for gram1 in list_of_grams1:
        for gram2 in list_of_grams2:
            if gram1 == gram2:
                list_of_common_grams.append(gram1)
                break  # или лучше без брейка?
    return list_of_common_grams


def adding_tags(split_text, list_of_common_grams):
    text_split1 = list(split_text)
    text_with_tags = list(split_text)
    start_tag = '<span style="background-color: #f38fd1">'
    end_tag = '</span>'
    for gramm in list_of_common_grams:
        current_pos = 0
        current_fourgramm = \
            (text_split1[current_pos], text_split1[current_pos + 1], text_split1[current_pos + 2],
             text_split1[current_pos + 3])
        while current_fourgramm != gramm and current_pos < len(split_text) - 4:
            current_pos += 1
            current_fourgramm = \
                (text_split1[current_pos], text_split1[current_pos + 1], text_split1[current_pos + 2],
                 text_split1[current_pos + 3])
        else:
            text_with_tags[current_pos] = start_tag + text_split1[current_pos] + end_tag
            text_with_tags[current_pos + 1] = start_tag + text_split1[current_pos + 1] + end_tag
            text_with_tags[current_pos + 2] = start_tag + text_split1[current_pos + 2] + end_tag
            text_with_tags[current_pos + 3] = start_tag + text_split1[current_pos + 3] + end_tag
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


def creating_html (text_list_withtags1, text_list_withtags2, filename):
    text_withtags_google = ' '.join(text_list_withtags1)
    text_withtags_trans = ' '.join(text_list_withtags2)
    name_txt = str(filename) + '.html'
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
