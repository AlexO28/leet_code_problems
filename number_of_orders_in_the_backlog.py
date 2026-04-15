# You are given a 2D integer array orders, where each orders[i] = [pricei, amounti, orderTypei] denotes that amounti orders have been placed of type orderTypei at the price pricei. The orderTypei is:
# 0 if it is a batch of buy orders, or
# 1 if it is a batch of sell orders.
# Note that orders[i] represents a batch of amounti independent orders with the same price and order type. All orders represented by orders[i] will be placed before all orders represented by orders[i+1] for all valid i.
# There is a backlog that consists of orders that have not been executed. The backlog is initially empty. When an order is placed, the following happens:
# If the order is a buy order, you look at the sell order with the smallest price in the backlog. If that sell order's price is smaller than or equal to the current buy order's price, they will match and be executed, and that sell order will be removed from the backlog. Else, the buy order is added to the backlog.
# Vice versa, if the order is a sell order, you look at the buy order with the largest price in the backlog. If that buy order's price is larger than or equal to the current sell order's price, they will match and be executed, and that buy order will be removed from the backlog. Else, the sell order is added to the backlog.
# Return the total amount of orders in the backlog after placing all the orders from the input. Since this number can be large, return it modulo 109 + 7.
import heapq
from typing import List


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        buy_heap = []
        sell_heap = []
        for price, amount, orderType in orders:
            if orderType == 0:
                while amount > 0 and sell_heap and sell_heap[0][0] <= price:
                    s_price, s_amount = heapq.heappop(sell_heap)
                    if s_amount > amount:
                        heapq.heappush(sell_heap, [s_price, s_amount - amount])
                        amount = 0
                    else:
                        amount -= s_amount
                if amount > 0:
                    heapq.heappush(buy_heap, [-price, amount])
            else:
                while amount > 0 and buy_heap and -buy_heap[0][0] >= price:
                    b_price_neg, b_amount = heapq.heappop(buy_heap)
                    if b_amount > amount:
                        heapq.heappush(buy_heap, [b_price_neg, b_amount - amount])
                        amount = 0
                    else:
                        amount -= b_amount
                if amount > 0:
                    heapq.heappush(sell_heap, [price, amount])
        return (
            sum(amt for price, amt in buy_heap) + sum(amt for price, amt in sell_heap)
        ) % 1000000007
