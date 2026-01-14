# 1. Convert the time entered in hh,min and sec into seconds. 
hr = int(input("Enter hours: "))
min = int(input("Enter minutes: "))
sec = int(input("Enter seconds: "))

Total_sec = hr*3600+min*60+sec
print(f'{hr}Hr:{min}Min:{sec}Sec ===> in seconds are {Total_sec}')