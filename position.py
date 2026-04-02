#the position class file

class Position:
    def __init__(self,numeric = (0,0),pos = "a8"):
        self._numeric = numeric
        self._pos = pos
    @property
    def numeric(self) -> tuple:
        return self._numeric

    @numeric.setter
    def numeric(self,value):
        self._numeric = value
    @property
    def pos(self) -> str:
        return self._pos
    @pos.setter
    def pos(self,value):
        self._pos = value

    def toPos(self,value):
        if type(value) == str:
            alphabet = ["a","b","c","d","e","f","g","h"]
            dictNumber={}
            dictLetter={}
            for i in range(9):
                dictNumber[str(i)] = i
            for i in range(9):
                dictLetter[alphabet[i]] = i
        else:
            raise ValueError(f"The given position has to be of type 'str', given type was {type(value)}")





    def changePos(self,value):
        if type(value) == tuple:
            if 0 <= value[0] < 9 and 0 < value[1] < 9:
                self._numeric = value
                self._pos = self.toPos(value)
        elif type(value) == str:
            if "a" <= value[0] <= "h" and "0" <= value[1] < "9":
                self._pos = value
                self._numeric = self.toNumeric(value)