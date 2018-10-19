class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        if numCourses<2 or len(prerequisites)<2:
            return True
        #prerequisites.sort()
        while True:
            count=0
            mark = [True]*numCourses
            for pre in prerequisites:
                mark[pre[0]] = False
            for pre in prerequisites:
                if mark[pre[1]]:
                    count+=1
                    prerequisites.remove(pre)
            if prerequisites==[]:
                return True
            elif count==0:
                return False
