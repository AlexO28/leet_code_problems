# Due to a bug, there are many duplicate folders in a file system. You are given a 2D array paths, where paths[i] is an array representing an absolute path to the ith folder in the file system.
# Two folders (not necessarily on the same level) are identical if they contain the same non-empty set of identical subfolders and underlying subfolder structure. The folders do not need to be at the root level to be identical. If two or more folders are identical, then mark the folders as well as all their subfolders.
# However, if the file structure also included the path "/b/w", then the folders "/a" and "/b" would not be identical. Note that "/a/x" and "/b/x" would still be considered identical even with the added folder.
# Once all the identical folders and their subfolders have been marked, the file system will delete all of them. The file system only runs the deletion once, so any folders that become identical after the initial deletion are not deleted.
# Return the 2D array ans containing the paths of the remaining folders after deleting all the marked folders. The paths may be returned in any order.
from typing import List
from collections import defaultdict


class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Trie()
        for path in paths:
            cur = root
            for name in path:
                if cur.children[name] is None:
                    cur.children[name] = Trie()
                cur = cur.children[name]
        self.g = {}
        self.search(root)
        self.ans = []
        self.path = []
        self.search2(root)
        return self.ans

    def search(self, node: Trie) -> str:
        if not node.children:
            return ""
        else:
            subs = []
            for name, child in node.children.items():
                subs.append(f"{name}({self.search(child)})")
            s = "".join(sorted(subs))
            if s in self.g:
                node.deleted = True
                self.g[s].deleted = True
            else:
                self.g[s] = node
            return s

    def search2(self, node: Trie) -> None:
        if not node.deleted:
            if self.path:
                self.ans.append(self.path[:])
            for name, child in node.children.items():
                self.path.append(name)
                self.search2(child)
                self.path.pop()


class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)
        self.deleted = False
