#An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

#Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

#To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

#At the end, return the modified image.

#Example 1:
#Input: 
#image = [[1,1,1],[1,1,0],[1,0,1]]
#sr = 1, sc = 1, newColor = 2
#Output: [[2,2,2],[2,2,0],[2,0,1]]
#Explanation: 
#From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
#by a path of the same color as the starting pixel are colored with the new color.
#Note the bottom corner is not colored 2, because it is not 4-directionally connected
#to the starting pixel.


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue=list()
        
        row_len=len(image)
        
        col_len=len(image[0])
                
        queue.append((sr,sc))
        
        visited=set()
        
        base_color=image[sr][sc]
        
        while(len(queue)>0):
            
            row,col=queue.pop(0);
            
            if image[row][col]==base_color:
                image[row][col]=newColor
            else:
                continue
            
            if (row-1)>=0 and ((row-1,col) not in visited):
                queue.append((row-1,col))
                #print('up')
                
            if (row+1)<row_len and ((row+1,col) not in visited):
                queue.append((row+1,col))
                #print('down')
                
            if (col-1)>=0 and ((row,col-1) not in visited):
                queue.append((row,col-1))
                #print('left')
            
            if (col+1)<col_len and ((row,col+1) not in visited):
                queue.append((row,col+1))
                #print('right')
            
            visited.add((row,col))
            #print(queue)
                
        return image
        
