class Feed:
    def __init__(self):
        self.song = 0

    class Post:
        def __init__(self, outer):
            self.outer = outer

        def set_value(self, new_value):
            self.outer.value = new_value

    def set_inner_value(self, new_value):
        self.inner = self.Post(self)
        self.inner.set_value(new_value)

# if __name__ == '__main__':
#     my_class = MyClass()
#     my_class.set_inner_value(5)
#     print(my_class.value) # output: 5
