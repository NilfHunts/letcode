class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        col_new = {}
        color_count = defaultdict(int)
        result = []

        for i, v in queries:
            if i in col_new:
                old_col = col_new[i]
                color_count[old_col] -= 1
                if color_count[old_col] == 0:
                    del color_count[old_col]

            col_new[i] = v
            color_count[v] += 1

            result.append(len(color_count))

        return result



        
        
             
        

        
            
        
