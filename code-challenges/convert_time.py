# Function to convert 12-hour time to 24-hour time
def convert_to_24_hour(hour, minute, period):
    # Checking if the period is 'am'
    if period == "am":
        # Converting 12 am to 24-hour format (midnight)
        if hour == 12:
            hour = 0
    else:
        # Converting times in the afternoon to 24-hour format
        if hour != 12:
            hour += 12
    # Returning the time in 24-hour format as a four-digit string
    return f"{hour:02d}{minute:02d}"
