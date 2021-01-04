'''
Polynomial Expansion from Coderbyte
January 2021 Jakub Kazimierski
'''

def PolynomialExpansion(strParam):
    '''
    Have the function PolynomialExpansion(str) 
    take str which will be a string representing 
    a polynomial containing only (+/-) integers, 
    a letter, parenthesis, and the symbol "^", 
    and return it in expanded form. 
    
    For example: if str is "(2x^2+4)(6x^3+3)", 
    then the output should be "12x^5+24x^3+6x^2+12". 
    Both the input and output should contain no spaces. 
    The input will only contain one letter, such as 
    "x", "y", "b", etc. There will only be four parenthesis 
    in the input and your output should contain no parenthesis. 
    The output should be returned with the highest exponential 
    element first down to the lowest.

    More generally, the form of str will be: 
    ([+/-]{num}[{letter}[{^}[+/-]{num}]]...[[+/-]{num}]...)(copy) 
    where "[]" represents optional features, "{}" represents mandatory 
    features, "num" represents integers and "letter" represents 
    letters such as "x".
    '''
    
    var = ''
    for char in strParam:
        if char.isalpha():
            var = char 
            break
        
    strParam = strParam.replace(var + '^', ' ').replace(var, ' 1').replace('+', ' +').replace('-', ' -')
    polys = strParam.split(')(')
    poly_pairs = []
    for poly in polys:
        poly = poly.replace('(', '').replace(')', '').split()
        if len(poly) % 2 != 0: poly.append('0')
        poly = [(int(poly[i + 1]), int(poly[i])) for i in range(0, len(poly), 2)]
        poly_pairs.append(poly)
    result_dict = {}
    for exp1, coeff1 in poly_pairs[0]:
        for exp2, coeff2 in poly_pairs[1]:
            result_dict[exp1 + exp2] = result_dict.setdefault(exp1 + exp2, 0) + coeff1*coeff2
    result = ''
    for exp, coeff in sorted(result_dict.items(), reverse=True):
        result += f'{f"{coeff:+}"[0] if coeff == 1 else f"{coeff:+}"}{"" if exp == 0 else var}{"" if exp in (0, 1) else "^" + str(exp)}'
        if result[0] == '+': result = result[1:]
    return result

