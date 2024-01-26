def estimate_reading_time(text):
    if text == '':
        return 'Please provide a text.' 
    word_count = len(text.split())
    if word_count < 200:
        return 'Estimated reading time: less than a minute.'
    if word_count >= 200:
        time = word_count / 200
        hours = round(time//60)
        minutes = round(time%60)
        if hours < 1:
            return f'Estimated reading time: {minutes} minutes.'
        elif hours == 1:
            return f'Estimated reading time: {hours} hour and {minutes} minutes.'
        elif hours > 1:
            return f'Estimated reading time: {hours} hours and {minutes} minutes.'
    



