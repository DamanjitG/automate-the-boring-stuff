#! python3
import shelve, pyperclip, sys
mclipShelf = shelve.open('mclip')

if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mclipShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mclipShelf[sys.argv[2]]

elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mclipShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        mclipShelf.clear()
    elif sys.argv[1] in mclipShelf:
        pyperclip.copy(mclipShelf[sys.argv[1]])
    
mclipShelf.close()