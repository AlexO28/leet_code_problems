# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
# For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_dict = {}
        for ticket in tickets:
            if ticket[0] in ticket_dict.keys():
                ticket_dict[ticket[0]].append(ticket[1])
            else:
                ticket_dict[ticket[0]] = [ticket[1]]
        for elem in ticket_dict.keys():
            ticket_dict[elem].sort()
        stack = ["JFK"]
        path = []
        while len(stack) > 0:
            top = stack[-1]
            if top not in ticket_dict.keys():
                path.append(top)
                stack.pop()
            elif len(ticket_dict[top]) == 0:
                path.append(top)
                stack.pop()
            else:
                stack.append(ticket_dict[top][0])
                del ticket_dict[top][0]
        return path[::-1]
  
