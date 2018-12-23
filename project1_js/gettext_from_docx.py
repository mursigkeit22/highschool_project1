import sys
import docx
import re


def get_text(filename):
    doc = docx.Document(filename)
    full_text = []
    for para in doc.paragraphs:
        full_text.append(para.text)
    joined_text = ' '.join(full_text)
    whole_text_in_one_string = re.sub(' +', ' ', joined_text)
    return whole_text_in_one_string

print(get_text('тестовыйЮриспруденцияgoogle.docx'))
sys.stdout.flush()