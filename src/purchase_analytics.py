import sys;
import os;
import logging;
from readfile import readproductinfo; 
from writefile import writedeptinfo

logging.basicConfig(level=logging.ERROR)
logging.debug('Purchase Analytics --')

logging.debug("Number of arguments:%s" %(len(sys.argv)))
logging.debug( "Argument List: %s"%( str(sys.argv)))

filepath = sys.argv[2]
productmap=readproductinfo(filepath);
logging.debug (list(productmap))
logging.debug(list(productmap.values()))


filepath=sys.argv[1]
if not os.path.isfile(filepath):
    print("File path {} does not exist. Exiting...".format(filepath))
    logging.error("File path {} does not exist. Exiting...".format(filepath))
    sys.exit()



with open(filepath) as fp:
    cnt = 0
    dept={};
    logging.debug("Reading order info")
    for line in fp:
        line=line.rstrip();
        word=line.split(',')
        #logging.debug("{}: {} {} ".format(cnt, word[1], word[3]))
        if(cnt>0):
            val=[0,0,0.0];
            pid=int(word[1])
            if(~pid in productmap):
                print ( "Pid %d does not exist in productmap" % (pid))
                logging.warning("Pid %d does not exist in productmap" % (pid))
            if(productmap[pid] in dept):
                val=dept[productmap[pid]];
            val=[val[0]+1, val[1]+1-int(word[3]),0.0]
            val[2]=float(float(val[1])/float(val[0]))    
            dept[productmap[pid]]=val;                    
        cnt += 1    
        

    #for key in sorted(dept.keys()):
    #        print("%s: %s" % (key, dept[key]))
    writedeptinfo(dept, sys.argv[3])        
    #print(list(dept))
    #print(list(dept.values()))
