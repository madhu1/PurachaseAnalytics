import logging;
def writedeptinfo(dept, filepath):
    try:
        f= open(filepath,"w+")
        f.write("%s\n"%("department_id,number_of_orders,number_of_first_orders,percentage"))
        logging.debug("Writing report in %s " % (filepath));
        for key in sorted(dept.keys()):
        #print("%s: %s" % (key, dept[key]))
            val=dept[key]
            f.write("%d,%d,%d,%.2f\r\n" % (key, val[0], val[1], val[2]))
    except Exception as e:
        logging.error("Error occured in writing file %s" %(filepath))
    finally:
        f.close();
