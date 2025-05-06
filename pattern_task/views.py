from model import Title
class Menu:
    def __init__(self, journal):
        self.journal = journal

    def render_menu(self):
        while True:
            menu = input('Menu:\n1-вывод статей\n2-добавить статью\n3-удалить статью\n0-выход')
            if menu == '1':
                self.journal.render()
            elif menu == '2':
                name_title = input('введите имя статьи')
                outhor_title = input('введите автора статьи')
                len_title = input('кол-во символов в статье')
                published = input('место публикации статьи')
                summary = input('краткое описание статьи')
                new_title = Title(name_title, outhor_title, len_title, published, summary)
                self.journal.add_title(new_title)
                print('***\nстатья добавлена\n***')
            elif menu == '3':
                name_title_del = input('введите имя статьи для удаления')
                self.journal.del_title(name_title_del)
            elif menu == '0':
                break