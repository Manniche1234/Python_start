from hashlib import new
from pydoc import text
import string

class Text_container():



    def __init__(self,text):
        self.text = text


    def print(self):
        return self.text

    def count_words(self):
        words = self.text.split(" ")
        print(len(words))

    def count_chars(self):
        print(len(self.text))

    def count_ASCII(self):
        letters = []
        for letter in self.text:
           if letter in string.ascii_letters:
               letters.append(letter)
        print(len(letters))

    def remove_punctions(self):
        new_string = self.text.translate(str.maketrans('', '', string.punctuation))
        print(len(new_string))
        print(new_string)


if __name__=='__main__':
    tc = Text_container("hej8lkasd£asd læ123 <123ål1æ asd9123k asdlæk123 9asdlk@@@@1232a@aaa")
    tc.count_words()
    tc.count_chars()
    tc.count_ASCII()
    tc.remove_punctions()
    
