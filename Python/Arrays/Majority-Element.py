class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        contador = 0
        ans = 0
        for i in nums:
            if contador == 0:
                ans = i
            if i==ans:
                contador += 1
            else:
                contador -= 1
        return ans
