'''
HTML elements from Coderbyte
December 2020 Jakub Kazimierski
'''

def HTMLelements(strParam):
    '''
    Have the function HTMLElements(str) 
    read the str parameter being passed 
    which will be a string of HTML DOM 
    elements and plain text. The elements 
    that will be used are: b, i, em, div, p. 
    
    For example: if str is "<div><b><p>hello world</p></b></div>" 
    then this string of DOM elements is nested correctly so your 
    program should return the string true.

    If a string is not nested correctly, return the first 
    element encountered where, if changed into a different 
    element, would result in a properly formatted string. 
    If the string is not formatted properly, then it will 
    only be one element that needs to be changed. 
    
    For example: if str is "<div><i>hello</i>world</b>" 
    then your program should return the string div because if 
    the first <div> element were changed into a <b>, the string 
    would be properly formatted.
    '''
    
    stack_opening = []
    
    # below append to stack opening tags 
    # and when ending tag appears compares it's
    # first letter with last apppended elem on stack
    for char_id in range(len(strParam)):

        if strParam[char_id] == '<':
            traverse_id = char_id + 1

            # if ending tag
            if strParam[traverse_id] == "/":
                # compare first letters of last elem at stack and ending tag
                if strParam[traverse_id + 1] != stack_opening[-1][0]:
                    return stack_opening[-1]
                else:
                    # if tag is nested correct remove it from stack
                    stack_opening.pop(-1)    
            else:
                tag = ""
                while strParam[traverse_id] != ">":
                    tag += strParam[traverse_id]
                    traverse_id += 1
                # append opening tag to stack
                stack_opening.append(tag)

    return "true"