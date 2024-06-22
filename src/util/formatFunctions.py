def add_zero_to_time(time_str):
    if '.' in time_str:
        integer_part, decimal_part = time_str.split('.')

        if len(decimal_part) > 2:
            decimal_part = decimal_part[:2]
        elif len(decimal_part) == 1:
            decimal_part += '0'
        elif decimal_part == '':
            decimal_part = '00'

        return f"{integer_part}.{decimal_part}"
    else:
        return f"{time_str}.00"


def formatTime(time):
    secs = time % 60
    mins = (time // 60) % 60
    hours = time // 3600

    # Ensure proper time format based on duration of timer
    if hours:
        return f"{int(hours):d}:{int(mins):02d}:{int(secs):02d}.{int((time % 1) * 100):02d}"
    elif mins:
        return f"{int(mins):d}:{int(secs):02d}.{int((time % 1) * 100):02d}"
    else:
        return f"{int(secs)}.{int((time % 1) * 100):02d}"


def formatStringToSeconds(time):
    time_parts = time.split(":")

    if len(time_parts) == 3:
        hours = float(time_parts[0])
        minutes = float(time_parts[1])
        seconds = float(time_parts[2])
    elif len(time_parts) == 2:
        hours = 0
        minutes = float(time_parts[0])
        seconds = float(time_parts[1])
    elif len(time_parts) == 1:
        hours = 0
        minutes = 0
        seconds = float(time_parts[0])
    else:
        raise ValueError("Invalid time format. Must be in 'hh:mm:ss.sss' or 'mm:ss.sss' format.")

    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds