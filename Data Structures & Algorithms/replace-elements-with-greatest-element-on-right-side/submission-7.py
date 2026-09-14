class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        k = []
        for i in range(len(arr) - 1):
            g = -1
            for j in range(i + 1, len(arr)):
                if arr[j] > g:
                    g = arr[j]
            k.append(g)
        k.append(-1)
        return k
