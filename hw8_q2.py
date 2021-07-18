import datetime
import jdatetime


#TODO : convert to seconds

class DifferenceTime:
    def __init__(self, d1, d2=None) -> None:
        try:
            self.d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
            print(d1)
        except ValueError:
            raise Exception("enter valid date")
        if d2 == None:
            self.d2 = datetime.datetime.today()
        else:
            try:
                self.d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
            except ValueError:
                raise Exception("enter valid date")

    def difference(self):
        return self.d2 - self.d1

    def jalali_dates(self):
        return jdatetime.datetime.fromgregorian(year=self.d1.year,
                                                month=self.d1.month, day=self.d1.day).strftime("%Y-%m-%d") \
            , jdatetime.datetime.fromgregorian(year=self.d2.year,
                                               month=self.d2.month, day=self.d2.day).strftime("%Y-%m-%d")

    def count_leap_year(self):
        leap_years = []
        for year in range(self.d1.year, self.d2.year):
            if year % 4 == 0 and year % 100 != 0:
                leap_years.append(year)
                break
        if len(leap_years) == 0:
            return 0
        counter = leap_years[0]
        while counter < self.d2.year:
            counter = counter + 4
            leap_years.append(counter)
        return len(leap_years)

    def clock_changes_number(self):
        start, end = self.jalali_dates()
        print(start)
        print(end)
        start = jdatetime.datetime.strptime(start, "%Y-%m-%d")
        end = jdatetime.datetime.strptime(end, "%Y-%m-%d")
        forward_counter = 0
        previuse_counter = 0
        if start.month < 7:
            previuse_counter += 1
        years = end.year - start.year
        previuse_counter += years
        forward_counter += years
        if end.month < 7:
            previuse_counter -= 1
        return forward_counter, previuse_counter


d = DifferenceTime("2010-12-19", "2010-12-18")
print(d.difference())
print(d.count_leap_year())
print(d.clock_changes_number())

