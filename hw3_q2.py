from datetime import datetime

class birthday():
    def __init__(self,yearofbirth:int,monthofbirth:int,dayofbirth:int,hourofbirth:int, format='gregorian') -> None:
        self.hoeur = hourofbirth
        if format == 'gregorian':
            self.year = yearofbirth
            self.month = monthofbirth
            self.day = dayofbirth
        elif format == 'jalali':
            grogian_list = self.__jalali_to_gregorian(yearofbirth,monthofbirth,dayofbirth)
            self.year = grogian_list[0]
            self.month = grogian_list[1]
            self.day = grogian_list[2]
        else:
            assert False, '<format must be gregorian or jalali>'
        # self.__check(self.year, self.month, self.day, self.hoeur)

    @staticmethod
    def __check(year, month, day, hour):
     pass

    @staticmethod
    def __jalali_to_gregorian(jy, jm, jd):
        jy += 1595
        days = -355668 + (365 * jy) + ((jy // 33) * 8) + (((jy % 33) + 3) // 4) + jd
        if jm < 7:
            days += (jm - 1) * 31
        else:
            days += ((jm - 7) * 30) + 186
        gy = 400 * (days // 146097)
        days %= 146097
        if days > 36524:
            days -= 1
            gy += 100 * (days // 36524)
            days %= 36524
            if days >= 365:
                days += 1
        gy += 4 * (days // 1461)
        days %= 1461
        if days > 365:
            gy += ((days - 1) // 365)
            days = (days - 1) % 365
        gd = days + 1
        if (gy % 4 == 0 and gy % 100 != 0) or (gy % 400 == 0):
            kab = 29
        else:
            kab = 28
        sal_a = [0, 31, kab, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        gm = 0
        while gm < 13 and gd > sal_a[gm]:
            gd -= sal_a[gm]
            gm += 1
        return [gy, gm, gd]

    def age_yearFormat(self) -> int:
        __age = datetime.now().year - self.year
        if datetime.now().month < self.month:
            __age += 1
        elif datetime.now().month == self.month:
            if datetime.now().day < self.day:
                __age += 1
            elif datetime.now().day == self.day:
                if datetime.now().time().hour < self.hoeur:
                    __age += 1
        return __age

    def age_hourformat(self) -> int:
        __age = (self.age_yearFormat())*365*24
        __age += abs(self.month - datetime.now().month)*30*24
        __age += abs(self.day - datetime.now().day)*24
        __age += abs(self.hoeur - datetime.now().time().hour)
        return __age

    def timeRemainsToBirthday(self):
        mounthsRemain = 12 - datetime.now().month + self.month
        if self.day - datetime.now().day >= 0:
            daysRemain = self.day - datetime.now().day
        else :
            mounthsRemain -= 1
            daysRemain = 30 - datetime.now().day + self.day
        if self.hoeur - datetime.now().hour >= 0:
            hoursremain = self.hoeur - datetime.now().hour
        else:
            daysRemain -= 1
            hoursremain = 24 - datetime.now().hour + self.hoeur
        return f'{mounthsRemain} month and {daysRemain} days and {hoursremain} hours remains to your bitrhday'

a= birthday(2021, 4, 20 ,18)
print(a.age_yearFormat())
print(a.age_hourformat())
print(a.timeRemainsToBirthday())


