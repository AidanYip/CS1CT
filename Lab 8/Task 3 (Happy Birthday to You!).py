import simpledate

def birthday(day, month):
    if day == 13 and month == 12:
        print("many happy returns!")
        return True
    else:
        print("a very merry unbirthday to you!")
        return False


print(birthday(simpledate.currentday(), simpledate.currentmonth()))
print(birthday(13, 12))
