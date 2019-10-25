#!/usr/bin/env python3

# A script to create an iCalendar file (linux-ag.ics) for the meetings of the
# Linux-AG at the University of Tübingen.

from ics import Calendar, Event
import arrow

# TODO: Update the following values (or fetch them from the website):
room = "A302"
time_start = "18:30:00"
dates = [ # Can be copied from the website
    "25.10.2019",
    "08.11.2019",
    "22.11.2019",
    "06.12.2019",
    "20.12.2019",
    "17.01.2020",
    "31.01.2020",
]

# The following values are unlikely to change:
name = "Linux-AG"
description = "Website: https://www.linux-ag.uni-tuebingen.de"
location = room + ", Sand, 72076 Tübingen, Germany"
time_end   = "21:00:00"

def get_date(date, time):
    # We use a strange format (can be copied directly from the website):
    date_format = "DD.MM.YYYY HH:mm:ss"
    date = arrow.get(date + " " + time, date_format)
    date = date.replace(tzinfo='Europe/Berlin')
    return date

# Create the calendar with all events and save the result (iCalendar):
c = Calendar()

for date in dates:
    e = Event()
    e.name = name
    e.description = description
    e.location = location
    e.begin = get_date(date, time_start)
    e.end   = get_date(date, time_end)
    # To make the output deterministic:
    e.created = arrow.get("1970-01-01 00:00:00+00:00")
    e.uid = date + "@www.linux-ag.uni-tuebingen.de"
    c.events.add(e)

with open("linux-ag.ics", "w") as f:
    f.writelines(c)
