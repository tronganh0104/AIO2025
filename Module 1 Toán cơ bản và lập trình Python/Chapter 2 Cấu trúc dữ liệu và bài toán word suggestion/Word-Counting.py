def processing(sentence: str):
    sentence = sentence.lower()
    sentence = sentence.replace(',', '')
    sentence = sentence.replace('.', '')
    words = sentence.split()
    return words

def count_word(file_path):
    with open(file_path, 'r') as f:
        document = f.read()
    words = processing(document)
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result