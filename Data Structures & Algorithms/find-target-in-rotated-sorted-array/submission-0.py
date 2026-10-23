class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # find sorted half, 
        # if nums[mid] == target return mid 

        # if nums[l] <= nums[mid]

            # true: check if nums[l] <= target < nums[mid]
                #true: r = m - 1
                #false: l = m + 1

            # false: check if nums[mid] < target <= nums[r]
                #true: l = m + 1
                # false: r = m - 1


        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            elif nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else: 
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid -1 
        return - 1
                






        