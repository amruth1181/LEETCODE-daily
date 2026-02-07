class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre=[1]*len(nums)
        for i in range(len(nums)):
            if i==0:
                pre[i]*1
            else:
                pre[i]=nums[i-1]*pre[i-1]
        suff=[1]*len(nums)
        numsr=nums[::-1]

        for j in range(len(nums)):
            if  j==0:
                suff[j]*1
            else:
                suff[j]=numsr[j-1]*suff[j-1]
        suff2=suff[::-1]
        answer=[1]*len(nums)
        for k in range(len(nums)):
            answer[k]=pre[k]*suff2[k]

        return answer