import sys;
import os;
import logging;
from readfile import readproductinfo; 
from writefile import writedeptinfo;
from processorder  import process_departmentinfo;


'''
This program is main code which initiate the analytics process
'''

'''
Part 1: set debug level and  log the inputs and outputs
'''
logging.basicConfig(level=logging.DEBUG)
logging.debug('Purchase Analytics --')
logging.debug("Number of arguments:%s" %(len(sys.argv)))
logging.debug( "Argument List: %s"%( str(sys.argv)))

'''
Part 2: Create a hashmap of productid (key): dept_id (value) using function readproductinfo ;
'''
filepath = sys.argv[2]
productmap=readproductinfo(filepath);
logging.debug (list(productmap))
logging.debug(list(productmap.values()))

'''
Part 3: Read the incoming orders to create a cummulative summary of orders for each department. Use the productmap to map the productid to the dept_id and update deptinfo hashmap.
Sort the hashmap based on dept_id and write it to reports file
'''

filepath=sys.argv[1]
deptinfo=process_departmentinfo(filepath,productmap)
logging.debug(list(deptinfo))
writedeptinfo(deptinfo, sys.argv[3])

