import re
from intentparser.utils import *

__author__ = 'Nonthakon Jitchiranant'

REQUIRE = 0
OPTIONAL = 1
REGEX = 2

class intentParser(object):
    def __init__(self, construct, typeOfSim='jaccard'):
        self.construct = construct
        self.description = self.construct["description"]
        assert type(self.description["type"]) == str, "Type need to be str!"
        assert type(self.description["args"]) == list, "Args need to be list!"
        assert type(self.description["keyword"]) == list, "Keyword need to be list!"
        self.type = self.description["type"]
        self.args = self.description["args"]
        self.keyword = self.description["keyword"]
        self.BigList = []
        self.SmallList = []
        self.know_words = []
        self.know_words_remove_stopwords = []
        self.typeOfSim = typeOfSim

        for i in self.keyword:
            if i[0] == 0:
                self.BigList.append([0, i[1], self.construct[i[1]]])
            elif i[0] == 1:
                self.BigList.append([1, i[1], self.construct[i[1]]])
            elif i[0] == 2:
                self.BigList.append([2, i[1], self.construct[i[1]]])
                """
                BigList should be like
                [(0, "weather_keyword", ['weather']),
                (1, "weather_types", ["snow", "rain", "wind", ...]),
                (2, "location", 'in (?P<location>.*)')]
                """
        for i in self.args:
            if i[0] == 0:
                self.SmallList.append([0, i[1], self.construct[i[1]]])
            elif i[0] == 1:
                self.SmallList.append([1, i[1], self.construct[i[1]]])
            elif i[0] == 2:
                self.SmallList.append([2, i[1], self.construct[i[1]]])

                """
                SmallList should be like
                [(0, "location", 'in (?P<location>.*)'), (1, "weather_types", ["snow" ...])]
                """
    def teachWords(self, list_of_word):
        assert type(list_of_word) == list, "list of word need to be list"
        self.know_words.extend(list_of_word)
        for i in list_of_word: #Remove all stop words
            i = remove_stopwords(i)
            self.know_words_remove_stopwords.append(i)

    def getTextConfidence(self, text):
        if self.typeOfSim == 'jaccard':
            intend_confidenceList = []
            for i in self.know_words:
                intend_confidenceList.append(jaccard_compare(text, i))
            if len(self.know_words) > 0:
                return max(intend_confidenceList)
            else :
                return 0
        elif self.typeOfSim == 'gensim':
            try:
                from gensim import corpora, models, similarities
            except Exception as e:
                print(e)
            dictionary = corpora.Dictionary(self.know_words_remove_stopwords)
            corpus = [dictionary.doc2bow(text) for text in self.know_words_remove_stopwords]
            lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)
            new_doc = text
            vec_bow = dictionary.doc2bow(new_doc.lower().split())
            vec_lsi = lsi[vec_bow]
            index = similarities.MatrixSimilarity(lsi[corpus])
            sims = index[vec_lsi]
            sims = sorted(enumerate(sims), key=lambda item: -item[1])
            most_sim = sims[0]
            return most_sim[1]

    def getResult(self, text):
        intersectBigSmall = intersect(self.BigList, self.SmallList)
        text.lower()
        text_list = tokenize(text)
        require_text = []
        return_args = []
        for i in self.BigList:
            if i[0] == 0:
                for j in i[2]:
                    require_text.append(j)
        if len(intersect(require_text, text_list)) != 0:
            for i in self.SmallList:
                if i[0] == 2:
                    regex = i[2]
                    regex_word = re.findall(regex, text)
                    try:
                        if len(regex_word) >= 0:
                            return_args.append((i[1], regex_word))
                    except Exception as e:
                        return {"confidence" : self.getTextConfidence(text),
                                "type" : self.type,
                                "args" : return_args}
                elif i[0] == 1:
                    optinal_list = intersect(text_list, i[2])
                    if len(optinal_list) > 0:
                        return_args.append((i[1], optinal_list))
                    else :
                        pass
            return {"confidence" : self.getTextConfidence(text),
                    "type" : self.type,
                    "args" : return_args}
        else:
            return {"confidence" : 0}
