class Jornal:
    def __init__(self, name):
        self.name = name 
        self.list_title = []

    def add_title(self, new_title):
        self.list_title.append(new_title)
    
    def del_title(self, name_title):
        for index_title in range(len(self.list_title)):
            if self.list_title[index_title].name_title == name_title:
                obj = self.list_title[index_title]
                self.list_title.pop(index_title)
                del obj
                print('***\nстатья удалена успешно\n***')
                return self
            else:
                print('тфкой строки нет ')

    def render(self):
        num = 1
        str_ = 'список статей\n'
        for title in self.list_title:
            str_ += f'{num}. {title.name_title}\n'
            num += 1
        str_ += '___'
        print(str_)

class Title:
    def __init__(self, name_title, outhor_title, len_title, published, summary):
        self.name_title = name_title
        self.outhor_title = outhor_title
        self.len_title = len_title
        self.published =published 
        self.summary = summary