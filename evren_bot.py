#!/usr/bin/env python

import datetime
import time
import random
import requests
import os


def build_message(phrase_sets):
    message = ''
    for phrase_set in phrase_sets:
        message += random.choice(phrase_set)
    return message

PHRASE_SETS = [
    ['', "dont forget to "],
    ['order'],
    ['', ' your'],
    [' lunch', ' lunches'],
    ['', ' people', ' everyone'],
]


def wait_random_time_between(minutes_min, minutes_max):
    seconds_min = minutes_min * 60
    seconds_max = minutes_max * 60
    seconds = random.randrange(seconds_min, seconds_max)
    print 'waiting', seconds, 'seconds'
    time.sleep(seconds)


def main():
    wait_random_time_between(1, 9)

    try:
        if datetime.datetime.today().day % 9 == 0:
            message = 'WFH today'
            os.system("""curl -X POST --data-urlencode 'payload={{"channel": "#sd", "username": "evren-bot", "text": "{message}", "icon_emoji": ":whale2:"}}' {hook_url}""".format(
                message=message,
                hook_url=os.environ['SLACK_HOOK_URL'],
            ))
            time.sleep(120)
    except:
        # stupid error handling to make sure nobody forgets to buy lunch
        pass

    message = build_message(PHRASE_SETS)
    print message

    os.system("""curl -X POST --data-urlencode 'payload={{"channel": "#sd", "username": "evren-bot", "text": "{message}", "icon_emoji": ":whale2:"}}' {hook_url}""".format(
        message=message,
        hook_url=os.environ['SLACK_HOOK_URL'],
    ))

if __name__ == '__main__':
    main()
