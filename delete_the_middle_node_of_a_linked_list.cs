/*
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.
For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
*/
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
using System.Collections.Generic;


public class Solution {
    public ListNode DeleteMiddle(ListNode head) {
        List<int> numbers = new List<int>();
        while (head is not null) {
            numbers.Add(head.val);
            head = head.next;
        }
        numbers.RemoveAt(numbers.Count / 2);
        ListNode res = null;
        for (int i = numbers.Count - 1; i >= 0; --i) {
            res = new ListNode(numbers[i], res);
        }
        return res;
    }
}
