def format_duration(seconds):
    if seconds == 0: return "now"

    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    years, days = divmod(days, 365)

    times = [years,days,hours,minutes,seconds]
    time_names = ["year","day","hour","minute","second"]
    
    duration_list = []
    
    for index, time in enumerate(times):
        if time == 1:
            duration_list.append(f"{time} {time_names[index]}")
        elif time > 1:
            duration_list.append(f"{time} {time_names[index]}s")
            
    if len(duration_list) == 1:
        return f"{duration_list[0]}"
    elif len(duration_list) == 2:
        return f"{duration_list[0]} and {duration_list[1]}"
    else:
        return ", ".join(duration_list[:-1]) + " and " + duration_list[-1]