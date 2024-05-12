class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        
        size = len(code)
        result = [ 0 for _ in range(size) ]
        
        if k == 0:
            # Quick response for k == 0
            return result
        
        # Get the sign of k
        # 1 for positive k, which means right shift
        # -1 for negative k, which means left shift
        RIGHT_SHIFT, LEFT_SHIFT = 1, -1
        direction = int( math.copysign(1, k) )
        
        # Compute start and end point of sliding window
        start, end = direction, k
        cur_window_sum = sum( code[start: end+direction: direction] )
        
        
        # Decrypt the code by sliding window
        for i in range(size):

            result[i] = cur_window_sum
            
            if direction == RIGHT_SHIFT:
                # Sliding window right shifts
                cur_window_sum += (-code[start])
                start = (start+1)%size  

                end = (end+1)%size  
                cur_window_sum += (code[end])
            
            else:
                # Sliding window left shifts
                cur_window_sum += (-code[end])
                end = (end+1)%size  
                
                start = (start+1)%size  
                cur_window_sum += (code[start])
                
            
        return result
            