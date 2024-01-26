def estimate_reading_time(text):
    if text == '':
        return 'Please provide a text.' 
    word_count = len(text.split())
    if word_count < 200:
        return 'Estimated reading time: less than a minute.'
    if word_count >= 200:
        time = word_count / 200
        hours = time//60
        minutes = time%60
        if hours < 1:
            return f'Estimated reading time: {round(minutes)} minutes.'
        elif hours == 1:
            return f'Estimated reading time: {round(hours)} hour and {round(minutes)} minutes.'
        elif hours > 1:
            return f'Estimated reading time: {round(hours)} hours and {round(minutes)} minutes.'
    



