import calendar
MM,DD,YYYY=map(int,input().split())
days=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
d=calendar.weekday(YYYY,MM,DD)
print(days[d])