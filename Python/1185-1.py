class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        months = [31,28,31,30,31,30,31,31,30,31,30,31];
        y = 1970
        sum  = 0
        while y < year:
            sum += 365
            if self.leapYear(y):
                sum += 1
            y += 1
        m = 1
        while m < month:
            sum += months[m - 1]
            if m == 2 and self.leapYear(year):
                sum += 1
            m += 1
        sum += day
        sum = sum % 7
        return days[(4 + sum) % 7]
    def leapYear(self, year):
        if year % 400 == 0:
            return True
        if year % 4 == 0 and year % 100 != 0 :
            return True
        return False

