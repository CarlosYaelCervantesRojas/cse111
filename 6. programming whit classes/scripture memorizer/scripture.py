from word import Word
from reference import Reference
from random import choice

class Scripture:

    def __init__(self, reference: Reference, text: str):
        self.__reference = reference
        self.__words = []
        
        strings = []
        strings = text.split(" ")

        for str in strings:
            
            word = Word(str)
            self.__words.append(word)

    def hide_random_words(self, number_to_hide: int):

        for i in range(number_to_hide):

            word = choice(self.__words)
            word.hide()

    def get_display_text(self):

        scrip = ""
        reference = self.__reference.get_display_text()

        for word in self.__words:
            scrip += word.get_display_text() + " "

        return f"{reference} {scrip}"    
    
    def is_completely_hidden(self):

        is_compl_hidden = False
        
        hidden = 0
        for word in self.__words:
        
            if word.is_hidden():
            
                hidden += 1

        if hidden == len(self.__words):
        
            is_compl_hidden = True
        
        
        return is_compl_hidden