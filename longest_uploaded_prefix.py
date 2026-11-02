# You are given a stream of n videos, each represented by a distinct number from 1 to n that you need to "upload" to a server. You need to implement a data structure that calculates the length of the longest uploaded prefix at various points in the upload process.
# We consider i to be an uploaded prefix if all videos in the range 1 to i (inclusive) have been uploaded to the server. The longest uploaded prefix is the maximum value of i that satisfies this definition.
# Implement the LUPrefix class:
# LUPrefix(int n) Initializes the object for a stream of n videos.
# void upload(int video) Uploads video to the server.
# int longest() Returns the length of the longest uploaded prefix defined above.
class LUPrefix:
    def __init__(self, n: int):
        self.info = [0] * n
        self.ind = 0        

    def upload(self, video: int) -> None:
        video -= 1
        self.info[video] = 1
        if self.ind <= video:
            res = self.ind
            for j in range(self.ind, len(self.info)):
                if self.info[j] > 0:
                    res += 1
                else:
                    self.ind = res
                    break
            else:
                self.ind = len(self.info)

    def longest(self) -> int:
        return self.ind


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
