class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # O(log(n+m)),O(1)
        # https://youtu.be/q6IEA26hvXc?si=wDnrS66qaEetgpzi
        A, B = nums1, nums2

        total = len(A) + len(B)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) -1
        # binary search on smaller array
        while True:
            # mid of small array
            i = (l+r)//2

            # elems of B = half - i - 1 - 1
            j = half - i -2

            # define border values
            Aleft = A[i] if i >=0 else float("-infinity")
            Aright = A[i+1] if (i + 1) < len(A) else float("infinity")

            Bleft = B[j] if j >=0 else float("-infinity")
            Bright = B[j+1] if (j + 1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total%2:
                    return min(Aright,Bright)
                # median of largest elem in left part and smallest in right part
                return (max(Aleft,Bleft) + min(Aright,Bright))/2
            elif Aleft > Bright:
                # Move the cut in A left 
                r = i - 1
            else:
                # Move the cut in A right
                l = i + 1