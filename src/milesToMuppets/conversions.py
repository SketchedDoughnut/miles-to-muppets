'''
These are a bunch of functions for unit conversions.
'''

# converts hours to millisecond
def hourToMs(hour: float) -> float:
    '''
    converts hours to milliseconds
    '''
    # hour to min
    minute = hour * 60
    # min to second
    second = minute * 60
    # second to ms
    ms = second * 1000
    return ms

# converts milliseconds to hour
def msToHour(ms: float) -> float:
    '''
    converts milliseconds to hours
    '''
    # ms to second
    second = ms / 1000
    # second to minute
    minute = second / 60
    # minute to hour
    hour = minute / 60
    return hour

# converts minutes to milliseconds
def minuteToMs(minute: float) -> float:
    '''
    converts minutes to milliseconds
    '''
    # minute to second
    second = minute * 60
    # second to ms
    ms = second * 1000
    return ms

# converts milliseconds to minutes
def msToMinute(ms: float) -> float:
    '''
    converts milliseconds to minutes
    '''

    # ms to second
    second = ms / 1000
    # second to minute
    minute = second / 60
    return minute

# converts minutes to hours
def minuteToHour(minute: float) -> float:
    '''
    converts minutes to hours
    '''

    # minute to hour
    hour = minute / 60
    return hour