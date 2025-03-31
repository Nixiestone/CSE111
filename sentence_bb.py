import random

def get_determiner(quantity):
  """Return a randomly chosen determiner. A determiner is
  a word like "the", "a", "one", "some", "many".
  If quantity is 1, this function will return either "a",
  "one", or "the". Otherwise this function will return
  either "some", "many", or "the".
  Parameter
      quantity: an integer.
          If quantity is 1, this function will return a
          determiner for a single noun. Otherwise this
          function will return a determiner for a plural
          noun.
  Return: a randomly chosen determiner.
  """
  if quantity == 1:
      words = ["a", "one", "the"]
  else:
      words = ["some", "many", "the"]
  # Randomly choose and return a determiner.
  word = random.choice(words)
  return word

def get_noun(quantity):
    if quantity == 1 :
        nouns = ["bird","boy","car","cat","children","dog","girl","man","rabbit","woman"]
    else:
        nouns = ["birds", "boys", "cars", "cats", "children","dogs", "girls", "men", "rabbits", "women"]
    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    if tense == past:
        verbs = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    elif tense == present: 
        if quantity==1:
            verbs= ["drinks", "eats", "grows", "laughs", "thinks","runs", "sleeps", "talks", "walks", "writes"]
    elif tense == present:
        if quantity != 1:
            verbs=["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    elif tense == future:
        verbs=["will drink", "will eat", "will grow", "will laugh","will think", "will run", "will sleep", "will talk","will walk", "will write"]
    else:
        raise ValueError(" Invalid tense. Must be past, present, or future.")
    
    return random.choice(verbs)

def make_sentence(quantity, tense):
     """Build and return a sentence with three words:
  a determiner, a noun, and a verb. The grammatical
  quantity of the determiner and noun will match the
  number in the quantity parameter. The grammatical
  quantity and tense of the verb will match the number
  and tense in the quantity and tense parameters.
  """
determiner = get_determiner(quantity)
noun = get_noun(quantity)
verb = get_verb(quantity, tense)

sentence = f"{determiner.capitalize} {noun} {verb}."
return sentence

def main():
    print(sentence(1,"past"))
    print(sentence(1,"present"))
    print(sentence(1,"future")) 
    print(sentence(2,"past"))
    print(sentence(2,"present"))
    print(sentence(2,"future"))
    
    
if __name__ =="__main__":
    main()