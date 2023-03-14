from datetime import datetime

time_data = "23/01/2022"
format_data = "%d/%m/%Y"
date=datetime.strptime(time_data,format_data)


print(date.strftime('%Y-%m-%d'))