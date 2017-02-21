'''
Created on 20 Feb 2017

@author: ezng
'''
from Carbon.Aliases import false
class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        if(len(board)==0) :
            return 0;
        
        h=len(board)
        
        if(len(board[0])==0) :
            return 0;
        
        w=len(board[0])
        
        result=0
        
        grid = [[False for x in range(0,w,1)] for y in range(0,h,1)] 
        
        for i in range(0,h,1) :
            for j in range(0,w,1) :
                if(grid[i][j]==True) :
                    continue
                elif(board[i][j] == '.') :
                    grid[i][j] = True
                    continue
                else :
                    hasleft = False
                    hasTop = False
                    
                    if(i==0) :
                        hasTop=False
                    else :
                        hasTop = True if board[i-1][j]=='X' else False
                    
                    if(j==0) :
                        hasleft=False
                    else :
                        hasleft = True if board[i][j-1]=='X' else False
                    
                if(hasleft == False and hasTop == False) :
                    result+=1
                    grid[i][j]=True
                     
        return result              
        
#board=[['X','.','.','X'],['.','.','.','X'],['.','.','.','X']]
board=[['.','.'],['X','X']]      
s=Solution()
print(s.countBattleships(board)    )