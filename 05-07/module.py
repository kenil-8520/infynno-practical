from datetime import datetime
from datetime import date

def date_format(date):
    datetimeobject = datetime.strptime(date,"%d/%m/%Y")
    new_format_1 = datetimeobject.strftime("%d %b %Y")
    formate = new_format_1.split(" ")
    if int(formate[0]) > 0 and int(formate[0]) == 1:
        formate[0] = str(formate[0])+"st"
    elif int(formate[0]) > 1 and int(formate[0]) == 2:
        formate[0] = str(formate[0])+"nd"
    elif int(formate[0]) > 2 and int(formate[0]) == 3:
        formate[0] = str(formate[0])+"rd"
    elif int(formate[0]) > 3 and int(formate[0]) < 21 or int(formate[0]) > 23:
        formate[0] = str(formate[0])+"th"
    elif int(formate[0]) > 20 and int(formate[0]) == 21:
        formate[0] = str(formate[0])+"st"
    elif int(formate[0]) > 21 and int(formate[0]) == 22:
        formate[0] = str(formate[0])+"nd"
    elif int(formate[0]) > 22 and int(formate[0]) == 23:
        formate[0] = str(formate[0])+"st"

    return " ".join(formate)


def fage(born):
    born = datetime.strptime(born, "%d/%m/%Y").date()
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month,born.day))
    return age
