from gensim import corpora, models

def topic_modeling(texts):
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(t) for t in texts]
    lda_model = models.LdaModel(corpus, num_topics=3, id2word=dictionary, passes=10)
    return lda_model.print_topics()
