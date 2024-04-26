import re
from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()  
        words = paragraph.split() 
        cleaned_paragraph = re.sub(r'[^\w\s]', ' ', paragraph)
        words = cleaned_paragraph.split()
        word_counts = Counter(words)
        for word, count in word_counts.most_common():
            if word not in banned:
                return word