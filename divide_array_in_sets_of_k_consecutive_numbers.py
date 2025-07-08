# Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.
# Return true if it is possible. Otherwise, return false.
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if k == 1:
            return True
        max_groups, remainder = divmod(len(nums), k)
        if remainder != 0:
            return False
        hand_dict = {}
        for card in nums:
            if card in hand_dict:
                hand_dict[card] += 1
            else:
                hand_dict[card] = 1
        hand_keys = list(hand_dict.keys())
        hand_keys.sort()
        num_groups = 0
        while num_groups < max_groups:
            cur_ind = 0
            cur_group = 0
            had_deletes = False
            prev_val = None
            the_group = []
            bad_indices = []
            while cur_group < k:
                if cur_ind == len(hand_keys):
                    return False
                if hand_dict[hand_keys[cur_ind]] == 1:
                    had_deletes = True
                    del hand_dict[hand_keys[cur_ind]]
                    bad_indices.append(cur_ind)
                else:
                    hand_dict[hand_keys[cur_ind]] -= 1
                if prev_val is not None:
                    if hand_keys[cur_ind] - prev_val != 1:
                        return False
                prev_val = hand_keys[cur_ind]
                cur_ind += 1
                cur_group += 1
                the_group.append(prev_val)
            num_groups += 1
            if had_deletes:
                for index in bad_indices[::-1]:
                    del hand_keys[index]
        return True
