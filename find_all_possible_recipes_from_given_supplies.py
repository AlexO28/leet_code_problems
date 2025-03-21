# You have information about n different recipes. You are given a string array recipes and a 2D string array ingredients. The ith recipe has the name recipes[i], and you can create it if you have all the needed ingredients from ingredients[i]. A recipe can also be an ingredient for other recipes, i.e., ingredients[i] may contain a string that is in recipes.
# You are also given a string array supplies containing all the ingredients that you initially have, and you have an infinite supply of all of them.
# Return a list of all the recipes that you can create. You may return the answer in any order.
# Note that two recipes may contain each other in their ingredients.
from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        res = []
        found_indices = []
        while True:
            not_found_anything = True
            for j in range(len(recipes)):
                if j not in found_indices:
                    all_good = True
                    for ingredient in ingredients[j]:
                        if ingredient not in supplies:
                            all_good = False
                            break
                    if all_good:
                        res.append(recipes[j])
                        supplies.append(recipes[j])
                        found_indices.append(j)
                        not_found_anything = False 
            if not_found_anything:
                return res
