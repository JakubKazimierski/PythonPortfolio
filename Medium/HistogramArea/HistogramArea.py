'''
Histogram Area from Coderbyte
December 2020 Jakub Kazimierski
'''

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


def max_area_histogram(histogram): 
      
    # This function calulates maximum  
    # rectangular area under given  
    # histogram with n bars 
  
    # Create an empty stack. The stack  
    # holds indexes of histogram[] list.  
    # The bars stored in the stack are 
    # always in increasing order of  
    # their heights. 
    stack = list() 
  
    max_area = 0 # Initialize max area 
  
    # Run through all bars of 
    # given histogram 
    index = 0
    while index < len(histogram): 
          
        # If this bar is higher  
        # than the bar on top 
        # stack, push it to stack 
  
        if (not stack) or (histogram[stack[-1]] <= histogram[index]): 
            stack.append(index) 
            index += 1
  
        # If this bar is lower than top of stack, 
        # then calculate area of rectangle with  
        # stack top as the smallest (or minimum 
        # height) bar.'i' is 'right index' for  
        # the top and element before top in stack 
        # is 'left index' 
        else: 
            # pop the top 
            top_of_stack = stack.pop() 
  
            # Calculate the area with  
            # histogram[top_of_stack] 
            # from index of previous bar
            area = (histogram[top_of_stack] * 
                   ((index - stack[-1] - 1)  
                   if stack else index)) 
  
            # update max area, if needed 
            max_area = max(max_area, area) 
  
    # Now pop the remaining bars from  
    # stack and calculate area with  
    # every popped bar as the smallest bar 
    while stack: 
          
        # pop the top 
        top_of_stack = stack.pop() 
  
        # Calculate the area with  
        # histogram[top_of_stack]  
        # stack as smallest bar 
        area = (histogram[top_of_stack] * 
              ((index - stack[-1] - 1)  
                if stack else index)) 
  
        # update max area, if needed 
        max_area = max(max_area, area) 
  
    # Return maximum area under  
    # the given histogram 
    return max_area 
  