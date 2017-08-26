"""
This is the program file. It handles all operations with the user.
"""

import journal


def main():
    print_header()
    run_event_loop()


def print_header():
    print('-------------------------')
    print('      JOURNAL APP')
    print('-------------------------')
    print()


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = 'B'
    journal_name = 'default'
    journal_data = journal.load(journal_name)

    while cmd != 'x' and cmd:  # Lägger till 'and cmd' för att kolla så cmd innehåller ett värde.
        cmd = input('[L]ist or [A]dd a journal entry? E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, do not understand '{}'".format(cmd))

    print('Done, goodbye!')
    journal.save(journal_name, journal_data)


def list_entries(data):
    print('Your journal entries are: ')
    entries = reversed(data)  # Detta för att få senaste inlägget överst.
    for idx, entry in enumerate(entries):
        print('* [{}]: {}'.format(idx + 1, entry))


def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)


if __name__ == '__main__':  # Kollar om programmet ska köras eller om koden används som referens i annat program.
    main()
