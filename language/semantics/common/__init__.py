from language.syntax.parse import Word
from language.semantics import Noun, Verb

class Preposition(Word):
    """ before, after """
    SPECIFIES = [Noun]
    COMPLEMENTS = [Noun, Copula]


class Operator(Preposition):
    """ plus, minus, times, over """
    COMPLEMENTS = [Noun]


class Complementizer(Word):
    SPECIFIES = [Verb]


class Subordinator(Word):
    REQUIRES_SPECIFIER = True
    REQUIRES_COMPLEMENT = True