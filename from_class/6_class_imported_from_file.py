class ImportedClass:
    def __init__(self, color: str, maker: str):
        self.color = color
        self.maker = maker
        # linia de mai jos apeleaza modtoda direct din contructor
        self.year = self.print_variables()

    def print_variables(self):
        print(f"The color is: {self.color} and the maker is: {self.maker}")
        return 29
    def print_self_default(self):
        print(f"The self default is: {self.year}")