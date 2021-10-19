def add_time(start, duration, Day = None):
    timeofday= start.split()
    start_numbers = timeofday[0].split(':')
    start_numbers.append(timeofday[1])
    numbers = duration.split(':')

# Function to convert the time.
    def twelve_below(time, increase):
        hour = int(time[0]) + int(increase[0])
        if time[1][0] == '0' and numbers[1][0] == '0':
            minute = int(time[1][1]) + int(increase[1][1])
        elif int(time[1][0]) == 0:
            minute = int(time[1][1]) + int(increase[1])
        elif int(time[1][0]) == 0:
            minute = int(time[1]) + int(increase[1][1])
        else:
            minute = int(time[1]) + int(increase[1])

        if minute >= 60:
            minute -= 60
            hour += 1
        
        if minute < 10:
            minute = f"0{minute}"
        else:
            minute = minute

        if hour >= 12 and 'PM' in time:
            if hour > 12: hour -= 12
            else: hour = 12
            return [f'{hour}', f"{minute}", 'AM', '(next day)']
        elif hour >= 12 and 'AM' in time:
            if hour > 12: hour -= 12
            else: hour = 12
            return [f'{hour}', f"{minute}", 'PM']
        else:
            return [f'{hour}', f"{minute}", time[2]]

#Main Code
    if int(numbers[0]) <= 12:
        date = twelve_below(start_numbers, numbers)
        if '(next day)' in date: 
            return f"{date[0]}:{date[1]} {date[2]} {date[3]}"
        else:
            return f"{date[0]}:{date[1]} {date[2]}"
    elif int(numbers[0]) < 24:
        numbers[0] = str(int(numbers[0]) - 12)
        twelve = twelve_below(start_numbers, ['12', '00'])
        two_four = twelve_below(twelve, numbers)
        return f"{two_four[0]}:{two_four[1]} {two_four[2]} (next day)"
    elif int(numbers[0]) >= 24:
        days = int(numbers[0]) // 24
        numbers[0] = int(numbers[0])% 24
        if int(numbers[0]) <= 12:
            date = twelve_below(start_numbers, numbers)
            if days == 1 and '(next day)' in date:
                return f"{date[0]}:{date[1]} {date[2]} (2 days later)"
            elif days ==1 and '(next day)' not in date:
                return f"{date[0]}:{date[1]} {date[2]} (next day)"
            elif days > 1 and '(next day)' in date:
                return f"{date[0]}:{date[1]} {date[2]} ({days + 1} days later)"
            else:
                return f"{date[0]}:{date[1]} {date[2]} ({days} days later)"
        else:
            numbers[0] = str(int(numbers[0]) - 12)
            twelve = twelve_below(start_numbers, ['12', '00'])
            two_four = twelve_below(twelve, numbers)
            return f"{two_four[0]}:{two_four[1]} {two_four[2]} ({days + 1} days later)"
