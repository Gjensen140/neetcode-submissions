class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre_product = [1] * n
        post_product = [1] * n

        for i in range(1, n):
            pre_product[i] = nums[i-1] * pre_product[i - 1]
            ind = -i - 1
            post_product[ind] = post_product[ind + 1] * nums[ind + 1] 


        output = [0] * n

        for i in range(n):
            output[i] = pre_product[i] * post_product[i]

        return output