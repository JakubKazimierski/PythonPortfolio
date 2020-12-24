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
    
    div_count = b_count = i_count = em_count = p_count = 0
    string_to_split = ""

    for char in strParam:
        if char == '>':
            string_to_split += char + ' '
        elif char == '<':
            string_to_split += ' ' + char
        else:
            string_to_split += char    

    elements_occurence = list(filter(None, string_to_split.split(' ')))

    # only one element is at wrong place, so that's mean tags are not mixed
    # like <div><b></div></b>
    for elem in elements_occurence:
        
        # if element has no end tag after itself sum is different than 0 
        if elem == '<div>':
            div_count += 1        
        if elem == '</div>' and div_count > 0:
            div_count -= 1

        if elem == '<b>':
            b_count += 1 
        if elem == '</b>' and b_count > 0:
            b_count -= 1 

        if elem == '<i>':
            i_count += 1 
        if elem == '</i>' and i_count > 0:
            i_count -= 1 

        if elem == '<em>':
            em_count += 1 
        if elem == '</em>' and em_count > 0:
            em_count -= 1 

        if elem == '<p>':
            p_count += 1 
        if elem == '</p>' and p_count > 0:
            p_count -= 1 

    if div_count != 0:
        return 'div'
    if b_count != 0:
        return 'b'
    if i_count != 0:
        return 'i'
    if em_count != 0:
        return 'em'
    if p_count != 0:
        return 'p'


    return "true"