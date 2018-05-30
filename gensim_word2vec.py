# -*- coding:utf-8 -*-
from gensim.models import word2vec
import gensim
import jieba

# sentences = word2vec.Text8Corpus("wiki.zh.sm.txt")
# model = word2vec.Word2Vec(sentences, size=100)
# model.save("corpus_wiki.model")
#
if __name__ == "__main__":
    model = word2vec.Word2Vec.load("corpus_wiki.model")
    model2 = word2vec.Word2Vec.load("corpus.model")
    print(model.most_similar(u'投资'))
    print(model2.most_similar(u'投资'))