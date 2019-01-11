import sys
import pythone_functions2 as pf
import docx2txt
text_from_google = str(sys.argv[-1])


words_in_text_from_google = len(list(text_from_google.split()))
names_and_paths = dict()  # имя файла: путь до файла
filenames_and_texts = dict()  # имя файла: текст файла
filenames_and_indents = dict()

for i in range(1, len(sys.argv) - 1, 2):
    names_and_paths[sys.argv[i]] = sys.argv[i + 1]

for name, path in names_and_paths.items():
    filenames_and_texts[name] = docx2txt.process(path)

for name, text in filenames_and_texts.items():
    filenames_and_indents[name] = pf.marking_indentations(filenames_and_texts[name])

filenames_and_commongrams = dict()  # имя файла: общие 4-граммы с text_from_google
for filename, text in filenames_and_texts.items():
    filenames_and_commongrams[filename] = pf.making_set_of_common_grams(text_from_google, text)

with open('tempFiles\\newfile.txt', 'w', encoding='utf-8') as made_file:
    made_file.write('<!DOCTYPE html> <html> <head> <meta charset="UTF-8"> '
                    '<title> Results </title> '
                    '<link rel="stylesheet" href="style_second_window.css">'
                    
                    ' </head>  <body style="background-color: #afdfe1">'
                    '<table class="table"  >'
                    '<tr>    <td class="fc-header">Name of a file</td>'
    '<td class="sc-header">Result</td>'
       '<td class="tc-header"> </td>'
   '</tr>')
for filename in filenames_and_texts:

    set_to_exclude = pf.making_list_of_reapeated_gramms(text_from_google, filenames_and_texts[filename],
                                                        filenames_and_commongrams[filename])[2]

    tagged_list_google = pf.adding_tags(text_from_google, filenames_and_commongrams[filename], set_to_exclude)
    tagged_list_trans = pf.adding_tags(filenames_and_texts[filename], filenames_and_commongrams[filename],
                                       set_to_exclude)
    list_with_tags_and_indents_google = pf.making_paragraphs(pf.marking_indentations(text_from_google),
                                                             tagged_list_google)
    list_with_tags_and_indents_trans = pf.making_paragraphs(filenames_and_indents[filename], tagged_list_trans)

    pf.creating_html(list_with_tags_and_indents_google, list_with_tags_and_indents_trans, filename)
    identical_to_write = str(pf.percentage(tagged_list_google, tagged_list_trans))
    with open('tempFiles\\newfile.txt', 'a', encoding='utf-8') as made_file:
        made_file.write('<tr>    <td class="first-column" >' + filename + '</td>    <td class="second-column">' + str(identical_to_write) +
                        """% identical </td>
       <td class="third-column"><button class="button" onclick="window.open('"""
                        + 'tempFiles\\\\' + filename + """.html', '', 'width=1200')">open</button></td>
  </tr>

""")

with open('tempFiles\\newfile.txt', 'a', encoding='utf-8') as made_file:
    made_file.write('</table> </body> </html>')
# results:
print('len and type sys.argv ', len(sys.argv), type(sys.argv))
print('len names_and_paths ', len(names_and_paths))
print('len filenames_and_texts ', len(filenames_and_texts))
