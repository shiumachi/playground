#!/usr/bin/python

    

def convert_rgb(red,green,blue):
    return hex(red * 65536 + green * 256 + blue)

if __name__=='__main__':
    print convert_rgb(100,0,0)
    print convert_rgb(255,255,127)
    

    




