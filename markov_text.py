# -*- coding: iso-8859-1 -*-
#text generation with hmm

from random import ranint 


def read_text(file): 
  textfile = open(file)
  text = textfile.read()
  text = text.rstrip("\n")
  return text

def text_dict(text): 
  words = [i for i in text.split(' ') if i != ''] 
  dict = {word : [] for word in words}

  for before, after in zip(words, words[1:]):
    dict[before].append(after)

  return dict

def create_text(text_dict, seed, n_words):
  text = seed 
  for i in range(n_words): 
    seed = text_dict[seed][randint(0,len(text_dict[seed])-1)]
    text += ' '
    text += seed
  return text 

if __name__ == "__main__":
  text = read_text('hansel.txt')
  td = text_dict(text)
  new_text = create_text(td, 'Die', 50)
  print new_text

