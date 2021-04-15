sec = int(input('введите секунды'))
if sec <= 60:
    minutes = sec // 60
if sec <= 3600:
    hours = sec // 3600
if sec <= 86400:
    days = sec // 86400
print('хоурс', hours, ': минутес', minutes, ': дэйс', days)