#! python3
# -*- coding:utf-8
import logging, traceback, os.path

def loggingSetting(path):    
    __lvList = { "DEBUG":logging.DEBUG,
                 "INFO": logging.INFO,
                 "WARN": logging.WARN,
                 "ERROR": logging.ERROR,
                 "CRITICAL": logging.CRITICAL,
                 "FATAL": logging.FATAL }
    
    #default setting
    def_fn = "./logging.log"
    def_l = logging.INFO
    def_fm = "%(asctime)s - %(levelname)s - %(message)s"
    
    try:
        if os.path.isfile(path):
            fn = None
            l = None
            fm = None            
            logEnv = open(path, "r")
            
            for line in logEnv.readlines():
                if line.startswith("filename"):
                    fn = line.split("=")[1].rstrip("\n")
                if line.startswith("level"):
                    l = line.split("=")[1].rstrip("\n")
                    l = __lvList.get(l, def_l)
                if line.startswith("format"):
                    fm = line.split("=")[1].rstrip("\n")
                        
            #last setting
            logging.basicConfig(filename=fn, level=l, format=fm)
            
        else:
            raise FileNotFoundError(path + " is not nothing.")
    except (KeyError, Exception) as ex:
        errMsg = "Error has occured!! not reading logging env file." + "\n" + "logfileName...:" + def_fn + traceback.format_exc()
        logging.basicConfig(filename=def_fn, level=def_l, format=def_fm)
        logging.error(errMsg)
        print(errMsg)
    finally:
        pass
        
