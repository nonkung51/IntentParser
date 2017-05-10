def jaccard_compare(text1, text2):
    text1 = remove_stopwords(text1)
    text2 = remove_stopwords(text2)
    same_word = []
    for i in text1:
        for j in text2:
            if i == j:
                same_word.append(text1)
    return len(same_word) / ((len(text1) + len(text2)) /2)

def remove_stopwords(text):
    text = tokenize(text)
    text_return = []
    stop_words = ['ไว้', 'ไม่', 'ไป', 'ได้', 'ให้', 'ใน', 'โดย', 'แห่ง', 'แล้ว', 'และ', 'แรก', 'แบบ', 'แต่', 'เอง', 'เห็น', 'เลย', 'เริ่ม', 'เรา']
    for word in text:
        if word not in stop_words:
            text_return.append(word)
    return text_return

def tokenize(text):
    from pythainlp.segment import segment
    return segment(text)

def intersect(a, b):
     return [val for val in a if val in b]
