print('Welcome to the which season program')

month_string=input("number of the month: ")
day_string=input("day of the month: ")

month=int(month_string)
day=int(day_string)

if month==1 or month==2 or month==3:
    season = 'winter'
elif month==4 or month==5 or month==6:
    season='spring'
elif month==7 or month==8 or month==9:
    season='summer'
elif month==10 or month==11 or month==12:
    season='autumn'
else:
    season='invalid'

if (month==3) and (day>19):
    season='spring'
elif (month==6) and (day>20):
    season='summer'
elif (month==9) and (day>21):
    season='autumn'
elif (month==12) and (day>20):
    season='winter'

print("Season is", season)
