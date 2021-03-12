# Naming Conventions

- Module names: Short, lowercase names, without underscores. (eg. myfile.py)
- Class names: camelCase Conventions. (eg. className)
- Definitions and Variables: lowercase with words seperated with underscore or camelCase. (eg. my_variable or myVariable)
- internal/private defs and variables: camelCase with underscore prefix. (eg. _myVariable)
- Don't use suffix underscore for public variables and defs. these formats are reserved names.
- imports: import one at a line
eg.:
import os
import sys
from somelibrary import module1, module2
(not like this: import os, sys)


- order of import:
  - standard lib imports
  - required package imports
  - project specific imports

# Indentations

- Strictly no tabs. use 2 space Indentations
- Max 70 characters in one line, then break line using \

# White spaces

- multiple statements/logic in one line is not a good practice.
improper way:
if foo == 'bar': doSomething()

good practice:
if foo == 'bar':
  doSomething()

- Not to use white space between parenthesis - correctWay(args) or dict['key']
- No white spaces inside the parenthesis.
- No white spaces just before comma.
- use these operators surrounding single space: (=, ==, <, >, !=, <>, <=, >=, in, not in, is, isnot, and, or, not, +, -, *, /, %)
- Don't use space around = sign in arguments or as a default value in params.


# Comments

- inline comments: use one space after # this is example inline-comment
- multi-line comments use # and one space
# after every
# line of
# multi-line comment

# Documentation String

Use three quotes """ for docStrings
