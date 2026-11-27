# You are given two string arrays positive_feedback and negative_feedback, containing the words denoting positive and negative feedback, respectively. Note that no word is both positive and negative.
# Initially every student has 0 points. Each positive word in a feedback report increases the points of a student by 3, whereas each negative word decreases the points by 1.
# You are given n feedback reports, represented by a 0-indexed string array report and a 0-indexed integer array student_id, where student_id[i] represents the ID of the student who has received the feedback report report[i]. The ID of each student is unique.
# Given an integer k, return the top k students after ranking them in non-increasing order by their points. In case more than one student has the same points, the one with the lower ID ranks higher.
class Solution:
    def topStudents(self, positive_feedback: list[str], negative_feedback: list[str], report: list[str], student_id: list[int], k: int) -> list[int]:
        positive_feedback = set(positive_feedback)
        negative_feedback = set(negative_feedback)
        results = []
        for sentence in report:
            words = sentence.split(" ")
            score = 0
            for word in words:
                if word in positive_feedback:
                    score += 3
                elif word in negative_feedback:
                    score -= 1
            results.append(score)
        return [x for _, x in sorted(zip(results, student_id), key=lambda pair: (-pair[0], pair[1]))][:k]
