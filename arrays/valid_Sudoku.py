class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squareTable = {}
        rowTable = {}
        columnTable = {}
        squareNumber = -1
        for i in range(len(board)):
            for j in range(len(board[i])):

                val = board[i][j]
                if val == '.':
                    continue

                squareNumber = 3*(i//3)+(j//3)
                if squareNumber not in squareTable:
                    squareTable[squareNumber] = set()
                if i not in rowTable:
                    rowTable[i] = set()
                if j not in columnTable:
                    columnTable[j] = set()

                if val in squareTable[squareNumber] or val in rowTable[i] or val in columnTable[j]:
                    return False
            
                squareTable[squareNumber].add(val)
                rowTable[i].add(val)
                columnTable[j].add(val)
        
        return True
