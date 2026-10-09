/*
You are given two 2D integer arrays, items1 and items2, representing two sets of items. Each array items has the following properties:
items[i] = [valuei, weighti] where valuei represents the value and weighti represents the weight of the ith item.
The value of each item in items is unique.
Return a 2D integer array ret where ret[i] = [valuei, weighti], with weighti being the sum of weights of all items with value valuei.
Note: ret should be returned in ascending order by value.
*/
using System.Collections.Generic;
using System.Linq;


public class Solution {
    private Dictionary<int, int> dict;

    public IList<IList<int>> MergeSimilarItems(int[][] items1, int[][] items2) {
        dict = new Dictionary<int, int>();
        fill(items1);
        fill(items2);
        int[][] res = dict
            .OrderBy(pair => pair.Key)
            .Select(pair => new int[] { pair.Key, pair.Value })
            .ToArray();
        return res;
    }

    private void fill(int[][] items) {
        foreach (int[] item in items) {
            if (dict.ContainsKey(item[0])) {
                dict[item[0]] += item[1];
            } else {
                dict[item[0]] = item[1];
            }
        }
    }
}
