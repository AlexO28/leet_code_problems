/* Design a special dictionary that searches the words in it by a prefix and a suffix.
Implement the WordFilter class:
WordFilter(string[] words) Initializes the object with the words in the dictionary.
f(string pref, string suff) Returns the index of the word in the dictionary, which has the prefix pref and the suffix suff. If there is more than one valid index, return the largest of them. If there is no such word in the dictionary, return -1. */
class WordFilter {

    private String[] words;

    public WordFilter(String[] words) {
        this.words = words;
    }
    
    public int f(String pref, String suff) {
        for (int i = (this.words.length)-1; i>=0; --i) {
            boolean not_found = true;
            if (this.words[i].length() >= pref.length()) {
                for (int j = 0; j < pref.length(); ++j) {
                    if (this.words[i].charAt(j) != pref.charAt(j)) {
                        not_found = false;
                        break;
                    }
                }
            } else {
                not_found = false;
            }
            if ((not_found) && (this.words[i].length() >= suff.length())) {
                for (int j = 0; j < suff.length(); ++j) {
                    if (this.words[i].charAt(this.words[i].length()-j-1) != suff.charAt(suff.length()-j-1)) {
                        not_found = false;
                        break;
                    }
                }
            } else {
                not_found = false;
            }
            if (not_found) {
                return i;
            }
        }
        return -1;
    }
}
