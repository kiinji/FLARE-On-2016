import sys
import os
import numpy

charswap_func_table = [
    'func_counter_plus_2',
    'func_counter_plus_1',
    'func_counter_plus_1_1',
    'func_counter_plus_1_2',
    'func_counter_plus_1_3',
    'func_counter_plus_1_4',
    'func_counter_plus_1_5',
    'func_counter_plus_1_6',
    'func_counter_plus_1_7',
    'func_counter_plus_1_8',
    'func_counter_arg_eof',
    'func_counter_plus_2_wswitch',
    'func_counter_plus_2_wswitch_1',
    'func_counter_plus_1_9'
]

another_cipher = open('another_cipher', 'rb').read()
another_cipher = another_cipher[:0x182 * 2]

# key = []
    
# for char in arg_key:
    # key.append(ord(char))
    # key.append(0)
    
# key += [0,0,0,0,0,0,0,0,0]

# func_counter    = 0
# global_counter  = 9
# _some_result  = 0
# _what  = 0

# key_validation()

def key_validation():
    global func_counter
    global another_cipher
    global charswap_func_table
    
    while func_counter < 0x182:
        char = another_cipher[func_counter * 2]

        if (char > 0xf):
            exit()
        
        func = charswap_func_table[char] + '()'

        eval(func)
        
def set_argchar_at_g_counter(char):
    global global_counter
    global key
    global func_counter
    
    global_counter += 1
    
    index = global_counter * 2
    
    if char > 0xff:
        lower = 0
        higher = 0
        
        lower = '0x' + hex(char)[-2:]
        lower = numpy.uint8(int(lower, 16))
        
        if len(hex(char)) < 6:
            higher = numpy.uint8(int(hex(char)[:3], 16))
            
        else:        
            higher = numpy.uint8(int(hex(char)[:4], 16))

        key[index] = lower
        key[index + 1] = higher

    else:
        key[index] = char
        key[index + 1] = 0x00
    
def get_char_at_g_counter():
    global key
    global global_counter
	
    index = global_counter * 2

    char_1 = numpy.uint8(key[index])
    char_2 = numpy.uint8(key[index + 1])
    
    result_char = int.from_bytes([char_1, char_2], byteorder='little', signed=False)
    
    global_counter -= 1
    
    return result_char
    
def func_counter_plus_2():
    global func_counter
    global another_cipher

    func_counter += 1

    index = func_counter * 2

    char_1 = another_cipher[index]
    char_2 = another_cipher[index + 1]

    char = int.from_bytes([char_1, char_2], byteorder='little', signed=False)

    set_argchar_at_g_counter(char)

    func_counter += 1
	
def func_counter_plus_1():
	global func_counter
	
	func_counter += 1
	get_char_at_g_counter()
	
def func_counter_plus_1_1():
	global func_counter
	
	char_1 = get_char_at_g_counter()
	char_2 = get_char_at_g_counter()
	
	sum = char_1 + char_2
	
	set_argchar_at_g_counter(sum)
	
	func_counter += 1
	
def func_counter_plus_1_2():
	global func_counter
	
	char_1 = get_char_at_g_counter()
	char_2 = get_char_at_g_counter()
	
	sub = char_2 - char_1
	
	set_argchar_at_g_counter(sub)
	
	func_counter += 1

def func_counter_plus_1_3():
    global func_counter
    
    char_1 = get_char_at_g_counter() # var_8
    char_2 = get_char_at_g_counter() # var_4
    
    sar = char_2 >> char_1
    
    sub = 0x10 - char_1 
    
    shl = char_2 << sub
    
    _or  = sar | shl
    _and = _or & 0xFFFF

    set_argchar_at_g_counter(_and)
    
    func_counter += 1

def func_counter_plus_1_4():
    global func_counter
    
    char_1 = get_char_at_g_counter() # var_8
    char_2 = get_char_at_g_counter() # var_4
    
    shl = char_2 << char_1
    
    sub = 0x10 - char_1
    
    sar = char_2 >> sub
    
    _or  = shl | sar
    _and = _or & 0xFFFF
    
    set_argchar_at_g_counter(_and)
    
    func_counter += 1
    
def func_counter_plus_1_5():
    global func_counter
    
    char_1 = get_char_at_g_counter() # var_4
    char_2 = get_char_at_g_counter() # var_8
    
    xor = char_1 ^ char_2
    
    set_argchar_at_g_counter(xor)
    
    func_counter += 1
    
def func_counter_plus_1_6():
    global func_counter
    
    char = get_char_at_g_counter()
    
    _not = ~char
    _and = _not & 0xFFFF
    
    set_argchar_at_g_counter(_and)
    
    func_counter += 1
    
def func_counter_plus_1_7():
    global func_counter
    
    char_1 = get_char_at_g_counter() # var_4
    char_2 = get_char_at_g_counter() # var_8
    
    result = 0x0
    
    if char_1 == char_2:
        result = 0x1
    
    set_argchar_at_g_counter(result)
    
    func_counter += 1
    
def func_counter_plus_1_8():
    global func_counter
    
    char_1 = get_char_at_g_counter() # var_8
    char_2 = get_char_at_g_counter() # var_c
    char_3 = get_char_at_g_counter() # var_4
    
    if char_3 == 0x1:
        set_argchar_at_g_counter(char_1)
    else:
        set_argchar_at_g_counter(char_2)
        
    func_counter += 1
    
def func_counter_arg_eof():
    global func_counter
    
    char = get_char_at_g_counter()
        
    func_counter = char
    
def func_counter_plus_2_wswitch():
    global func_counter
    global another_cipher
    global _what
    global _some_result
    global global_counter
    
    func_counter += 1
    
    char = another_cipher[func_counter * 2]
    
    if char <= 0x3:
        to_be_set = 0
        
        if char == 0x0:
            to_be_set = _some_result
        elif char == 0x1:
            to_be_set = _what
        elif char == 0x2:
            to_be_set = global_counter
        elif char == 0x3:
            to_be_set = func_counter
            
        set_argchar_at_g_counter(to_be_set)
        
    func_counter += 1
    
def func_counter_plus_2_wswitch_1():
    global func_counter
    global another_cipher
    global _what
    global _some_result
    global global_counter
    
    func_counter += 1
    
    char = another_cipher[func_counter * 2]
    
    if char <= 0x3:
        to_be_set = get_char_at_g_counter()
        
        if char == 0x0:
            _some_result = to_be_set       
        elif char == 0x1:
            _what = to_be_set
        elif char == 0x2:
            global_counter = to_be_set
        elif char == 0x3:
            func_counter = to_be_set
        
    func_counter += 1
        
def func_counter_plus_1_9():
    global func_counter
    
    func_counter += 1