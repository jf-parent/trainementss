#! /usr/bin/env python

from random import choice

import click

exercises = \
    ['Crunches'] * 2 + \
    ['Squat'] * 3 + \
    ['Lounge'] * 3 + \
    ['Vsit'] * 3 + \
    ['Padmasana'] * 3 + \
    ['Sirshasana'] * 3

quotes = [
    "Sweat is Fat Crying",
    "Better Sore Than Sorry",
    "I hated every minute of training, but I said, \'Don\'t quit. Suffer now and live the rest of your life as a champion.\' -Muhammad Ali",
    "The purpose of training is to tighten up the slack, toughen the body, and polish the spirit. -Morihei Ueshiba",
    "Strive for progress, not perfection.",
    "You want me to do something... tell me I can't do it. -Maya Angelou",
    "Energy and persistence conquer all things. -Benjamin Franklin",
]

@click.group()
def cli():
    pass

@click.command()
@click.argument('number', default=1, type=int)
def random(number):
    print '-'*80
    print '[*]', choice(quotes)
    print '-'*80
    for _ in xrange(number):
        print '[*]', choice(exercises)

cli.add_command(random)
