class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        count = 0
        j = {'a', 'e', 'i', 'o','u'}
        valid = [0]*(len(words)+1)
        for  i,word in enumerate(words,start = 1):
            if word[0] in j and word[-1] in j:
                count +=1
            valid[i] = count
        return [valid[q+1] - valid[p] for p,q in queries]
