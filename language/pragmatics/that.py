from plain_english.language.pragmatics.verbs import Clause


class Complementizer:
    def __getattr__(self, item):
        return Clause(verb=item)
