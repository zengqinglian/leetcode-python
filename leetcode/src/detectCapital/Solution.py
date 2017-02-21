'''
Created on 21 Feb 2017

@author: ezng
'''
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        findLowerCase=False
        
        index = 0;
        firstLowerIndex = 0;
        for c in word :
            if (c>='A'  and c<='Z') :
                if(findLowerCase==True) :
                    return False
            elif(findLowerCase==False) :
                findLowerCase = True 
                firstLowerIndex=index   
            index+=1  
        if(firstLowerIndex>1) :
            return False
        return True                
                