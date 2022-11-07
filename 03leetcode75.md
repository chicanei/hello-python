# [leetcode 75]([https:/](https://leetcode.com/study-plan/leetcode-75/?progress=xnkxa3c1)/)

###### tags: `程式設計` `leetcode` `study plan`

## level1

### [Day 1 Prefix Sum](https://leetcode.com/study-plan/leetcode-75/?progress=xnkxa3c1)

#### 1480 [1480. Running Sum of 1d Array](https://leetcode.com/problems/running-sum-of-1d-array/?envType=study-plan&id=level-1)
```(=python)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
    #第i個數字會 == 前i-1個數字的加總
        for i  in range(1,len(nums)) :
            nums[i]+= nums[i-1]
        return nums
```

#### 724 [724. Find Pivot Index]([https:/](https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1)/)
```(=python)
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''此法超時
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        
        return -1
        '''
'''第i個數字的所有右側數字加總 == 第i個數字的所有的左側數字加總 ，那麼就回傳i值 '''   
        total = sum(nums)
        leftSum = 0
        
        for i in range(len(nums)):
            rightSum = total - nums[i] - leftSum
            if leftSum == rightSum:
                return i
            leftSum += nums[i]
            
        return -1
```

### Day 2 String