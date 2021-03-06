# Bright.MD Take Home Tasks

This is my code challenge submission for a Developer position at Bright.MD

## Task 1: Globophone

### How to use it

1. Simply visit https://jarrighi.github.io/take-home-tasks/ to interact with the page.

    or 

1. The whole application is contained in one page, so this should work by downloading the globophone.html file and loading it in a browser.

### Feature specs

These are somewhat reorganized from the prompt to represent how I plan to implement the features

Page Structure

+ Text field exists
+ Phone number field exists
+ Save button exists
+ Confirmation section hidden initially
+ Go Back button exists within hidden confirmation section


Phone number Validation

+ Validate number field not blank
+ Validate number field 10 or 11 digits
+ Validate number field doesn't start with 0
+ Validate number field spaces, dots, dashes okay
+ Validate number field alpha and special characters not okay


Save a number

+ Clicking save adds name and number to localStorage
+ Clicking save sends user to success message
+ Can't click save without a name
+ Can't click save on invalid number


Delete a number

+ Visible only if number data in localStorage
+ Clicking delete button removes data from localStorage


Confirmation section

+ Visible immediately after clicking save
+ Go back button reloads the page

Miscellaneous
+ Data persists over browser sessions
* return/enter key doesn't trigger delete
* attractive style rather than plain html 


### Additional notes

Globophone does not allow for '+', '(', and ')' characters to be used in a phone number as specified in the prompt. It may be desirable to allow these characters since some users may type phone numbers as (555) 555-5555 or +1 555 555 5555.


## Task 2: Book Search

### How to use it

Both the booksearch tool and the tests can be run with Python 2 or 3. I've tested them with Python 2.7.12 and Python 3.5.2. All searches are case-inensitive.

#### Running the search

Run either of the following to get usage guide:

```
$ python booksearch.py 
```

```
$ python booksearch.py -h
```

To search for books that contain a specific word in the default dataset (bookdata.json):

```
$ python booksearch.py [word]
```

To search for books that contain any of a set of words using the default dataset (bookdata.json):

```
$ python booksearch.py [word1] [word2] ...
```

To search for books using a specific dataset:

```
$ python booksearch.py -f [path/to/dataset] [word1] [word2] ...
```

or 

```
$ python booksearch.py --file [path/to/dataset] [word1] [word2] ... 
```

#### Running the tests

To run the tests from the booksearch directory: 

```
python tests.py
```

### Feature specs

These are somewhat reorganized from the prompt

Basic usage 

* Usage: yourbookprogram word1 word2 ...
* Output: id and title for each book that matches any word


Search

* Allow user to match words case-insensitively
* Punctuation surrounding words should be ignored


Performance 

* Searches run in constant time (O(1)) with respect to a single word
* Multiple word searches linear (O(n)) with respect to number of words
    



### Additional notes

NA
