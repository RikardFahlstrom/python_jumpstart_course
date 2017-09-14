import collections
import glob
import os

SearchResult = collections.namedtuple('SearchResult', 'file, line, text')

def main():
    print_header()

    folder = get_folder_from_user()
    if not folder:
        print("We can't search that location.")  # if user don't enters something
        return

    text = get_search_text_from_user()
    if not text:
        print("We can't search for nothing!")
        return

    matches = search_folders(folder, text)

    match_count = 0
    for m in matches:
        match_count += 1
        #  print(m)
        print('------ MATCH ------')
        print('file: ' + m.file)
        print('line: {:,}'.format(m.line))
        print('match: ' + m.text.strip())  # .strip() to remove new line from each line of text
        print()

    print("Found {:,} matches.".format(match_count))


def print_header():
    print("----------------------------")
    print("       FILE SEARCH APP")
    print("----------------------------")


def get_folder_from_user():
    folder = input('What folder do you want to search? ')
    if not folder or not folder.strip():  # if user input is empty or only spaces, which .strip() detects, return None.
        return None

    if not os.path.isdir(folder):  # if the folder don't exists.
        return None

    return os.path.abspath(folder)  # return absolute path to make future interactions easier.


def get_search_text_from_user():
    text = input('What are you searching for [single phrases only]? ')
    return text.lower()  # To become non-case sensitive


def search_folders(folder, text):
    #  print('Would search {} for {}.'.format(folder, text))

    all_matches = []
    # items = os.listdir(folder)  # Will return all items in the folder, return just filename, not full path name
    items = glob.glob(os.path.join(folder, '*'))  # for mac only, crash with above line due to hidden .DS_Store binary files

    for item in items:
        full_item = os.path.join(folder, item)  # folder is already abs path, join-function will join folders abs path with filename for item in a 'smart' way.
        if os.path.isdir(full_item):  # checks if item is a folder, if it is...
            # continue  # ...we use continue which will just continue to the next item in the loop.
            matches = search_folders(full_item, text)  # Use recursion since we use the same function within the function.
            #  all_matches.extend(matches)
            #  for m in matches:
                #  yield m
            yield from search_folders(full_item, text)  # Same as for-loop on above line, 'yield from' is Python 3 specific 
        else:
            #  if it's not a directory, it has to be a file, search the file for the text
            matches = search_file(full_item, text)
            #  all_matches.extend(matches)  # if this was one item = append, but if it's a collection, we want to add each item from the collection individually -> then extend
            #  for m in matches:
                #  yield m
            yield from search_file(full_item, text)  # Same as for-loop on above line, 'yield from' is Python 3 specific

    #  return all_matches

def search_file(filename, search_text):
    #  matches = []
    with open(filename, 'r', encoding='utf-8') as fin:  # open in a context manager, open filename, which is a full file path from above join-func., 'r' -> read only-mode, 'utf-8' -> treat as text.

        line_num = 0
        for line in fin:
            line_num += 1
            if line.lower().find(search_text) >= 0:  # Could look for a sub-text in two ways. line.index() or line.find(), if not found index will show a Exception, find will return -1.
                m = SearchResult(line=line_num, file=filename, text=line)
                #  matches.append(m)
                yield m
    #  return matches

if __name__ == '__main__':
    main()
