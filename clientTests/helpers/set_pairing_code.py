import sys
import os
import re
from pair_steps import *
ROOT_ADDRESS = os.environ['PAIRFILEPATH']
CONSTANTS_FILE = './clientTests/constants.h'

def write_pairing_code_to_constants_h():
    code = read_file("%s/paircode.txt" % ROOT_ADDRESS)
    if len(code) < 1:
        print('code looks wrong...exiting')
        return
    file_string = read_file(CONSTANTS_FILE)
    repl = re.sub(r'@".*"', "@\"%s\"" % code, file_string)
    write_code_to_file(repl, CONSTANTS_FILE)

def read_file(fname):
    code = ''
    with open(fname, 'r') as content_file:
        code = content_file.read()
    return code.strip()

get_claim_code_from_server()
write_pairing_code_to_constants_h()
print("done")
