class TimeMap:

    def __init__(self):
        self.tmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        exist_val = self.tmap.get(key,None)
        tup = (value, timestamp)
        if exist_val:
            self.tmap[key].append(tup)
        else:
            self.tmap[key] = [tup]

    def get(self, key: str, timestamp: int) -> str:
        val = self.tmap.get(key,None)
        if not val:
            return ""
        else:
            max_ts = ""
            l, r = 0, len(val) - 1
            while l<=r:
                mid = (l+r)//2
                if val[mid][1] <= timestamp:
                    l = mid + 1
                    max_ts = val[mid][0]
                else:
                    r = mid - 1
            return max_ts

        
