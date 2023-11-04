import random

def main():
    for _ in range(10):
        sentence = make_sentence()
        print(sentence)

def make_sentence():
    determiner = get_determiner()
    noun = get_noun()
    verb = get_verb()
    prepositional_phrase = get_prepositional_phrase()
    return f"{determiner} {noun} {verb} {prepositional_phrase}."

def get_determiner():
    determiners = ["A", "An", "The", "One", "Some", "Many"]
    return random.choice(determiners)

def get_noun():
    nouns = ["cat", "man", "woman", "girls", "dogs", "men", "bird", "child", "car", "rabbits", "children", "cats"]
    return random.choice(nouns)

def get_verb():
    verbs = ["talked", "drinks", "will run", "drank", "laugh", "will talk"]
    return random.choice(verbs)

def get_preposition():
    prepositions = ["for", "off", "on", "above", "at", "about"]
    return random.choice(prepositions)

def get_prepositional_phrase():
    preposition = get_preposition()
    determiner = get_determiner()
    noun = get_noun()
    return f"{preposition} {determiner} {noun}"

if __name__ == "__main__":
    main()
