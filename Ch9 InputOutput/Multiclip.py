#! python3
import shelve, pyperclip, sys

mclipShelf = shelve.open("mclip")
if len(sys.argv) == 3 and sys.argv[1] == 'save':
    mclipShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mclipShelf.keys())))
    elif sys.argv[1] in mclipShelf:
        pyperclip.copy(mclipShelf[sys.argv[1]])

mclipShelf.close()