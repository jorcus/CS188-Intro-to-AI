#!/usr/bin/env python
__author__ = "Ng Fang Kiang / Jorcus"
__copyright__ = "Copyright 2017"
__credits__ = ["Ng Fang Kiang / Jorcus"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Ng Fang Kiang / Jorcus"
__email__ = "jorcus96@gmail.com"
__status__ = "Production"



import os
import errno
import shutil

arr_py = [x for x in os.listdir() if x.endswith(".py")]
if arr_py:
    print(arr_py)
    for each_py in arr_py:
        terminal_cmd = '2to3 -w '+each_py
        print(terminal_cmd)
        os.system(terminal_cmd)

backup_py = [x for x in os.listdir() if x.endswith(".py.bak")]
backup_dir = "backup_code"

if backup_py:
    print(backup_py)
    if not os.path.exists(os.path.dirname(backup_dir)):
        try:
            os.mkdir(backup_dir)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    for each_py in backup_py:
        shutil.move(each_py, backup_dir)



