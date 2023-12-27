# You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order). Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a height greater than or equal to hi.
# Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people_dict = {}
        for human in people:
            if human[0] in people_dict:
                people_dict[human[0]].append(human[1])
            else:
                people_dict[human[0]] = [human[1]]
        for key in people_dict.keys():
            people_dict[key].sort()
        res = [None]*len(people)
        keys = list(people_dict.keys())
        keys.sort()
        for height in keys:
            infos = people_dict[height]
            j = 0
            counter = 0
            ind = 0
            while j < len(res):
                if ind >= len(infos):
                    break
                if counter == infos[ind]:
                    if res[j] is None:
                        counter += 1
                        res[j] = [height, infos[ind]]
                        ind += 1
                        j += 1
                    else:
                        j += 1
                    continue
                if res[j] is None:
                    counter += 1
                    j += 1
                else:
                    j += 1 
        return res
  
