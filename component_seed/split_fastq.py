'''
Created on Aug 28, 2014

@author: dgrewal
'''
import gzip
import argparse
import shutil

version = '1.0.4'

parser = argparse.ArgumentParser()

parser.add_argument('--input',  
                    required=True, 
                    help='the input bam file')
parser.add_argument('--range',
                    required = True,
                    help = 'the beginning and end of offset from the beginning')
parser.add_argument('--output',
                    required = True,
                    help = 'the output')
args = parser.parse_args()

class splitFastq(object):
    def __init__(self):
        self.args = args

    def get_file_linecount(self):
        def blocks(files, size=65536):
            while True:
                b = files.read(size)
                if not b: break
                yield b

        if self.__is_gzip(self.args.input):
            input_stream = gzip.open(self.args.input, 'rb')
        else:
            input_stream = open(self.args.input)

        return sum(bl.count("\n") for bl in blocks(input_stream))

    def __is_gzip(self, filename):
        if filename.split('.')[-1] == 'gz':
            return True
        return False
    
    def split(self):
        if not self.args.range:
            print 'No splitting done since no range specified'
            shutil.copy(self.args.input, self.args.output)
            return
        
        if self.__is_gzip(self.args.input):
            input_stream = gzip.open(self.args.input, 'rb')
        else:
            input_stream = open(self.args.input)
        output_stream = open(self.args.output,'w')

        num_lines = self.get_file_linecount()
        print 'number of lines:'+str(num_lines)

        try:
            self.args.range = self.args.range.split(':')
            num_splits = int(self.args.range[1])
            chunk = int(self.args.range[0])

            #split file into num_splits equal chunks ( the remaining reads go to  last chunk)
            split_size = num_lines/num_splits

            if not split_size%4 == 0:
                split_size -= split_size%4

            begin = (chunk-1) * split_size
            end = (chunk * split_size)-1
            if chunk == num_splits:
                end = num_lines-1
        except ValueError as e:
            raise Exception( 'Please ensure that the range provided 2 integers separated by ":"' )
        except Exception,e:
            raise e
            
        if (end+1)%4 != 0:
            raise Exception( 'the end of the interval removes a part of the read')
        
        print 'Printing lines %s-%s to output' %(str(begin), str(end))    
        for i,line in enumerate(input_stream):
            if i < begin:
                continue
            if i > end:
                return
            output_stream.write(line)

        #for val in lines:
         #   output_stream.write(val)
        
        output_stream.close()
        input_stream.close()            
            
if __name__ == '__main__':
    split = splitFastq()
    split.split()
