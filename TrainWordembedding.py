import os
from gensim.models import Word2Vec
from nltk.corpus import CategorizedPlaintextCorpusReader

corpus = CategorizedPlaintextCorpusReader('Lemma Text Files', r'.*\.txt', cat_pattern = r'(.*?)_.*')
texts = ""
for f in corpus.fileids():
    text = ' '.join(corpus.words(fileids=f))
    texts += text

def make_sentences(text):
    sentences = []
    sentence = []
    text = text.replace('.', ' . ')
    tokens = text.split()

    for word in tokens:
        word = word.replace('᾽', '' ).replace('῞', '')
        if word in [',', '\n', "'", "᾽", '']:
            continue
        elif word in [';', ':', '.']:
            if sentence:
                sentences.append(sentence)
                sentence = []
        else:
            sentence.append(word)
    return sentences

training_sentences = make_sentences(texts)

cbow_model = Word2Vec(training_sentences, vector_size=100, min_count=0, workers=4)
cbow_model.train(training_sentences, total_examples=len(training_sentences), epochs=20)
print(cbow_model.wv.key_to_index)
cbow_model.save("cbow.model")
cbow_model.wv.save("cbow_keyedvectors.kv")
