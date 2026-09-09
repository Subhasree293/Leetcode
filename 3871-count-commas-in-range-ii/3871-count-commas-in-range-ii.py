class Solution(object):
    def countCommas(self, n):
        total = 0
        power = 1000
        commas = 1
        
        while power <= n:
            next_power = power * 1000
            
            end = min(n, next_power - 1)
            total += (end - power + 1) * commas
            
            power = next_power
            commas += 1
        
        return total