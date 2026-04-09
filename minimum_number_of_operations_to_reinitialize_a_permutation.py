# You are given an even integer n​​​​​​. You initially have a permutation perm of size n​​ where perm[i] == i​ (0-indexed)​​​​.
# In one operation, you will create a new array arr, and for each i:
# If i % 2 == 0, then arr[i] = perm[i / 2].
# If i % 2 == 1, then arr[i] = perm[n / 2 + (i - 1) / 2].
# You will then assign arr​​​​ to perm.
# Return the minimum non-zero number of operations you need to perform on perm to return the permutation to its initial value.
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        perm_start = [i for i in range(n)]
        perm = perm_start.copy()
        n_half = n // 2
        num_operations = 0
        while True:
            num_operations += 1
            arr = []
            for i in range(n):
                main_part, remainder = divmod(i, 2)
                if remainder == 0:
                    arr.append(perm[main_part])
                else:
                    arr.append(perm[n_half + main_part])
            if arr == perm_start:
                break
            perm = arr
        return num_operations
