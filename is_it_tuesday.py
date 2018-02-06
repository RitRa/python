# Rita Raher 5 feb 2017
# Is it Tuesday?

import datetime

z = datetime.datetime.today().weekday()

if( z == 1 ):
    print("Yay!!! It is Tuesday")
else:
    print("Not Tuesday, boooooo")
