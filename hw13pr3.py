# coding: utf-8
#
# the top line, above, is important --
# it ensures that Python will be able to use this file,
# even if you paste in text with Unicode characters
# (beyond ASCII)
# for an more expansive example of such a file, see
#    http://www.cl.cam.ac.uk/~mgk25/ucs/examples/UTF-8-demo.txt
#
# OK! Now we're ready for hw13pr3.py ...
#
#
# Name: Peter Morales
#
#

import random 


def vc(filename):

    f = open(filename, encoding = 'latin1')
    text = f.read()
    f.close()

    LoW = text.split()    
    print("There are", len(LoW), "words.")

    pw = '$'

    d = {}
    for nw in LoW:
        if pw not in d:
            d[pw] = [nw]
        else:
            d[pw] += [nw]
        
        pw = nw
    
        if pw[-1] in '.!,?':
            pw = '$'
            
    print("There are", len(d), "*distinct* words.\n")
    return d 

# function #1
#
def createDictionary(filename):
    d = vc(filename)
    return d

# function #2
#
d = createDictionary('shakespeare.txt')

def generateText(d, N):
    strList = []
    ctr = 0
    j = 0
    value = []
    while ctr < N:
        if ctr == 0:
            word = random.choice(d['$'])
            strList = strList + [word]
            ctr += 1
        elif ctr >= 1:
            value = random.choice(d[strList[j]])
            strList = strList + [value]
            if value[-1] in '.!,?':                    
                strList = strList + [random.choice(d['$'])]
                ctr+=1
                j+=1
                
            ctr += 1
            j+=1

        outPut = ' '.join(strList)
    return outPut



#
# Your 500-or-so-word CS essay (paste into these triple-quoted strings below):
#
"""
#3
"Die single and she in thy husbandry? Die single and thine image dies with thee. Whose fresh repair if now thou viewest, Whose fresh repair if thou through windows of thine age shalt see, 
unbless some mother. But if now thou live remembered not to stop posterity? Thou art thy glass and she so fond will be the time that face thou not to stop posterity? Despite of wrinkles 
this thy mother's glass and tell the lovely April of thy husbandry? Look in thee Calls back the tillage of her prime, Whose fresh repair if now thou not to be, Die single and thine image 
dies with thee. Die single and thine image dies with thee. For where is the lovely April of wrinkles this thy glass and she so fair whose uneared womb Disdains the world, Die single and 
thine age shalt see, Whose fresh repair if thou through windows of wrinkles this thy husbandry? Thou dost beguile the face should form another, Whose fresh repair if now thou live remembered 
not renewest, Look in thee Calls back the lovely April of her prime, Of his self-love to stop posterity? So thou through windows of thy golden time. Thou dost beguile the world, Die single 
and she so fond will be the tillage of thy mother's glass and tell the face should form another, unbless some mother. Whose fresh repair if thou through windows of her prime, unbless some 
mother. But if now thou through windows of her prime, So thou not to be, Thou art thy glass and thine age shalt see, Now is he so fond will be the tillage of wrinkles this thy glass and 
tell the lovely April of thy mother's glass and she in thee Calls back the face should form another, Despite of her prime, Or who is he so fair whose uneared womb Disdains the lovely April 
of wrinkles this thy golden time. Despite of thy golden time. Or who is she so fair whose uneared womb Disdains the lovely April of her prime, Or who is the lovely April of wrinkles this 
thy mother's glass and tell the lovely April of her prime, Thou dost beguile the world, Despite of her prime, Die single and tell the face thou not to be, Despite of thine age shalt see, 
unbless some mother. But if now thou through windows of wrinkles this thy golden time. Thou dost beguile the time that face should form another, Of his self-love to be, Whose fresh repair 
if thou not to stop posterity? Thou dost beguile the world, Whose fresh repair if thou not to stop posterity? Thou dost beguile the face thou through windows of thy glass and thine age shalt 
see, Now is she in thee Calls back the tillage of thy husbandry? Whose fresh repair if now thou viewest, Of his self-love to stop posterity? Of his self-love to be, So thou not renewest, For 
where is the face should form another, Or who"

"""
#
#