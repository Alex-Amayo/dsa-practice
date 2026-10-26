class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort array 

        #loop through len(range(nums)) -2
            #skip duplicate fixed numbers
            #break if numbers are above O
            
            #while l < r
                #check fixed num + left + right > 0
                    # move r -= 1
                #check fixed num + left + right < 0
                    # move l  += 1 
                #check fixed num + left + right == 0
                    #add to result

                    #skip duplicate left and right values

        nums.sort()
        res = []


        for i in range(len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            l = i + 1
            r = len(nums) - 1

            while l < r:
                total =  nums[i] + nums[l] + nums[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1 
                else:
                    res.append([nums[i], nums[l], nums[r]])

                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1 

                    l += 1
                    r -= 1
        
        return res
