#CLTK habe ich überhaupt niht zum Laufen gebracht, also verwende ich ein altgriechisches Model von Huggingface:
#https://centre-for-humanities-computing.github.io/odyCy/getting_started.html

import spacy
import csv
import os

nlp = spacy.load("grc_odycy_joint_trf")

def lemmatize(path):
    data = []
    with open(path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    for row in data[1:]:
        text = row[3]
        doc = nlp(text)
        lemmas = [token.lemma_ for token in doc if not token.is_stop]
        lemmatized_text = ' '.join(lemmas)
        row.append(lemmatized_text)
    with open('CSV with Lemmas/'+path[10:-3] + 'with_lemma.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

for file in os.listdir('CSV Files'):
    print(file)
    lemmatize(os.path.join('CSV Files', file))
    print('done')

