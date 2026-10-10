/*Design a food rating system that can do the following:
Modify the rating of a food item listed in the system.
Return the highest-rated food item for a type of cuisine in the system.
Implement the FoodRatings class:
FoodRatings(String[] foods, String[] cuisines, int[] ratings) Initializes the system. The food items are described by foods, cuisines and ratings, all of which have a length of n.
foods[i] is the name of the ith food,
cuisines[i] is the type of cuisine of the ith food, and
ratings[i] is the initial rating of the ith food.
void changeRating(String food, int newRating) Changes the rating of the food item with the name food.
String highestRated(String cuisine) Returns the name of the food item that has the highest rating for the given type of cuisine. If there is a tie, return the item with the lexicographically smaller name.
Note that a string x is lexicographically smaller than string y if x comes before y in dictionary order, that is, either x is a prefix of y, or if i is the first position such that x[i] != y[i], then x[i] comes before y[i] in alphabetic order.*/
using System.Collections.Generic;


public class FoodRatings {
    private Dictionary<string, SortedSet<Tuple<int, string>>> d = new();
    private Dictionary<string, Tuple<int, string>> g = new();
    private readonly Comparer<Tuple<int, string>> cmp = Comparer<Tuple<int, string>>.Create((a, b) => {
        if (a.Item1 != b.Item1) {
            return b.Item1.CompareTo(a.Item1);
        } else {
            return string.Compare(a.Item2, b.Item2, StringComparison.Ordinal);
        }
    });
    public FoodRatings(string[] foods, string[] cuisines, int[] ratings) {
        for (int i = 0; i < foods.Length; ++i) {
            if (!d.TryGetValue(cuisines[i], out var set)) {
                set = new SortedSet<Tuple<int, string>>(cmp);
                d[cuisines[i]] = set;
            }
            set.Add(Tuple.Create(ratings[i], foods[i]));
            g[foods[i]] = Tuple.Create(ratings[i], cuisines[i]);
        }
    }
    
    public void ChangeRating(string food, int newRating) {
        Tuple<int, string> old = g[food];
        g[food] = Tuple.Create(newRating, old.Item2);
        d[old.Item2].Remove(Tuple.Create(old.Item1, food));
        d[old.Item2].Add(Tuple.Create(newRating, food));        
    }
    
    public string HighestRated(string cuisine) {
        return d[cuisine].Min.Item2;
    }
}

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.ChangeRating(food,newRating);
 * string param_2 = obj.HighestRated(cuisine);
 */
