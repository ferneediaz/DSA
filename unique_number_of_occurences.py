class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique_list = []
        arr_freq = {}
        for i in arr:
            arr_freq[i] = arr_freq.get(i, 0) + 1
        for k, v in arr_freq.items():
            unique_list.append(v)
        
        if len(list(set(unique_list))) == len(unique_list):
            return True
        else:
            return False