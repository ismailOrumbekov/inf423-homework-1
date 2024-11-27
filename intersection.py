class Solution(object):
    def intersection(self, nums1, nums2):
        seen = {}
        for i in nums1:
            seen[i] = 1
        res = set()
        for i in nums2:
            if i in seen:
                res.add(i)
        return list(res)

