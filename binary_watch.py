# Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        HOURS = ['1', '2', '4', '8']
        MINUTES = ['01', '02', '04', '08', '16', '32'] 
        hours_dict = {0: ['0'],
                      1: HOURS,
                      2: ['3', '5', '6', '9', '10'],
                      3: ['7', '11'],
                      4: []}
        minutes_dict = {0: ['00'],
                        1: MINUTES,
                        2: ['03', '05', '09', '17', '33', '06', '10', '18', '34', '12', '20', '36', '24', '40', '48'],
                        3: ['07', '11', '13', '14', '19', '21', '22', '25', '26', '28', '35', '37', '38', '41', '42', '44', '49', '50', '52', '56'],
         4: ['15', '23', '27', '29', '30', '39', '43', '45', '46', '51', '53', '54', '57', '58'],
         5: ['31', '47', '55', '59'],
         6: []}
        res = []
        for i in range(0, 5):
            hours = hours_dict[i]
            if len(hours) > 0:
                if turnedOn - i in minutes_dict:
                    minutes = minutes_dict[turnedOn - i]
                    if len(minutes) > 0:
                        for hour in hours:
                            for minute in minutes:
                                res.append(hour+":"+minute)
        return list(set(res))
