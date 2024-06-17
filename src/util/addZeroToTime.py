def add_zero_to_time(time_str):
    if '.' in time_str:
        # Split the string into integer and decimal parts
        integer_part, decimal_part = time_str.split('.')
        # If there are more than two digits in the decimal part, trim it to two digits
        if len(decimal_part) > 2:
            decimal_part = decimal_part[:2]
        # If there is only one digit in the decimal part, add a zero
        elif len(decimal_part) == 1:
            decimal_part += '0'
        # If there is no decimal part or an empty string, set decimal part to '00'
        elif decimal_part == '':
            decimal_part = '00'
        # Concatenate the integer and decimal parts with a dot
        return f"{integer_part}.{decimal_part}"
    else:
        # If no decimal part found, add '.00' to the end
        return f"{time_str}.00"