import argparse
import sys
import json
import string

DEFAULT_FILE = 'bookdata.json'

class BookSearchParser(argparse.ArgumentParser):
  def error(self, message):
    sys.stderr.write('error: %s\n' % message)
    self.print_help()
    sys.exit(2)

def create_parser():
  parser = BookSearchParser()
  parser.add_argument('-f', '--file', nargs=1, help="JSON File to be searched.")
  parser.add_argument('words', nargs='+')
  return parser

def create_index(bookfile):
  index = {}

  with open(bookfile, 'r') as f:
    books = json.load(f)

  for bookid in books.keys(): 
    tbl = {ord(c): None for c in string.punctuation}
    words = books[bookid]['title'].translate(tbl).split() 
    words += books[bookid]['description'].translate(tbl).split()
    sub_index = {word.lower(): [(bookid, books[bookid]['title'])] for word in words}

    for word in sub_index:
      existing_books = index.get(word)
      index[word] = sub_index[word] + existing_books if existing_books else sub_index[word]

  return index

def search(word, index):
  pass

def print_output(bookfile):
  print('Using "{}" as book data source.'.format(bookfile))

def set_data_file(args):
  bookfile = DEFAULT_FILE
  if args.file:
    bookfile = args.file[0]
  return bookfile

def main():
  # Create parser
  parser = create_parser()

  # Parse Args
  args = parser.parse_args()

  bookfile = set_data_file(args)

  # Create Index
  index = create_index(bookfile)

  # Run Searches

  # Print Results
  print_output(bookfile)

if __name__ == '__main__':
  main()
