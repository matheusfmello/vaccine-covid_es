import pandas as pd
from datetime import datetime
from datetime import date

def convert_to_datetime(x):
    try:
        return(datetime.strptime(str(x),'%Y-%m-%d'))
    except:
        return(datetime.strptime('3000-01-01','%Y-%m-%d'))


# checks if 2nd shot was taken in time, and also if deadline was reached.
# returns a column with values {0:'2nd shot late', 1:'2nd shot taken', 2:'2nd shot deadline not reached yet'}

def took_shot(shot1, shot2, vaccine, deadlines={'CORONAVAC':60, 'ASTRAZENECA':120, 'PFIZER':120, 'JANSSEN':120}):
    today = datetime.strptime(date.today().strftime('%Y-%m-%d'), "%Y-%m-%d")
    erro = datetime.strptime('3000-01-01','%Y-%m-%d')
    result = []
    for i in range(0, len(shot1)):
        # when not above deadline
        if (today - shot1[i]).days < deadlines[vaccine[i]]:
            if(shot2[i] == erro):
                result.append(2)
            else:
                result.append(1)
        else:
            if(shot2[i] == erro):
                result.append(0)
            else:
                result.append(1)

    return result