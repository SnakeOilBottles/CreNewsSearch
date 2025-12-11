#!/bin/sh
pip3 install ../CreNewsSearch/
python -m unittest
pip3 uninstall -y CreNewsSearch
pip3 install CreNewsSearch
