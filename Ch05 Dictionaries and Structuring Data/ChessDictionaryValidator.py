def isValidChessBoard(chessBoard):
    validSpaces = []
    validPieces = ['wpawn','bpawn','wknight','bknight','wbishop','bbishop','wrook','brook','wqueen','bqueen','wking','bking']
    wpawns = 0
    bpawns = 0
    wknights = 0
    bknights = 0
    wbishops = 0
    bbishops = 0
    wrooks = 0
    brooks = 0
    wqueens = 0
    bqueens = 0
    wkings = 0
    bkings = 0
    
    if ("bking" not in chessBoard.values()) or ("wking" not in chessBoard.values()):
        return False
    for i in range(1,9):
        for letter in "abcdefgh":
            validSpaces.append(str(i)+letter)
    for space in chessBoard.keys():
        if space not in validSpaces:
            return False
    for piece in chessBoard.values():
        if piece not in validPieces:
            return False
        elif piece == "wpawn":
            wpawns += 1
        elif piece == "bpawn":
            bpawns += 1
        elif piece == "wknight":
            wknights += 1
        elif piece == "bknight":
            bknights += 1
        elif piece == "wbishop":
            wbishops += 1
        elif piece == "bbishop":
            bbishops += 1
        elif piece == "wrook":
            wrooks += 1
        elif piece == "brook":
            brooks += 1
        elif piece == "wqueen":
            wqueens += 1
        elif piece == "bqueen":
            bqueens += 1
        elif piece == "wking":
            wkings += 1
        elif piece == "bking":
            bkings += 1
    if (
           wpawns > 8 or bpawns > 8
        or wknights > 2 or bknights > 8
        or wbishops > 2 or bbishops > 2
        or wrooks > 2 or brooks > 2
        or wqueens > 1 or bqueens > 1
        or wkings > 1 or bkings > 1
    ): return False

    else: return True

testValidBoard = {'1h':'bking', '2a':'wking', '3c': 'wqueen'}
testInvalidBoard = {'1h':'bking', '2a':'wking', '3c':'wqueen', '4c':'wqueen'}

print(str(isValidChessBoard(testValidBoard)))
print(str(isValidChessBoard(testInvalidBoard)))


        

    