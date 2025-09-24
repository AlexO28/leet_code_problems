# Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.
# Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.
from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        food_items = set()
        info = {}
        tables = set()
        for order in orders:
            code = order[1] + "_" + order[2]
            if code in info:
                info[code] += 1
            else:
                info[code] = 1
            tables.add(int(order[1]))
            food_items.add(order[2])
        food_items = list(food_items)
        food_items.sort()
        tables = list(tables)
        tables.sort()
        line = ["Table"]
        line.extend(food_items)
        res = [line]
        for table in tables:
            table_id = str(table)
            line = [table_id]
            for food_item in food_items:
                code = table_id + "_" + food_item
                if code in info:
                    line.append(str(info[code]))
                else:
                    line.append("0")
            res.append(line)
        return res
