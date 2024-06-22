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
    mins = time // 60
    hours = mins // 60

    # Ensure proper time format based on duration of timer
    if hours:
      return(f"{int(hours):2d}:{int(mins):02d}:{int(secs):02d}.{int((time % 1) * 100):02d}")
    if mins:
      return(f"{int(mins):2d}:{int(secs):02d}.{int((time % 1) * 100):02d}")
    if secs:
      return(f"{int(secs)}.{int((time % 1) * 100):02d}")