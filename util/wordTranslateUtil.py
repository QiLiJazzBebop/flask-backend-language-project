from word2word import Word2word

en2jaModel = Word2word("en", "ja")
ja2enModel = Word2word("ja", "en")


def en2ja(word):
    return en2jaModel(word)


def ja2en(word):
    return ja2enModel(word)
