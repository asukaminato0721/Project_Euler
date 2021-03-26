from datetime import timedelta, date

begin = date(1901, 1, 1)
end = date(2000, 12, 31)
tdelta = end - begin


def main():
    return sum(
        (t := (begin + timedelta(days=i))).isoweekday() == 7 and t.day == 1
        for i in range(tdelta.days + 1)
    )


assert main() == 171