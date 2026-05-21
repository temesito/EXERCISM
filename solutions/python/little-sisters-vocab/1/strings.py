
def add_prefix_un(word):
    return "un" + word

def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    applied_words = [prefix] + [prefix + word for word in vocab_words[1:]]
    return " :: ".join(applied_words)
    
def remove_suffix_ness(word):
    root_word = word[:-4]
    if root_word.endswith("i"):
        return root_word[:-1] + "y"
    return root_word

def adjective_to_verb(sentence, index):
    words = sentence.split()
    target_word = words[index]
    return target_word.strip(".,!") + "en"






