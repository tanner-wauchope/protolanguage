from plain_english.language.syntax.word_classes import word_classes


class InvalidToken(Exception):
    """
    Raised when a lexeme cannot be classified.
    """
    pass


def classify(lexeme):
    """
    :param lexeme: a lexeme that is possibly punctuated or numeric
    :return: the word class of the lexeme
    """
    for word_class in word_classes.values():
        if lexeme.lower() in word_class.KEYWORDS:
            return word_class
    for word_class in word_classes.values():
        if word_class.match(lexeme):
            return word_class
    raise InvalidToken(lexeme + ' is not a valid token.')


def tokenize(paragraph):
    """
    Replaces the lexemes in the paragraph with tokens.
    :param paragraph: sentences that contain lines that contain lexemes
    :return: sentences that contain lines that contain tokens
    """
    tokens = []
    for sentence in paragraph:
        tokens.append([])
        for line in sentence:
            tokens[-1].append([])
            for lexeme in line:
                word_class = classify(lexeme)
                token = word_class(lexeme)
                tokens[-1][-1].append(token)
    return tokens
