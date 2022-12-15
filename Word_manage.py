import pandas
import random

x = input("輸入檔名(數字):")
data = pandas.read_csv(f"C:/Users/user/OneDrive/桌面/背單字/單字庫/new_word_{x}.txt")
#data = pandas.read_csv(f"C:/Users/user/OneDrive/桌面/背單字/單字庫/test.txt")


class Word_manage:
    def __init__(self):
        self.word_book = {row.English: row.中文 for (index, row) in data.iterrows()}
        self.Wrong_word_book = {}
        self.Eng = str
        self.Che = str

    def next_word(self):
        if self.have_next_word():
            self.Eng = random.choice(list(self.word_book))
            self.Che = self.word_book[self.Eng]
            return True
        else:
            if self.refresh():
                self.next_word()
                return True
            else:
                return False

    def have_next_word(self):
        if len(self.word_book) > 0:
            return True
        else:
            return False

    def refresh(self):
        if len(self.Wrong_word_book) > 0:
            self.word_book = self.Wrong_word_book
            self.Wrong_word_book = {}
            return True
        else:
            return False
