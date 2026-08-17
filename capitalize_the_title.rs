/*
You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. Capitalize the string by changing the capitalization of each word such that:
If the length of the word is 1 or 2 letters, change all letters to lowercase.
Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
Return the capitalized title.
*/
impl Solution {
    pub fn capitalize_title(title: String) -> String {
        let mut res: String = String::new();;
        for word in title.split_whitespace() {
            let mut changed_word = String::from(word.to_lowercase());
            if (changed_word.len() > 2) {
                unsafe {
                    changed_word.as_mut_vec()[0..1].make_ascii_uppercase();
                }
            }
            if (res == "") {
                res = changed_word;
            } else {
                res.push_str(" ");
                res.push_str(&changed_word);
            }
        }
        res
    }
}
