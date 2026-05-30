#the position class file

class Position:
    def __init__(self):
        self.column = "a"
        self.row = 1
        self.numeric = (0,0)

    def __str__(self):
        return self.column + str(self.row)

    @property
    def column(self):
        return self.column

    @column.setter
    def column(self, value):
        if type(value) == str:
            self.column = value
            if "a"<=value<="h":
                self.column = value
                self.numeric = self.toNumeric()
    @property
    def row(self):
        return self.row

    @row.setter
    def row(self, value):
        if type(value) == int:
            self.row = value

    def toNumeric(self):
        letter = ["a","b","c","d","e","f","g","h"]
        dictLetter = {}
        for i in range(8):
            dictLetter[letter[i]] = i
        rlt = (dictLetter[self.column],self.row-1)
        return rlt
