class Solution(object):
    def merge(self, nums1, m, nums2, n):
        res = []
        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                res.append(nums1[i])
                i += 1
            else:
                res.append(nums2[j])
                j += 1

        while i < m:
            res.append(nums1[i])
            i += 1

        while j < n:
            res.append(nums2[j])
            j += 1

        for k in range(m + n):
            nums1[k] = res[k]