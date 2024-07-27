# There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
# You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        flights_dict = {}
        for flight in flights:
            if flight[0] in flights_dict:
                flights_dict[flight[0]].append([flight[1], flight[2]])
            else:
                flights_dict[flight[0]] = [[flight[1], flight[2]]]
        cities = {src: 0}
        achieved = None
        while k >= 0:
            new_cities = {}
            for city in cities.keys():
                if city in flights_dict:
                    for flight in flights_dict[city]:
                        if flight[0] in new_cities:
                            new_cities[flight[0]] = min(new_cities[flight[0]], cities[city] + flight[1])
                        else:
                            new_cities[flight[0]] = cities[city] + flight[1]
            cities = new_cities
            if len(cities) == 0:
                break
            if dst in cities.keys():
                if achieved is None:
                    achieved = cities[dst]
                else:
                    achieved = min(achieved, cities[dst]) 
            k -= 1
        if achieved is None:
            return -1
        else:
            return achieved
