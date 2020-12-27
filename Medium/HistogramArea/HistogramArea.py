'''
Histogram Area from Coderbyte
December 2020 Jakub Kazimierski
'''

def max_area_histogram(histogram): 
      
    stack = list() 
  
    max_area = 0 
  
    index = 0
    while index < len(histogram): 
  
        # while next bar is higher than last appended, append it position to the stack
        if (not stack) or (histogram[stack[-1]] <= histogram[index]): 
            stack.append(index) 
            index += 1
        else: 
            # else remove last appended elem from the stack
            top_of_stack = stack.pop() 
            # count area created by this element
            # (e.g if 2 is after 3, 3 was removed before 2
            # so 2 start from position of 3, and area counted at 2
            # is 2*2= 4)
            area = (histogram[top_of_stack] * 
                   ((index - stack[-1] - 1)  
                   if stack else index)) 
  
            # update max possible area
            max_area = max(max_area, area) 
  
    while stack: 
        # repeat procees for elements' positions which still are on stack
        # (e.g. it can be positions of 1, and if arr has length 5 and histogram started from 1
        # so area is counted as 5*1 = 5)
        top_of_stack = stack.pop() 
  
        area = (histogram[top_of_stack] * 
              ((index - stack[-1] - 1)  
                if stack else index)) 
  
  
        max_area = max(max_area, area) 
  
    return max_area 

def HistogramArea(arr):
    '''
    Have the function HistogramArea(arr) 
    read the array of non-negative integers 
    stored in arr which will represent the 
    heights of bars on a graph (where each bar width is 1), 
    and determine the largest area underneath the entire bar 
    graph. 
    
    For example: if arr is [2, 1, 3, 4, 1] then this looks 
    like the following bar graph:
 
              __
           __|  |
     __   |xx|xx|
    |  |__|xx|xx|__
    |  |  |xx|xx|  |

    You can see in the above bar graph that the largest 
    area underneath the graph is covered by the x's. 
    The area of that space is equal to 6 because the 
    entire width is 2 and the maximum (common) height is 3, 
    therefore 2 * 3 = 6. Your program should return 6. 
    The array will always contain at least 1 element.
    '''
    
    return max_area_histogram(arr)



  