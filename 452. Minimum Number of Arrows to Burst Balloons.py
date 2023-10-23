class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points.sort(key=lambda x: x[1])

        arrow_count = 1
        arrow_position = points.pop(0)[1]

        for index, point in enumerate(points):
            if(arrow_position < point[0]):
                arrow_count += 1
                arrow_position = point[1]
            else:
                continue

        print(arrow_count)
        return arrow_count

test = Solution()
test.findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])
        
        