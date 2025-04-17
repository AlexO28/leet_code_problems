# Implement a SnapshotArray that supports the following interface:
# SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
# void set(index, val) sets the element at the given index to be equal to val.
# int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
# int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
class SnapshotArray:

    def __init__(self, n):
        self.histories = [[[-1, 0]] for i in range(n)]
        self.snap_id = 0

    def set(self, index, val):
        self.histories[index].append([self.snap_id, val])

    def snap(self):
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        left = 0 
        right = len(self.histories[index]) - 1
        pos = -1
        while left <= right:
            mid = (left + right) // 2
            if self.histories[index][mid][0] <= snap_id:
                left = mid + 1
                pos = mid
            else:
                right = mid - 1
        return self.histories[index][pos][1]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
