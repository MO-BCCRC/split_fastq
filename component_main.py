'''

Created on May 12, 2014

@author: dgrewal

component for titan pipeline
filter positions from input file that aren't in dbsnp file.
'''
from kronos.utils import ComponentAbstract
import os


class Component(ComponentAbstract):
    
    def __init__(self,component_name='split_fastq', component_parent_dir=None, seed_dir=None):
        self.version = '1.1.3'
        ## initialize ComponentAbstract 
        super(Component, self).__init__(component_name, component_parent_dir, seed_dir)
    
    def focus(self,cmd,cmd_args,chunk):
        cmd_args = cmd_args + ['--range '+ str(chunk) ]
        return cmd,cmd_args
        
    def make_cmd(self,chunk=None):
        path = os.path.join(self.seed_dir, 'split_fastq.py')
        cmd = self.requirements['python'] +' '+ path
                      
        cmd_args = ['--input '+self.args.input,
                    '--output '+self.args.output]
        
        if self.args.range:
            cmd_args.append('--range '+self.args.range)	
        elif chunk is not None:
            cmd, cmd_args = self.focus(cmd, cmd_args, chunk)
        else:
            raise Exception('--range is required')
       
        return cmd, cmd_args

    def test(self):
        import component_test
        component_test.run()
                    
def _main():
    comp = Component()
    comp.args = component_ui.args
    comp.run()
    comp.test()
    
    
if __name__ == '__main__':
    import component_ui
    _main()
