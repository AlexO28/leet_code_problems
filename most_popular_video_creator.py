# You are given two string arrays creators and ids, and an integer array views, all of length n. The ith video on a platform was created by creators[i], has an id of ids[i], and has views[i] views.
# The popularity of a creator is the sum of the number of views on all of the creator's videos. Find the creator with the highest popularity and the id of their most viewed video.
# If multiple creators have the highest popularity, find all of them.
# If multiple videos have the highest view count for a creator, find the lexicographically smallest id.
# Note: It is possible for different videos to have the same id, meaning that ids do not uniquely identify a video. For example, two videos with the same ID are considered as distinct videos with their own viewcount.
# Return a 2D array of strings answer where answer[i] = [creatorsi, idi] means that creatorsi has the highest popularity and idi is the id of their most popular video. The answer can be returned in any order.
class Solution:
    def mostPopularCreator(self, creators: list[str], ids: list[str], views: list[int]) -> list[list[str]]:
        create_data = {}
        create_data_2 = {}
        create_data_3 = {}
        video_data = {}
        max_val = -1
        for j in range(len(creators)):
            if creators[j] in create_data:
                create_data[creators[j]] += views[j]
                if views[j] > create_data_2[creators[j]]:
                    create_data_2[creators[j]] = views[j]
                    create_data_3[creators[j]] = ids[j]
                elif views[j] == create_data_2[creators[j]]:
                    create_data_3[creators[j]] = min(create_data_3[creators[j]], ids[j])
            else:
                create_data[creators[j]] = views[j]
                create_data_2[creators[j]] = views[j]
                create_data_3[creators[j]] = ids[j]
            max_val = max(max_val, create_data[creators[j]])
        creators = []
        for creator in create_data:
            if create_data[creator] == max_val:
                creators.append([creator, create_data_3[creator]])
        return creators
