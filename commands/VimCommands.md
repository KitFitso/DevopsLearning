## [To the notes page](../03_Linux.md)

### it has better notes and some examples

# commands in the 3 modes

## command mode (default)

- i - insert lets you edit the files
- : - enters extended command line mode
- o - inserts like i but onto the next line
- gg - go to the beginning of the page
- G - go to the end of the page
- w - move cursor forward 1 word
- b - move cursor backward 1 word
- nw - move cursor forward n words (5w)
- nb - move cursor backward n words (3b)
- u - undo the last change
- U - undo the whole line
- crtl-R - redo the changes
- yy - copy a line
- nyy - copies n lines
- dd - cut the line (works as delete if you don't paste)
- ndd - cut n lines
- p - paste line below cursor
- P - paste line above cursor
- dw - delete like backspace
- x - delete like del
- / - search for a word

## insert mode

- esc - takes back to command mode
- {any} - lets you actually type stuff

## extended command mode

- :w - writes(saves) the file
- :q - quits out of vim
- :q! - force quit - let's you quit without saving, you can force quit with !
- :se nu - set lines numbers on vim editor
- :wq save and quit at the same time
- :%s/{search}/{replace}[/g]
