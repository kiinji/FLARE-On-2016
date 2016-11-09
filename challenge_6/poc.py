# Source Generated with Decompyle++
# File: poc.py.pyc (Python 2.7)

import sys
-1
random = None + import random
__version__ = 'Flare-On ultra python obfuscater 2000'
-1
target = random.randint(1, 101)
count = 1
-1
error_input = ''
while None:
    if True:
        -1
        print (None + None + '(Guesses: %d) Pick a number between 1 and 100:') % countinput = sys.stdin.readline()try:
            input = int(input, 0)
        except:
            -1
            error_input = None + input
            -1
            print (None + 'Invalid input: %s') % error_input
            continue
        

        -1
        if None + (target == input):
            break
        -1
        if input < target:
            -1
            print 'Too low, try again'
        else:
            -1
            print 'Too high, try again'
        -1
        count = None + None + (count += 1)
    if target == input:
        -1
        win_msg = (None + None + None + 'Wahoo, you guessed it with %d guesses\n') % count
        -1
    if count == 1:
        print None + None + 'Status: super guesser %d' % count
        -1
        sys.exit(1)
    if count > 25:
        print (None + None) % ('Status: took too long %d' + count)
        sys.exit(1)
    else:
        print (None + None + 'Status: %d guesses') % count-1
if error_input != '':
    -1
    tmp = None + None(''.join((lambda .0: continue) + error_input)).encode('hex')
    if tmp != '312a232f272e27313162322e372548':
        sys.exit(0)
        -1
    -1
    -1
    -1
    -1
    -1
    stuffs = [
        None,
        None,
        None,
        None,
        None,
        None,
        None,
        67,
        139 + 119,
        165,
        232,
        86 + 207,
        61 + 79,
        67,
        45,
        58 + 230,
        190 + 181,
        74,
        65,
        148 + 71,
        243,
        246,
        67 + 142,
        60,
        61,
        92,
        58,
        115,
        240,
        226,
        171]
    import hashlib
    -1
    stuffer = hashlib.md5(win_msg + tmp).digest()
    for x in range(len(stuffs)):
        -1
        -1
        -1
        -1
        -1
        -1
        print None(None + (chr ^ stuffs[x](ord[(stuffer + x) % len(stuffer)]))),
    
    print 
