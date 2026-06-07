from sortedcontainers import SortedDict

class TimeMap:

    def __init__(self):
        '''
        {
            key: [(val,ts),(val,ts)]
        }
        '''
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        val_pair=[timestamp,value]
        if not self.time_map.get(key):
            self.time_map[key] = [val_pair]
        else:
            self.time_map[key].append(val_pair)

    def get(self, key: str, timestamp: int) -> str:
        val_list = self.time_map.get(key)
        if not val_list:
            return ""
        res = ""
        l,r = 0, len(val_list) - 1
        while l<=r:
            mid = (l+r)//2
            if val_list[mid][0] <= timestamp:
                res = val_list[mid][1] 
                l = mid + 1
            else:
                r = mid -1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)