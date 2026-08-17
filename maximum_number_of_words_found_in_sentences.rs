/*
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
You are given an array of strings sentences, where each sentences[i] represents a single sentence.
Return the maximum number of words that appear in a single sentence.
*/
use std::cmp::max;


impl Solution {
    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        let mut maximum_number_of_words: i32 = 0;
        for sentence in &sentences {
            maximum_number_of_words = max(maximum_number_of_words, sentence.chars().filter(|c| c.is_whitespace()).count() as i32);
        }
        maximum_number_of_words + 1
    }
}
