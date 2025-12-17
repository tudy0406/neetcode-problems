class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        
        for string in strs:
            encodedString += str(len(string))
            encodedString += '.'
            encodedString += string
        return encodedString

    def decode(self, s: str) -> List[str]:
        foundSep = False
        length = 0
        stringList = []
        string = ""
        currPosInString = -1
        for ch in s:
            if ch == '.':
                foundSep = True
                currPosInString = -1
                if length == 0:
                    length = 0
                    stringList.append(string)
                    string = ""
                    foundSep = False
                continue
            
            if not foundSep:
                length = length*10+(ord(ch)-ord('0'))
            else:
                string += ch
                currPosInString += 1
                if currPosInString == length-1:
                    length = 0
                    stringList.append(string)
                    string = ""
                    foundSep = False
        return stringList
                    




