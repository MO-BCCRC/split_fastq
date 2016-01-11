'''

@author: dgrewal
'''

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--input',  
                    required=True, 
                    help='the input bam file')
parser.add_argument('--range',
                    default = None,
                    help = 'the beginning and end of offset from the beginning')
parser.add_argument('--output',
                    required = True,
                    help = 'the output')
args, unknown = parser.parse_known_args()
