class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        for i in range (len(nums)):
            if i==0 or nums[i-1]==0:
                count=0
                while i<len(nums) and nums[i]==1 :
                    count+=1
                    i+=1 
                c= max(c,count)
                
        return c


        