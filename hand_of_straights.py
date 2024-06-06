# Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size groupSize, and consists of groupSize consecutive cards.
# Given an integer array hand where hand[i] is the value written on the ith card and an integer groupSize, return true if she can rearrange the cards, or false otherwise.
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1:
            return True
        max_groups, remainder = divmod(len(hand), groupSize)
        if remainder != 0:
            return False
        hand_dict = {}
        for card in hand:
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
            while cur_group < groupSize:
                if cur_ind == len(hand_keys):
                    return False
                if hand_dict[hand_keys[cur_ind]] == 1:
                    had_deletes = True
                    del hand_dict[hand_keys[cur_ind]]
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
                hand_keys = list(hand_dict.keys())
                hand_keys.sort()
        return True
