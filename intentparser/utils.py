def jaccard_compare(text1, text2):
    #from nltk.tokenize import TweetTokenizer
    #tknzr = TweetTokenizer()
    text1 = remove_stopwords(text1)
    text2 = remove_stopwords(text2)
    same_word = []
    for i in text1:
        for j in text2:
            if i == j:
                same_word.append(text1)
    return len(same_word) / ((len(text1) + len(text2)) /2)

def remove_stopwords(text):
    from nltk.corpus import stopwords
    from nltk.tokenize import TweetTokenizer
    stop_words = stopwords.words('english')
    tknzr = TweetTokenizer()
    text = tknzr.tokenize(text.lower())
    text_return = []
    for word in text:
        if word not in stop_words:
            text_return.append(word)
    return text_return

def tokenize(text):
    from nltk.tokenize import TweetTokenizer
    tknzr = TweetTokenizer()
    text = tknzr.tokenize(text.lower())
    return text

def intersect(a, b):
     return [val for val in a if val in b]
