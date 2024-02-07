class Reference:

    def __init__(self, book: str, chapter: int, verse: int, endVerse: int = 0):
        self.__book = book
        self.__chapter = chapter
        self.__verse = verse
        self.__endVerse = endVerse

    def get_display_text(self):
        text = f"{self.__book} {self.__chapter}:{self.__verse}-{self.__endVerse}" if self.__endVerse != 0 else f"{self.__book} {self.__chapter}:{self.__verse}"
        return text