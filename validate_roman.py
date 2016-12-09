# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 21:01:13 2016

@author: bhupeshgupta
"""

'''
Validate Roman Numerals
Regex for validating Roman numerals 
Thousandth’s place - (M{0,3})
Hundreth’s place - ((C{1,3})|(CD)|(DC{0,3})|(CM))
Tenth’s place - ((X{1,3})|(XL)|(LX{0,3})|(XC))
Units Place - ((I{1,3})|(IV)|(VI{0,3})|(IX))

Units Place - I, II, III, IV, V, VI, VII, VIII, IX - Letters used = I, V, X
Tenths Place = X, XX, XXX, XL, L, LX, LXX, LXXX, XC Letters used = X, L, C
Hundreth’s place = C, CC, CCC, CD, D, DC, DCC, DCCC, CM Letters = C, D, M
Thousands Place = M, MM, MMM Letters = M 

Given input string S, check if ROman or Not 

Solution:
lets try to go from Left to Right and convert the string of roman into decimal. 
If we get an error then is_roman = False 
SO whats the deal. 
FIRST WE WILL TRY TO DO SOME VALIDATIONS - 
1) Max len = 15 
2) NO CHARACTER ISOUTSIDE MDCLXVI, 
for letter in S: if letter not in 'MDCLXVI' return false 
3) M,C,X,I <=3, D,L,V <=1


NEXT WE WILL TRY TO CONVERT ROMAN TO DECIMAL, IF ERROR THEN FALSE 

1) initialize with is_roman = True dec_num = 0, dec_dict = {"M": 1000, 'D': 500 ...}
2) While S: -> Get S[0] and S[1]

'''

def is_roman(S):
    '''
    Input - String in capital letters 
    Out True or False if roamn or not  
    '''
    # initializations 
    dec_num = 0 # decimal number for the given roman numeral string 
    dec_dict = {'M': 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, \
    "I": 1, "CM": 900, "CD": 400, "XC": 90, "XL":40, "IX": 9, "IV":4}
    
    #check if string has any char other than allowed 
    if len(S) > 15 : 
        return False
        
    for letter in S: 
        if letter not in "MDCLXVI":
            return False

    dup_s = S
    for rom_char in 'MDCLXVI':
        if rom_char == 'M' and (len(dup_s) - len(dup_s.replace("M", ""))) > 3:            
            if 'MMMCM' not in dup_s:
                return False
        else: 
            dup_s = dup_s.replace('M', "")

        if rom_char == 'D' and (len(dup_s) - len(dup_s.replace("D", ""))) >1:
            return False 
        else: 
            dup_s.replace('D', "")
        
        if rom_char == 'C' and (len(dup_s) - len(dup_s.replace("C", ""))) > 3:
            if 'CCCXC' not in dup_s:
                return False
        else: 
            dup_s.replace('C', "")

        if rom_char == 'X' and (len(dup_s) - len(dup_s.replace("X", ""))) >3:
            if 'XXXIX' not in dup_s:
                return False
        else: 
            dup_s.replace('X', "")

        if rom_char == 'I' and (len(dup_s) - len(dup_s.replace("I", ""))) >3:
            return False 
        else: 
            dup_s.replace('I', "")

        if rom_char == 'L' and (len(dup_s) - len(dup_s.replace("L", ""))) >1:
            return False 
        else: 
            dup_s.replace('L', "")
        
        if rom_char == 'V' and (len(dup_s) - len(dup_s.replace("V", ""))) >1:
            return False 
        else: 
            dup_s.replace('V', "")

    SD = S
    while SD[:-1]:
        s = SD[0]   
        if s == 'M':
            dec_num += dec_dict['M']
            SD = SD[1:]
        elif s == 'C' and SD[1] == 'M':
            dec_num += dec_dict['CM']
            SD = SD[2:]
        elif s == 'C' and SD[1] == 'D':
            dec_num += dec_dict['CD']
            SD = SD[2:]
        elif s == 'C' and (SD[1] == 'C' or 'L' or 'X' or 'V' or 'I'):
            dec_num += dec_dict['C']
            SD = SD[1:]
        elif s == 'D' and SD[1] == 'M':
            return False
        elif s == 'D' and (SD[1] == 'C' or 'L' or 'X' or 'V' or 'I'):
            dec_num += dec_dict['D']
            SD = SD[1:]

        elif s == 'X' and SD[1] == 'M':
            return False
        elif s == 'X' and SD[1] == 'D':
            return False
        elif s == 'X' and SD[1] == 'C':
            dec_num += dec_dict['XC']
            SD = SD[2:]
        elif s == 'X' and (SD[1] == 'L' or 'X' or 'V' or 'I'):
            dec_num += dec_dict['X']
            SD = SD[1:]
        elif s == 'L' and SD[1] == 'M':
            return False
        elif s == 'L' and SD[1] == 'D':
            return False
        elif s == 'L' and SD[1] == 'C':
            return False
        elif s == 'L' and (SD[1] == 'X' or 'V' or 'I'):
            dec_num += dec_dict['L']
            SD = SD[1:]      
        elif s == 'I' and SD[1] == 'M':
            return False
        elif s == 'I' and SD[1] == 'D':
            return False
        elif s == 'I' and SD[1] == 'C':
            return False
        elif s == 'I' and SD[1] == 'L':
            return False
        elif s == 'I' and SD[1] == 'X':
            dec_num += dec_dict['IX']
            SD = SD[2:]
        elif s == 'I' and SD[1] == 'V':
            dec_num += dec_dict['IV']
            SD = SD[2:]
        elif s == 'I' and (SD[1] == 'X' or 'V' or 'I'):
            dec_num += dec_dict['X']
            SD = SD[1:]       
        elif s == 'V' and SD[1] == 'M':
            return False
        elif s == 'V' and SD[1] == 'D':
            return False
        elif s == 'V' and SD[1] == 'C':
            return False
        elif s == 'V' and SD[1] == 'L':
            return False
        elif s == 'V' and SD[1] == 'X':
            return False
        elif s == 'V' and SD[1] == 'I':
            dec_num += dec_dict['V']
            SD = SD[1:]
    if SD:
        dec_num += dec_dict[SD[0]] 
    print(dec_num)
    return True       
    
        
S = input()
print(is_roman(S))