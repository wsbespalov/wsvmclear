import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

def get_module_name():
    return os.path.abspath(__file__).split('/')[-1][:-3]
