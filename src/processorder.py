import os;
import logging;
'''
This function reads the order information from the product.csv file and update the information about the department in dept (hashmap). It uses the productmap to look up the respective department of each product.
Both the operations, looking up the department id of the product and updating the information in dept is O(1) order. If the product id does not exist in the productmap, it prints a warning about it and continues to process the remaining orders. It returns the department info as the hashmap data structure to the main purchase_analytics. 
'''

def process_departmentinfo(filepath, productmap):
    dept={};
    #print ("filepath: %s" %(filepath))
    try:
        if not os.path.isfile(filepath):
            logging.error("File path {} does not exist. Exiting...".format(filepath))
            sys.exit()
        
        with open(filepath) as fp:
            cnt = 0
            logging.debug("Reading order info")
            for line in fp:
                line=line.rstrip();
                word=line.split(',')
                cnt=cnt+1;
                if (cnt>1):
                    val=[0,0,0.0];
                    pid=int(word[1])
                    #print ("pid : %d" %(pid))
                    #print("pdmap: %d" %(productmap[pid]))
                    if(~pid in productmap):
                        print ( "Pid %d does not exist in productmap" % (pid))
                        logging.warning("Pid %d does not exist in productmap" % (pid))
                    if(productmap[pid] in dept):
                        val=dept[productmap[pid]];
                    val=[val[0]+1, val[1]+1-int(word[3]),0.0]
                    val[2]=float(float(val[1])/float(val[0]))
                    dept[productmap[pid]]=val;
                    #print(val)
                
    except:
        logging.error("Exception occured in reading file")
    print(list(dept))    
    return dept;

