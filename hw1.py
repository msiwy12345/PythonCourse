days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

workdays = days.copy()

workdays.remove('sunday')
workdays.remove('saturday')

print(workdays, days)