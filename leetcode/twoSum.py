# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.



from operator import index, le
from unicodedata import name


class Solution(object):
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        seen = {nums[0]: 0}
        for i,v in enumerate(nums,1):
            r = target - nums[i]
            if r in seen:
                return (i, seen[r])
            seen[nums[i]] = i 


    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
        
    #     seen = {}
    #     seen[nums[0]] = 0
    #     for i in range(1, len(nums)):
    #         r = target - nums[i]
    #         if r in seen:
    #             return ([i, seen[r]])
    #         seen[nums[i]] = i 
    
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
        
    #     seen = {}#g! best asnwer - fastest
    #     for i, value in enumerate(nums):
    #         remaining = target - value
           
    #         if remaining in seen:
    #             return (i, seen[remaining])
            
    #         seen[value] = i 

    # def twoSum3(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     for i in range(len(nums)):
    #         for j,m in enumerate(nums):
    #             if nums[i] + m == target and i != j :
    #                 return (i, j)

    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            c = 0
            for j in nums:
                if nums[i] + j == target and i != c :
                    return (i, c)
                c +=1

    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_i = 0
        for i in nums:
            index_ii = 0
            for ii in nums:
                if not index_i == index_ii:
                    if i+ii == target:
                        return [index_i, index_ii]
                index_ii+=1
            index_i +=1


            

def main():
    test = Solution()
    print(test.twoSum([3,2,4], 6))

if __name__=='__main__':
    main()