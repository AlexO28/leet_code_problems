# Design a data structure that can efficiently manage data packets in a network router. Each data packet consists of the following attributes:
# source: A unique identifier for the machine that generated the packet.
# destination: A unique identifier for the target machine.
# timestamp: The time at which the packet arrived at the router.
# Implement the Router class:
# Router(int memoryLimit): Initializes the Router object with a fixed memory limit.
# memoryLimit is the maximum number of packets the router can store at any given time.
# If adding a new packet would exceed this limit, the oldest packet must be removed to free up space.
# bool addPacket(int source, int destination, int timestamp): Adds a packet with the given attributes to the router.
# A packet is considered a duplicate if another packet with the same source, destination, and timestamp already exists in the router.
# Return true if the packet is successfully added (i.e., it is not a duplicate); otherwise return false.
# int[] forwardPacket(): Forwards the next packet in FIFO (First In First Out) order.
# Remove the packet from storage.
# Return the packet as an array [source, destination, timestamp].
# If there are no packets to forward, return an empty array.
# int getCount(int destination, int startTime, int endTime):
# Returns the number of packets currently stored in the router (i.e., not yet forwarded) that have the specified destination and have timestamps in the inclusive range [startTime, endTime].
# Note that queries for addPacket will be made in increasing order of timestamp.
from typing import List
import collections
from sortedcontainers import SortedList


class Router:

    def __init__(self, memoryLimit: int):
        self.__size = memoryLimit
        self.__q = collections.deque()
        self.__lookup = collections.defaultdict(SortedList)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (timestamp, source) in self.__lookup[destination]:
            return False
        else:
            self.__lookup[destination].add((timestamp, source))
            if len(self.__q) == self.__size:
                s, d, t = self.__q.popleft()
                self.__lookup[d].remove((t, s))
            self.__q.append((source, destination, timestamp))
            return True

    def forwardPacket(self) -> List[int]:
        if not self.__q:
            return []
        s, d, t = self.__q.popleft()
        self.__lookup[d].remove((t, s))
        return [s, d, t]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        return self.__lookup[destination].bisect_left((endTime + 1, 0)) - self.__lookup[
            destination
        ].bisect_left((startTime, 0))

