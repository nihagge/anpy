#!/usr/bin/python3

import tempfile

# with tempfile.TemporaryDirectory() as directory: 
with tempfile.TemporaryDirectory() as directory:
    print ("the created temp dir: %s" % directory)