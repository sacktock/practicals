import os.path


def q1():
    sentence = input('sentence? ')

    lst = sentence.split(' ')

    return '{}'.format(len(sentence.replace(' ',''))/len(lst))


def vowel_count():
    string = input('string? ').lower()
    ords=[97,101,105,111,117]
    x=0
    for s in string:
        num = ord(s)
        if num in ords:
            x+=1
    return x
        
    
                                                                                                        
def rotate(v):
    string = input('string? ')
    output = ''

    for i in range(0,len(string)):
        num = ord(string[i])
        if num == 122:
            num = 96
        output = output + chr(num+1)
    return output 


def hyperlinks():
    filename = input('filename? ')
    
    if filename[-5:] == '.html' or filename[-4:] == '.htm':
        if os.path.isfile(filename):
            infile = open(filename)
            s = infile.read()
            infile.close()

            x=s.count('<a ')
            y=s.count('<\a>')
            if y==x:
                return x
    return False
        
def distribution():
    output = ''
    filename = input('filename? ')
    if filename[-4:].strip() == '.txt':
        if os.path.isfile(filename):
            infile = open(filename)
            string = infile.readline()
            infile.close()            
            lst = string.split(' ')
            for l in lst:
                if l != ' ':
                    output = output+ "{} ".format(string.count(l)) + l+"'s, "
                    for i in range(0,len(lst)):
                        if str(lst[i]) == str(l):
                            lst[i] = ' '
                        

    return output


def censor():
    s=''
    filename = input('filename? ')
    if filename[-4:].strip() == '.txt':
        if os.path.isfile(filename):
            infile = open(filename)
            s = infile.read()
            infile.close()

            lst = s.split(' ')

            for l in lst:
                if len(l) ==4:
                    s=s.replace(l,'XXXX')

            outfile = open(filename,'w')
            outfile.write(s)
            outfile.close()

        return('done')

            
    



            
