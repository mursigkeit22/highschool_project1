import sys
import pythone_functions2 as pf


text_from_google = str(sys.argv[-1]).split()
# text_from_google = ' '.join(text_from_google)
# words_in_text_from_google = len(text_from_google.split())

names_and_paths = dict()  # имя файла: путь до файла
filenames_and_texts = dict()  # имя файла: текст файла

for i in range(1, len(sys.argv) - 1, 2):
    names_and_paths[sys.argv[i]] = sys.argv[i + 1]
for name, path in names_and_paths.items():
    filenames_and_texts[name] = pf.get_text(path) # тест поспличеный

filenames_and_commongrams = dict()  # имя файла: общие 4-граммы с text_from_google
for filename, text in filenames_and_texts.items():
    filenames_and_commongrams[filename] = pf.making_list_of_common_grams(text_from_google, text)
# number_words_with_tag = int
# ident = float
# words_in_doc2 = int
with open('newfile.txt', 'w', encoding='utf-8') as made_file:
    made_file.write('<!DOCTYPE html> <html> <head> <meta charset="UTF-8"> '
                    '<title> Результаты сравнения </title> <style> .indent{ padding-left: 100px }</style> </head>  <body>')
for filename in filenames_and_texts:
    text_list_withtags_google = pf.adding_tags(text_from_google, filenames_and_commongrams[filename])
    text_list_withtags_trans = pf.adding_tags(filenames_and_texts[filename], filenames_and_commongrams[filename])
    pf.creating_html(text_list_withtags_google, text_list_withtags_trans, filename)
    ident_to_write = str(pf.percentage(text_list_withtags_google, text_list_withtags_trans))
    with open('newfile.txt', 'a', encoding='utf-8') as made_file:
        made_file.write('<p>' + filename + '<span class="indent"> </span>' + str(ident_to_write) +
                        """% identical <button onclick="window.open('"""
                        + filename + """.html', '', 'width=1200')">open</button>
</p>
""")

with open('newfile.txt', 'a', encoding='utf-8') as made_file:
    made_file.write('</body> </html>')
# results
print(len(sys.argv), type(sys.argv))
print(len(names_and_paths))
print(len(filenames_and_texts))