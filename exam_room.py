# There is an exam room with n seats in a single row labeled from 0 to n - 1.
# When a student enters the room, they must sit in the seat that maximizes the distance to the closest person. If there are multiple such seats, they sit in the seat with the lowest number. If no one is in the room, then the student sits at seat number 0.
# Design a class that simulates the mentioned exam room.
# Implement the ExamRoom class:
# ExamRoom(int n) Initializes the object of the exam room with the number of the seats n.
# int seat() Returns the label of the seat at which the next student will set.
# void leave(int p) Indicates that the student sitting at seat p will leave the room. It is guaranteed that there will be a student sitting at seat p.
class ExamRoom:

    def __init__(self, n: int):
        self.students_dict = {}
        self.n = n

    def seat(self) -> int:
        if len(self.students_dict) == 0:
            self.students_dict[0] = 1
            return 0
        else:
            keys = list(self.students_dict.keys())
            keys.sort()
            max_len = -1
            best_elem = -1
            for j in range(len(keys)+1):
                if j == 0:
                    cur_len = keys[0]-1
                    cur_elem = 0    
                elif j == len(keys):
                    cur_len = self.n-1 - keys[-1] - 1
                    cur_elem = self.n-1
                else:
                    main_part = (keys[j] - keys[j-1]) // 2
                    cur_len = main_part-1
                    cur_elem = keys[j-1]+cur_len+1
                if max_len < cur_len:
                    max_len = cur_len
                    best_elem = cur_elem
            self.students_dict[best_elem] = 1
            return best_elem

    def leave(self, p: int) -> None:
        del self.students_dict[p]
