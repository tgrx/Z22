from homeworks.yan_romanovich.lesson11 import level03


class User(level03.User):
    def validate(self):
        if not self.email:
            raise ValueError
        elm = str(self.email).index("@")
        lst1 = str(self.email[:elm])
        if not str(self.email[elm + 1 :]):
            raise ValueError
        lst2 = str(self.email[elm + 1 :])
        if not (self.name and lst1):
            raise ValueError
        if not (
            self.name.isalnum()
            and "a" <= self.name <= "z"
            and lst1.isalnum()
            and "a" <= lst1 <= "z"
        ):
            raise ValueError
        if not (self.name[0].isalpha() and lst1[0].isalpha()):
            raise ValueError
        if not lst2[0].isalpha():
            raise ValueError
        if lst2[0] == "." or lst2[-1] == ".":
            raise ValueError
        if "@" in lst2:
            raise ValueError
