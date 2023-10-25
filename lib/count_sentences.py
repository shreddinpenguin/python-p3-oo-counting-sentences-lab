#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if type(value) is str:
      self._value = value
    else:
      print("The value must be a string.")
    
  def is_sentence(self):
    return self._value.endswith(".")
 
  def is_question(self):
    return self._value.endswith("?")
  
  def is_exclamation(self):
    return self._value.endswith("!")
  
  def count_sentences(self):
    value = self._value
    sentences = 0
    for letter in value:
      if letter.endswith((".", "!", "?")):
        print(letter)
        sentences += 1
    return sentences
    
string = MyString()
string.value = "This, well, is a sentence. This is too!! And so is this, I think? Woo..."
print(string.count_sentences())


    