# Ques: To append, delete, display element of a list using classes

class ListMethod:
    def __init__(self, l):
        self.li = l
        print(*self.li)

    def append_value(self, value):
        self.li.append(value)

    def display_list(self):
        print(*self.li)

    def delete_value(self, value):
        self.li.remove(value)


l = [1, 2, 3, 4]
obj = ListMethod(l)
obj.append_value(value=5)
obj.append_value(value=7)
obj.append_value(value=9)
obj.display_list()
obj.delete_value(value=3)
obj.display_list()
obj.delete_value(value=7)
obj.display_list()
