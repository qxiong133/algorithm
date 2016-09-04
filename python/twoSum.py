


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index,j in enumerate(nums):
            z = target - j
            try:
                k = nums[index+1:].index(z)
                k += index+1
            except:
                continue
            if k:
                return [index, k]
        return [None, None]

def main():
    a = Solution()
    print a.twoSum([2,7,11,17], 9)
    print a.twoSum([0,4,3,0], 0)
    print a.twoSum([-1,-2,-3,-4,-5], -8)



if __name__ == "__main__":
    main()
