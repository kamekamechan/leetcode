class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        arr = nums1.append(nums2)
        arr = sorted(arr)
        pivot = len(arr)%2
        if(len(arr)%2 == 0):
            median = (arr[len(arr)//2-1],arr[len(arr)//2])/2
        else:
            median = arr[len(arr)//2]
        return median

test = Solution()
test.findMedianSortedArrays([1,2],[3])