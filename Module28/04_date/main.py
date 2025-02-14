class Date:
    def __init__(self, day: str, month: str, year: str) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return "День: {}	Месяц: {}	Год: {}".format(
            self.day, self.month, self.year
        )

    @classmethod
    def from_string(cls, form_data: str) -> "Date":
        result = form_data.split("-")
        day, month, year = result[0], result[1], result[2]
        total_result = cls(day, month, year)
        return total_result

    @classmethod
    def is_date_valid(cls, form_data: str) -> bool:
        result = form_data.split("-")
        day, month, year = result[0], result[1], result[2]
        if 0 < int(day) <= 31 and 0 < int(month) <= 12 and 0 < int(year) <= 2077:
            return True
        return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

# зачет!
