'''
In this Bite you read in a text file with course times (MM:SS) per video.
You extract these and calculate the total course duration in HH:MM:SS.
'''

import datetime
import os
import re
import urllib.request

# getting the data
COURSE_TIMES = os.path.join('/tmp', 'course_timings')
urllib.request.urlretrieve('http://bit.ly/2Eb0iQF', COURSE_TIMES)

#Regex
times = re.compile('\d+\:\d+') # Pulls times from text file

def get_all_timestamps():

    with open(COURSE_TIMES) as f:
        timestamps = f.read()
        timestamps = re.findall(times, timestamps)
    return timestamps


def calc_total_course_duration(timestamps):
    sum = datetime.timedelta()
    for i in timestamps:
        (m, s) = i.split(':')
        d = datetime.timedelta(minutes=int(m), seconds=int(s))
        sum += d
    return (str(sum))

print(test_calc_total_course_duration())