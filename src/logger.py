import logging
import os
from datetime import datetime

file= f"{datetime.now().strftime('%D_%Y_%H_%M_%S')}.log"  #file = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
path=os.path.join(os.getcwd(),"logs",file)
os.makedirs(path,exist_ok=True)
log_path=os.path.join(path,file)

logging.basicConfig(filename=log_path,level=logging.INFO,
                    format='%(asctime)s %(name)s %(levelname)s %(message)s')