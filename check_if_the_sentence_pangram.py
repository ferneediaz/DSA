class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        isPangram = {
        chr(letter): 0 
        for letter in range(ord('a'), ord('z') + 1)
        }

        for char in sentence:
            if char in isPangram:
                isPangram[char] += 1
        for count in isPangram.values():
            if count == 0:
                return False
        return True