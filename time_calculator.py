def add_time(start, duration, start_day=None):

    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # Parse start time
    start_time, period = start.split()
    start_hours, start_minutes = map(int, start_time.split(':'))

    # Convert to 24-hour format
    if period == "PM" and start_hours != 12:
        start_hours += 12
    elif period == "AM" and start_hours == 12:
        start_hours = 0

    # Parse duration time
    duration_hours, duration_minutes = map(int, duration.split(':'))

    # Calculate new time
    new_minutes = start_minutes + duration_minutes
    extra_hours = new_minutes // 60
    new_minutes %= 60

    new_hours = start_hours + duration_hours + extra_hours
    days_later = new_hours // 24
    new_hours %= 24

    # Convert back to 12-hour format
    new_period = "AM" if new_hours < 12 else "PM"
    new_hours = new_hours % 12 if new_hours % 12 != 0 else 12  # Handle 12 AM and 12 PM correctly

    # Format new time
    new_time = f"{new_hours}:{new_minutes:02d} {new_period}"

    # Handle day of the week
    if start_day:
        start_day = start_day.capitalize()
        day_index = days_of_week.index(start_day)
        new_day = days_of_week[(day_index + days_later) % 7]
        new_time += f", {new_day}"


    # Handle days later notation
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"



    return new_time

# Test cases
print(add_time('3:30 PM', '2:12'))  # Should return '5:42 PM'
print(add_time('11:55 AM', '3:12'))  # Should return '3:07 PM'
print(add_time('2:59 AM', '24:00'))  # Should return '2:59 AM (next day)'
print(add_time('11:59 PM', '24:05'))  # Should return '12:04 AM (2 days later)'
print(add_time('8:16 PM', '466:02'))  # Should return '6:18 AM (20 days later)'


print(add_time('3:30 PM', '2:12'))

print(add_time('3:30 PM', '2:12', 'Monday'))
print(add_time('2:59 AM', '24:00', 'saturDay'))
