"""
This is the journal file, it handles all operations with the journal.
It contains three functions; load, save and add journal entry.
"""

import os


def load(name):
    """
    This methods creates and loads a new journal.

    :param name: Name of the journal to load.
    :return: Content from journal.
    """
    data = []
    filename = get_full_pathname(name)

    if os.path.exists(filename):
        with open(filename) as fin:
            for entry in fin.readlines():
                data.append(entry.rstrip())

    return data


def save(name, journal_data):
    filename = get_full_pathname(name)
    print('... saving to: {}'.format(filename))

    with open(filename, 'w') as fout:
        for entry in journal_data:
            fout.write(entry + '\n')


def add_entry(text, journal_data):
    journal_data.append(text)


def get_full_pathname(name):
    filename = os.path.abspath(os.path.join('.', 'journals', name + '.txt'))
    return filename



