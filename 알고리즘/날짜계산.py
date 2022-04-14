#Calculate the Days between Two Date
def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def Count_Days(year1, month1, day1):
    daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month1 ==2:
        if isLeapYear(year1):
            if day1 < daysOfMonths[month1-1]+1:
                return year1, month1, day1+1
            else:
                if month1 ==12:
                    return year1+1,1,1
                else:
                    return year1, month1 +1 , 1
        else: 
            if day1 < daysOfMonths[month1-1]:
                return year1, month1, day1+1
            else:
                if month1 ==12:
                    return year1+1,1,1
                else:
                    return year1, month1 +1 , 1
    else:
        if day1 < daysOfMonths[month1-1]:
             return year1, month1, day1+1
        else:
            if month1 ==12:
                return year1+1,1,1
            else:
                    return year1, month1 +1 , 1


def daysBetweenDates(y1, m1, d1, y2, m2, d2, end_day):
    """
    end_day: 시작일 포함 유무
    """
    if y1 > y2:
        m1,m2 = m2,m1
        y1,y2 = y2,y1
        d1,d2 = d2,d1
    days=0
    while(not(m1==m2 and y1==y2 and d1==d2)):
        y1,m1,d1 = Count_Days(y1,m1,d1)
        days+=1
    if end_day:
        days+=1
    return days


# Test Case

def test():
    test_cases = [((2015,1,1,2016,1,1,False), 365), 
                  ((2016,1,1,2017,1,1,False), 366),
                  ((2006,5,8,2022,4,3,False), 5809),
                  ((2011,1,1,2012,8,8,False), 585 ),
                  ((1994,5,15,2019,8,31,False), 9239),
                  ((1999,3,24,2018,2,4,False), 6892),
                  ((1999,6,24,2018,8,4,False),6981),
                  ((1995,5,24,2018,12,15,False),8606),
                  ((1994,8,24,2019,12,15,True),9245),
                  ((2019,12,15,1994,8,24,True),9245),
                  ((2019,5,15,1994,10,24,True),8970),
                  ((1994,11,24,2019,8,15,True),9031)
                 ]

    for (args, answer) in test_cases:
        print(answer)
        result = daysBetweenDates(*args)
        print(result)
        if result != answer:
            print("Test with data:", args, "failed")
        else:
            print("Test case passed!")

test()
# https://stackoverflow.com/questions/151199/how-to-calculate-number-of-days-between-two-given-dates