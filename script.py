from os import system
import scr
import subprocess
import urllib
from urllib import request

def nothing():
    pass

def file_size(src_file):
    return len(open(src_file).readlines())

def try_urlopen(link):
    try:
        urllib.request.urlopen(link)
        return True
    except Exception as ex:
        nothing()
    return False

def network_connection_check(link):
    if not link.startswith('http'):
        for prefix in ['https://', 'http://']:
            if try_urlopen(prefix+link):
                return prefix+link
        return link
    else:
        return link

def main_script(src_file):
    size = file_size(src_file)
    system('chcp 65001') 

    f = open(src_file)
    for i in range (size):
        line = f.readline()
        link = line.rstrip('\n')
        #output = subprocess.check_output(['tracert', link]) #работает криво, исправлю
        #print(str(output)) #работает криво, исправлю
        newlink = network_connection_check(link)
        scr.scr_f(newlink)
    f.close()
    return line