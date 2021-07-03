class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def insert(self, intervals, newInterval):
        results = []
        if newInterval == None:
            results.append(newInterval)
            return results

        intervals.append(newInterval)
        intervals.sort(key=lambda x: x.start)

        print(intervals)

        res.append(intervals[0])
        # scan the list
        for i in range(1, len(intervals)):
            cur = intervals[i]
            pre = res[-1]
            # check if current interval intersects with previous one
            if cur.start <= pre.end:
                res[-1].end = max(pre.end, cur.end)  # merge
            else:
                res.append(cur)  # insert

        return res

print(Solution().insert(Interval(1,5), Interval(2,6)))
