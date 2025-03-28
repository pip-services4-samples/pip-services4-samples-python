# -*- coding: utf-8 -*-
import sys
import traceback
import os

# add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from src.containers.BeaconsProcess import BeaconsProcess

if __name__ == '__main__':
    proc = BeaconsProcess()
    proc._config_path = "./config/config.yml"
    try:
        proc.run()
    except Exception as ex:
        print(traceback.format_exc())
        sys.stderr.write(str(ex) + '\n')