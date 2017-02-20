'''
Created on 20 Feb 2017

@author: ezng
'''
import math
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        
        result = list();
        
        if(area==0) :
            result.append(0)
            result.append(0)
            return result
        
        if(area==1) :
            result.append(1)
            result.append(1)
            return result
        
        startPoint = int(math.sqrt(area))
        
        if(startPoint * startPoint == area) :
            result.append(startPoint)
            result.append(startPoint)
            return result
            
        else :
            testNum = startPoint
            while(area % testNum != 0) :
                testNum-=1
            
            result.append(area/testNum)
            result.append(testNum)    
            
        return result

s = Solution()
print(s.constructRectangle(2))