def add_time(start, duration, day = ''):
  time = start.split(':')
  time_hours = int(time[0])
  time_minutes = int(time[1].split()[0])
  time_frame = time[1].split()[1]
  
  add = duration.split(':')
  add_hours = int(add[0])
  add_minutes = int(add[1])
  
  new_minutes = (time_minutes + add_minutes) % 60
  new_hours = int((time_minutes + add_minutes) / 60) + time_hours + add_hours
  half_days = int(new_hours/12)
  new_hours = new_hours % 12
  if new_hours == 0:
    new_hours = 12
  
  days_count = 0
  
  for i in range(half_days):
    if time_frame == 'PM':
      time_frame = 'AM'
      days_count += 1
    else:
      time_frame = 'PM'
      
  message = ''
  if days_count == 1:
    message = ' (next day)'
  elif days_count > 1:
    message = f' ({days_count} days later)'
  
  days = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}
  nDays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
  new_day = ''
  if day != '':
    current_day_num = days[day.lower()]
    new_day_num = current_day_num + days_count
    if new_day_num > 6:
      new_day_num = new_day_num % 7
    new_day = nDays[new_day_num]
  
  new_time = ''
  if new_day != '':
    new_time = str(new_hours) + ':' + '{:02d}'.format(new_minutes) + ' ' + time_frame + ', ' + new_day + message
  else:
    new_time = str(new_hours) + ':' + '{:02d}'.format(new_minutes) + ' ' + time_frame + message
  
  return new_time