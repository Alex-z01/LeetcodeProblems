import math
from collections import defaultdict
from functools import cache

# Time complexity: O(N + k)O(N+k)
# Space complexity: O(N + k)O(N+k)
def deleteAndEarnTopDown(self, nums: list[int]) -> int:
    points = defaultdict(int)
    maxNum = 0

    for num in nums:
        points[num] += num
        maxNum = max(maxNum, num)

    @cache
    def maxPoints(num):
        if num == 0:
            return 0
        if num == 1:
            return points[1]

        return max(maxPoints(num - 1), maxPoints(num - 2) + points[num])

    return maxPoints(maxNum)

# Time complexity: O(N + k)O(N+k)
# Space complexity: O(N + k)O(N+k)
def deleteAndEarnBottomUp(self, nums: list[int]) -> int:
    points = defaultdict(int)
    maxNum = 0

    for num in nums:
        points[num] += num
        maxNum = max(maxNum, num)

    maxPoints = [0] * (maxNum + 1)
    maxPoints[1] = points[1]

    for i in range(2, len(maxPoints)):
        maxPoints[i] = max(maxPoints[i - 1], maxPoints[i - 2] + points[i])

    return maxPoints[maxNum]

# Time complexity: O(N + k)O(N+k)
# Space complexity: O(N)O(N)
def deleteAndEarnSpaceOptimized(self, nums: list[int]) -> int:
    points = defaultdict(int)
    maxNum = 0

    for num in nums:
        points[num] += num
        maxNum = max(maxNum, num)

    # Base cases
    twoBack = 0
    oneBack = points[1]

    for num in range(2, maxNum + 1):
        twoBack, oneBack = oneBack, max(oneBack, twoBack + points[num])

    return oneBack

# Time complexity: O(N⋅log(N)
# Space complexity: O(N)
def deleteAndEarnIterate(self, nums: list[int]) -> int:
    points = defaultdict(int)

    for num in nums:
        points[num] += num

    elements = sorted(points.keys())
    twoBack = 0
    oneBack = points[elements[0]]

    for i in range(1, len(elements)):
        currentElement = elements[i]
        if currentElement == elements[i - 1] + 1:
            # The 2 elements are adjacent, cannot take both - apply normal recurrence
            twoBack, oneBack = oneBack, max(oneBack, twoBack + points[currentElement])
        else:
            # Otherwise, we don't need to worry about adjacent deletions
            twoBack, oneBack = oneBack, oneBack + points[currentElement]

    return oneBack

# Time Complexity : O(N + min(k, N * log(N))
# Space Complexity : O(N)
def deleteAndEarnBest(self, nums: list[int]) -> int:
    points = defaultdict(int)
    maxNum = 0

    for num in nums:
        points[num] += num
        maxNum = max(maxNum, num)

    twoBack = oneBack = 0
    n = len(points)

    if maxNum < n + n * math.log(n, 2):
        oneBack = points[1]
        for num in range(2, maxNum + 1):
            twoBack, oneBack = oneBack, max(oneBack, twoBack + points[num])
    else:
        elements = sorted(points.keys())
        oneBack = points[elements[0]]

        for i in range(1, len(elements)):
            currentElement = elements[i]
            if currentElement == elements[i - 1] + 1:
                # The 2 elements are adjacent, cannot take both - apply normal recurrence
                twoBack, oneBack = oneBack, max(oneBack, twoBack + points[currentElement])
            else:
                # Otherwise, we don't need to worry about adjacent deletions
                twoBack, oneBack = oneBack, oneBack + points[currentElement]

    return oneBack