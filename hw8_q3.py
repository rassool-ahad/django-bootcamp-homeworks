import datetime
import calendar


def weekday_count(s_day, e_day, w_day):
    day_dict = {0: "Saturday",
                1: "Sunday",
                2: "Monday",
                3: "Tuesday",
                4: "Wednesday",
                5: "Thursday",
                6: "Friday"
                }
    start_date = datetime.datetime.strptime(s_day, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(e_day, "%Y-%m-%d")
    week = {}
    for i in range((end_date - start_date).days):
        day = calendar.day_name[(start_date + datetime.timedelta(days=i + 1)).weekday()]
        if day_dict[w_day] == day:
            yield (start_date + datetime.timedelta(days=i + 1)).date()
        # week[day] = week[day] + 1 if day in week else 1
    return week


# weekday_count(, 1)
for i in weekday_count("2010-05-19", "2018-04-15",1):
    print(i)