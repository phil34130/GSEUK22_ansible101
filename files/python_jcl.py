#!/bin/env python                             
import platform                               
print("machine",platform.machine())           
print("platform",platform.platform())         
print("arch ",platform.architecture())        
print("process ",platform.processor())        
print("compiler",platform.python_compiler())  
print("system ",platform.system())                                                      
from zoautil_py import jobs                    
from zoautil_py import mvscmd, datasets        
print(jobs.fetch_multiple())  