# Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.
# If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".
# The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for elem in folder:
            found = False
            for parent in res:
                if (parent == elem) or elem.startswith(parent + "/"):
                    found = True
                    break
            if not found:
                res.append(elem)
        return res