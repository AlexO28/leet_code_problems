# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.
# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:
# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        max_number_of_trees = 0
        for j in range(len(fruits)):
            if len(fruits)-j <= max_number_of_trees:
                break
            number_of_trees = 0
            other_fruit = None
            for i in range(j, len(fruits)):
                if fruits[i] == fruits[j]:
                    number_of_trees += 1
                else:
                    if other_fruit is None:
                        other_fruit = fruits[i]
                        number_of_trees += 1
                    else:
                        if fruits[i] == other_fruit:
                            number_of_trees += 1
                        else:
                            break
            max_number_of_trees = max(max_number_of_trees, number_of_trees)
        return max_number_of_trees
