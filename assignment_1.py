import datetime as dt


class BirthDates:
    def __init__(self, name, surname, year, month, day):
        self.name = name
        self.surname = surname
        self.birth_date = dt.date(year, month, day)
        self.today = dt.date.today()

    def get_age_in_years(self):
        age = self.today.year - self.birth_date.year
        return 'Age in years: {} years'.format(age)

    def get_days_diff(self):
        birthday = dt.date(self.today.year, self.birth_date.month, self.birth_date.day)
        birthday_2 = dt.date(self.today.year + 1, self.birth_date.month, self.birth_date.day)
        days_left = ((birthday if birthday > birthday_2 else birthday_2) - self.today).days
        return '{} days left to your next birthday'.format(days_left)

    def get_info(self):
        return self.name.title(), self.surname.title(), self.get_age_in_years()


p1 = BirthDates('john', 'doe', 1999, 6, 8)
print(p1.get_age_in_years(), p1.get_days_diff(), p1.get_info())
