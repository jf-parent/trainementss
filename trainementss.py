#! /usr/bin/env python
# -*- coding: utf-8 -*-

from random import sample, choice

import click

wim_hof_exercises = [
    'Butterfly asana (Badhakonasana)',
    'Forward bending (1 legs & 2 legs)',
    'Back bending (Ūrdhvamukhaśvānāsana)',
    'Ardha Matsyendrāsana',
    'Lateral stretch',
    'Headstand (Shirshasana)',
    'Shoulder Stand (Salamba Sarvāṅgāsana I)',
    'Warrior II (Vīrabhadrāsana II)',
    'Crane (Bakāsana)',
    'Raven (bakasana with leg extension)',
    'Side plank (Vasiṣṭhāsana)',
    'Split (Hanumanāsana)',
    'Shelf (Mayūrāsana)',
    'Astavakrasana (Eight angled Pose)',
    'Hand stand',
    'Horse Stance (馬步) (10 minutes with breathing)',
]

kettlebell = [
    'Man maker',
    'Upper Body Blast',
    'Slingshot',
    'Core',
    'Leg burner',
    'Swings'
]

mobilities = [
    "Neck",
    "Shoulder",
    "Elbow, Wrist, Hand & Finger",
    "Spine & Lower Back",
    "Hip Mobility",
    "Toe, Foot, Ankle & Knee",
    "Spinal Rocking"
]

exercises = [
    "Back Extension",
    "Ball Triceps Extension",
    "Hamstring Curl",
    "3min walking on the toe",
    "3min walking on the heel",
    "3min sitting on the heel",
    "Redressement assis",
    "Front kick",
    "Roundhouse kick",
    "Side kick",
    "Spin kick",
    "Hook kick",
    "Armada kick",
    "Axe kick",
    "Back kick",
    "Shadow boxing",
    "Forme",
    "Plank",
    "Squat",
    "Lounge",
    "L-sit",
    "Pistol squat",
]

quotes = [
    "Sweat is Fat Crying",
    "Better Sore Than Sorry",
    "I hated every minute of training, but I said, \'Don\'t quit. Suffer now and live the rest of your life as a champion.\' -Muhammad Ali",
    "The purpose of training is to tighten up the slack, toughen the body, and polish the spirit. -Morihei Ueshiba",
    "Strive for progress, not perfection.",
    "You want me to do something... tell me I can't do it. -Maya Angelou",
    "Energy and persistence conquer all things. -Benjamin Franklin",
    "Use only that which works, and take it from any place you can find it. -Bruce Lee",
    "Things do NOT happen. Things are made to happen -John F. Kennedy",
]

@click.group()
def cli():
    pass

@click.command()
@click.argument('number', default=1, type=int)
def random(number):
    #QUOTE
    print '-'*80
    print '[*]', choice(quotes)
    print '-'*80
    #WIM-HOF BREATHING
    print '[*] Breath Motherfucker!'
    print '-'*80
    #BODYWEIGHT TRAINING
    print '[*] Pompe'
    samples = sample(exercises, number)
    for s in samples:
        print '[*]', s

    #WIM-HOF EXERCISES
    print '-'*80
    print '\t**WIM-HOF**'
    samples = sample(wim_hof_exercises, number)
    for s in samples:
        print '[*]', s

    #MOBILITY
    print '-'*80
    print '[*] Mobility =>', choice(mobilities)
    print '-'*80

    #KETTLEBELL
    print '[*] Kettlebell =>', choice(kettlebell)
    print '-'*80

cli.add_command(random)
