/*
A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:
<col> denotes the column number c of the cell. It is represented by alphabetical letters.
For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
<row> is the row number r of the cell. The rth row is represented by the integer r.
You are given a string s in the format "<col1><row1>:<col2><row2>", where <col1> represents the column c1, <row1> represents the row r1, <col2> represents the column c2, and <row2> represents the row r2, such that r1 <= r2 and c1 <= c2.
Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2. The cells should be represented as strings in the format mentioned above and be sorted in non-decreasing order first by columns and then by rows.
*/
impl Solution {
    pub fn cells_in_range(s: String) -> Vec<String> {
        let mut temp = s.chars();
        let col1 = temp.nth(0).unwrap();
        let row1 = temp.nth(0).unwrap().to_digit(10).unwrap_or(0);
        let col2 = temp.nth(1).unwrap();
        let row2 = temp.nth(0).unwrap().to_digit(10).unwrap_or(0);
        if col1 > col2 {
            return Vec::new();
        }
        if row1 > row2 {
            return Vec::new();
        }
        let mut res: Vec<String> = Vec::new();
        for col_ind in (col1 as u32)..(col2 as u32 + 1) {
            for row in row1..(row2 + 1) {
                res.push(format!("{}{}", char::from_u32(col_ind).unwrap_or('0'), row));
            }
        }
        res
    }
}
