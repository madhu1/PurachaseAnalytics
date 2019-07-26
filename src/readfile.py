import os;
import logging;
'''
This function creates a productmap which is hashmap of product_id (key): dept_id(value). 
Allows easy and fast lookup. 
Returns the productmap.
'''

def readproductinfo(filepath):
    productmap={};
    try:
        if not os.path.isfile(filepath):
            print("File path {} does not exist. Exiting...".format(filepath))
            logging.error("File path {} does not exist. Exiting...".format(filepath))
            sys.exit()
     
        with open(filepath) as fp:
            cnt = 0
            for line in fp:
                #print("line {} contents {}".format(cnt, line))
                line=line.rstrip()
                word =line.split(',')
                #print("key : {} val: {}".format(word[0],word[3]))
                if(cnt>0):
                    productmap[int(word[0])]=int(word[3])
                cnt+=1
    

    except Exception as e:
        logging.error("Error occured in reading  file %s" %(filepath))
    finally:
        fp.close();
        

    #print (list(productmap))
    #print(list(productmap.values()))
    return productmap;


