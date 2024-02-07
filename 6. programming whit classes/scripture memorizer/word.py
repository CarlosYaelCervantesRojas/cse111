class Word:

    def __init__(self, text: str):
        self.__text = text
        self.__is_hidden = False

    def hide(self):
        self.__is_hidden = True

    def show(self):
        self.__is_hidden = False

    def is_hidden(self):
        return self.__is_hidden
    
    def get_display_text(self):
        
      if self.__is_hidden == True:
        text = ""
        for letter in self.__text:
            text += "_"
        return text
      
      else:
          return self.__text
        
    
