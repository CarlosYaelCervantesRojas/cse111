from reference import Reference
from scripture import Scripture
from random import choice
import os

TEXT_INDEX = 0
BOOK_INDEX = 1
CHAPTER_INDEX = 2
VERSE_INDEX = 3
END_VERSE_INDEX = 4

def main():

    scriptures_compound_list = [
        # [text, book, chapter, verse, end_verse ?]
        ["For behold, this is my work and my glory—to bring to pass the immortality and eternal life of man.","Moses",1,39],
        ["And it came to pass that I, Nephi, said unto my father: I will go and do the things which the Lord hath commanded, for I know that the Lord giveth no commandments unto the children of men, save he shall prepare a way for them that they may accomplish the thing which he commandeth them.","1 Nephi",3,7],
        ["Therefore shall a man leave his father and his mother, and shall cleave unto his wife: and they shall be one flesh.","Genesis",2,24],
        ["Even so faith, if it hath not works, is dead, being alone. Yea, a man may say, Thou hast faith, and I have works: shew me thy faith without thy works, and I will shew thee my faith by my works.","James",2,17,18],
        ["And all saints who remember to keep and do these sayings, walking in obedience to the commandments, shall receive health in their navel and marrow to their bones; And shall find wisdom and great treasures of knowledge, even hidden treasures; And shall run and not be weary, and shall walk and not faint. And I, the Lord, give unto them a promise, that the destroying angel shall pass by them, as the children of Israel, and not slay them. Amen.","Doctrine and Covenants",89,18,21]
    ]

    reference, text_scripture = make_scripture(scriptures_compound_list)

    scripture = Scripture(reference, text_scripture)

    entry = ""
    number_to_hide = 0
    while (entry != "quit"):

        os.system("cls")

        print(scripture.get_display_text())

        entry = input("Press enter to continue or type 'quit' to finish: ")

        if scripture.is_completely_hidden():
            break

        number_to_hide += 3
        scripture.hide_random_words(number_to_hide)


def make_scripture(compound_list: list):

    scripture_list = choice(compound_list)

    text = scripture_list[TEXT_INDEX]

    book = scripture_list[BOOK_INDEX]
    chapter = scripture_list[CHAPTER_INDEX]
    verse = scripture_list[VERSE_INDEX]

    ref : Reference
    if len(scripture_list) == 5:
        end_verse = scripture_list[END_VERSE_INDEX]
        ref = Reference(book, chapter, verse, end_verse)
    else:
        ref = Reference(book, chapter, verse)

    return ref, text

    
if __name__ == "__main__":
    main()    