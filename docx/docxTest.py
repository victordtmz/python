from io import StringIO
import docx

doc = docx.Document('defuncion.docx')

# print(doc.paragraphs[0].text)
# for p in doc.items:
#     print(p.text)

with open('defuncion.txt', 'r', encoding='latin') as f:
    for line in f:
        print(line)
    # print(f.read())
    