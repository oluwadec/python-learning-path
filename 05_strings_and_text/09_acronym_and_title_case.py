"""09_acronym_and_title_case.py - Change how text looks."""

SMALL_WORDS = {"a", "an", "the", "and", "or", "of", "in", "on", "to", "for"}


def make_acronym(phrase: str) -> str:
    return "".join(word[0].upper() for word in phrase.split() if word)


def title_case(phrase: str) -> str:
    words = phrase.lower().split()
    result = []
    for i, word in enumerate(words):
        if i == 0 or word not in SMALL_WORDS:
            result.append(word.capitalize())
        else:
            result.append(word)
    return " ".join(result)


if __name__ == "__main__":
    print(make_acronym("as soon as possible"))
    print(make_acronym("north atlantic treaty organization"))
    print(title_case("the lord of the rings"))
    print(title_case("a tale of two cities"))
