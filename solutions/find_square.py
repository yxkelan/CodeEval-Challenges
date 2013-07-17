#
# You have coordinates of four points on a plane. Check whether they make a square.
#  
# Solution: 1. suppose 4 points: p1, p2, p3, p4
#           2. Calculate the distances from p1 to other points.
#           3. If all 3 distances are equal, return false
#              otherwise, find the largest distance, set it as diagonal distance
#              if other 2 distances are same(edge), return the point which is not the diagonal point.
#              Otherwise, return false
#           4. Caluate the distances from returned point to other points. repeate step 3. If it has
#              diagnoal distance and edge, compare them with p1's results. If they are same respectivly, 
#              these 4 points construct a square, otherwise not. 
#

import re
import math
import operator

def index_max( A ):
    """output: index, max"""
    return max(enumerate(A), key = operator.itemgetter(1))

class Solution:

    """ 
    Find if 4 points construct to a square or not.
    """
    def __init__(self):
        self.diagonal = 0
        self.edge = 0

    def checkSquare(self, s):
        """ 
        Calculate the distances of p1 to other points, and pX to other points(if pX exists).
        """
        points = self.process(s)

        distances = map(self.distance, [points[0], points[0], points[0]], points[1:])
        index = self.compare(distances)
        if not index:
            return False

        diagonal =  self.diagonal
        edge = self.edge
        y_list = points[0:index] + points[index+1:] if index != 3 else points[0:3]

        distances = map(self.distance, [points[index],points[index],points[index]],y_list)
        index = self.compare(distances)
        if not index:
            return False

        if diagonal == self.diagonal and edge == self.edge:
            return True

        return False 

    def distance(self, p1, p2):
        """
        Calculate distance of 2 points
        """
        p1x, p1y = p1[0], p1[1]
        p2x, p2y = p2[0], p2[1]

        return math.sqrt((p1x-p2x)**2 + (p1y-p2y)**2)


    def process(self, s):
        """
        Process input string, return a list of coordinates of 4 points.
        """
        s_list = s.split(',')
        values = [ v.strip(" ()\n") for v in s_list ]
        points = []
        i = 0
        while i < len(values):
            points.append([int(values[i]),int(values[i+1])])
            i += 2
        return points

    def compare(self, distances):
        """
        Find if diagonal and edge exists or not, return a non-diagonal point or 0(not exists)
        """
        if all( d == distances[0] for d in distances):
            return 0

        index, maxv = index_max(distances)
        self.diagonal = maxv

        if index == 0 and distances[1] == distances[2]:
            self.edge = distances[1]
            return 2
        elif index == 1 and distances[0] == distances[2]:
            self.edge = distances[0]
            return 3
        elif index == 2 and distances[0] == distances[1]:
            self.edge = distances[0]
            return 1

        return 0


def main():
    import sys
    test_cases = open(sys.argv[1], 'r')
    solution = Solution()
    for test in test_cases:
        print solution.checkSquare(test)
    test_cases.close()
    return 0

if __name__ == "__main__":
    main()








