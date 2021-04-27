def acrobot(title, min_word_length = 0):
    acronym = []
    splitTitle = title.split()
    for word in splitTitle:
        if len(word) >= min_word_length:
            acronym.append(word[:1].capitalize())
    letters = ''.join(acronym)
    return letters
