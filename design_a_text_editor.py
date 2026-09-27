# Design a text editor with a cursor that can do the following:
# Add text to where the cursor is.
# Delete text from where the cursor is (simulating the backspace key).
# Move the cursor either left or right.
# When deleting text, only characters to the left of the cursor will be deleted. The cursor will also remain within the actual text and cannot be moved beyond it. More formally, we have that 0 <= cursor.position <= currentText.length always holds.
# Implement the TextEditor class:
# TextEditor() Initializes the object with empty text.
# void addText(string text) Appends text to where the cursor is. The cursor ends to the right of text.
# int deleteText(int k) Deletes k characters to the left of the cursor. Returns the number of characters actually deleted.
# string cursorLeft(int k) Moves the cursor to the left k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
# string cursorRight(int k) Moves the cursor to the right k times. Returns the last min(10, len) characters to the left of the cursor, where len is the number of characters to the left of the cursor.
from collections import deque


class TextEditor:

    def __init__(self):
        self.queue_left = deque([])
        self.queue_right = deque([])

    def addText(self, text: str) -> None:
        self.queue_left.extend(list(text))

    def deleteText(self, k: int) -> int:
        num_deleted = 0
        for j in range(k):
            try:
                elem = self.queue_left.pop()
                num_deleted += 1
            except:
                break
        return num_deleted

    def cursorLeft(self, k: int) -> str:
        for j in range(k):
            try:
                elem = self.queue_left.pop()
            except:
                break
            self.queue_right.appendleft(elem)
        moved = []
        for j in range(1, 11):
            try:
                moved.append(self.queue_left[-j])
            except:
                break
        return "".join(moved[::-1])
                

    def cursorRight(self, k: int) -> str:
        for j in range(k):
            try:
                elem = self.queue_right.popleft()
            except:
                break
            self.queue_left.append(elem)
        moved = []
        for j in range(1, 11):
            try:
                moved.append(self.queue_left[-j])
            except:
                break
        return "".join(moved[::-1])

# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)
