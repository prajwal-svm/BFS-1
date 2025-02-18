# 207. Course Schedule

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

# Intuition:
# Use a graph to represent the courses and their dependencies.
# Use a BFS approach to check if the courses can be completed by checking the in-degree of each course.
# If the in-degree of a course is 0, it means that the course has no dependencies and can be completed.
# Add the course to the queue.
# Process the courses in the queue.
# If the in-degree of a course is 0, add it to the queue.
# If the number of processed courses is equal to the number of courses, return True.
# Otherwise, return False.

from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0]*numCourses
        prereqToCourseMap = {i:[] for i in range(numCourses)}

        for course, pre in prerequisites:
            inDegree[course]+=1
            prereqToCourseMap[pre].append(course)

        queue = deque([i for i in range(numCourses) if inDegree[i] == 0])
        
        processed = 0
        while queue:
            course = queue.popleft()
            processed +=1
            for dep in prereqToCourseMap[course]:
                inDegree[dep]-=1
                if inDegree[dep] == 0:
                    queue.append(dep)

        return processed == numCourses
    