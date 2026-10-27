class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0 
        l = 0
        window = {}
        max_frequency = 0

        for r in range(len(s)):
            window[s[r]] = window.get(s[r], 0) + 1
            max_frequency = max(window[s[r]], max_frequency)

            while (r - l + 1) - max_frequency > k:
                window[s[l]] -= 1
                l += 1

            longest = max(longest, (r - l) + 1)
        
        return longest


            




            



            
             






        