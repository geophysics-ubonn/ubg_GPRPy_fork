#!/bin/bash
# delete and recreate the virtualenv "reda"
source /usr/share/virtualenvwrapper/virtualenvwrapper.sh

rmvirtualenv gprpy
mkvirtualenv --python /usr/bin/python3 gprpy
workon gprpy
# pip install -r requirements.txt
# pip install -r requirements_dev.txt
pip install -r doc/requirements_doc.txt
pip install ipython

pip install .
