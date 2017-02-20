class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if(num==0) :
            return "0"
         
        n = num; 
        if(num>0) : 
            return self.convertAbsToBase7(n);
        else :
            return "-"+self.convertAbsToBase7(-n);
    
    def convertAbsToBase7(self, num):
        if num < 7 :
            return str(num)
        
        loop =1;
        total = 0;
        while(total<num) :
            total = pow(7,loop)-1
            loop+=1
         
        result = "";  
        loop -= 2  
        while(loop>=1) :
            d = pow(7, loop)
            div = num / d
            result+=str(div)
            num = num % d
            loop -= 1
              
        result+=str(num)    
        return result 
            
s = Solution()
print(s.convertToBase7(-8))