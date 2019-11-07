#!/usr/bin/env python3
###############################################################################
#       author:
#           Mattia Mantovani
#       date:  
#           v10_04_2019_01
#       description: 
#           make an eps-file processable with psfrag, converting 
#           glyphs to plain text
#       usage:
#           python3 unglyph.py inputEpsFile
#           python3 unglyph.py inputEpsFile [outputEpsFile]
###############################################################################

import re,sys
def main():
    if 1 < len(sys.argv) <= 3:
        def charof(s):
            res = s
            cname = s[1:].strip()
            cdic = {    'equal': '=',
                        'space': ' ',
                        'hyphen': '-', 
                        'period': '.',
                        'zero': '0',
                        'one': '1',
                        'two': '2',
                        'three': '3',
                        'four': '4',
                        'five': '5', 
                        'six': '6',
                        'seven': '7',
                        'eight': '8',
                        'nine': '9',
                        'plus': '+',
                        'minus': '-',
                        'slash': '/',
                        'comma': ',',
                        'colon': ':'
                    }
            if s[0] == '/':
                if len(cname) == 1:
                    res = cname
                else:
                    res = cdic[cname]
            else:
                print('[error]: character without trailing slash')
            return res

        epsFileStr =''
        with open(sys.argv[1], 'r') as f:
            startstr    = ''
            transstr    = ''
            rotatestr   = ''
            showstr     = ''
            lnbuff      = list()
            printBool   = True
            for line in f:
                ln = line.strip()
                
                if ln.startswith('/CharStrings'):
                    printBool = False
                elif ln.startswith('%%EndProlog'):
                    printBool = True
                
                if len(lnbuff)==2:
                    if not ln.endswith('glyphshow'):
                        epsFileStr += ''.join(lnbuff)
                    lnbuff = list()
                if len(lnbuff)==1:
                    lnbuff.append(line)
                if ln.endswith('translate'):
                    lnbuff.append(line)
                    strPart = ln.split(' ')
                    startstr = ' '.join(strPart[0:2])+' m'
                if ln.endswith('rotate'):
                    rotatestr = ln
                if ln.startswith('/Encoding'):
                    if not ln.endswith('def'):
                        print('[error]: newline in flag /Encoding - is not
                                supported')
                    epsFileStr += '/Encoding StandardEncoding def\n'
                elif ln.endswith('glyphshow'):
                    strPart = ln.split(' ')
                    if len(transstr)==0:
                        transstr = ' '.join(strPart[0:2])+' rmoveto'
                    showstr += charof(strPart[3])
                elif len(showstr)>0:
                    acclines = '\n'.join([startstr,transstr,rotatestr,
                                         '('+showstr+') show'])+'\n'
                    epsFileStr += acclines
                    epsFileStr += line
                    startstr    = ''
                    transstr    = ''
                    rotatestr   = ''
                    showstr     = ''
                    lnbuff      = list()
                elif len(lnbuff)==0 and printBool==True:
                    epsFileStr += line
        
        if len(sys.argv) == 2:
            print epsFileStr
        else:
            with open(sys.argv[2], 'w') as f:
                f.write(epsFileStr)
    else:
        print(f'[error]: {sys.argv[0]} requires one(two) argument(s)')
    
if __name__ == '__main__':
    main()







