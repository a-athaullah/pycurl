#! /usr/bin/env python
# -*- coding: iso-8859-1 -*-
# vi:ts=4:et
# $Id: setup_win32_ssl.py,v 1.22 2004/10/15 08:56:22 kjetilja Exp $

import os, sys, string
assert sys.platform == "win32", "Only for building on Win32 with SSL and zlib"


CURL_DIR = r"c:\src\build\pycurl\curl-7.12.2-ssl"
OPENSSL_DIR = r"c:\src\build\pycurl\openssl-0.9.7d"
sys.argv.insert(1, "--curl-dir=" + CURL_DIR)

from setup import *

setup_args["name"] = "pycurl-ssl"


for l in ("libeay32.lib", "ssleay32.lib",):
    ext.extra_objects.append(os.path.join(OPENSSL_DIR, "out32", l))
ext.extra_objects.append(r"c:\src\pool\zlib-1.2.1.1\pool\win32\vc6\zlib.lib")
ext.extra_objects.append(r"c:\src\build\pycurl\c-ares-1.2.0\ares.lib")
ext.extra_objects.append(r"c:\src\pool\libidn-0.5.4\pool\win32\vc6\idn.lib")


if __name__ == "__main__":
    for o in ext.extra_objects:
        assert os.path.isfile(o), o
    apply(setup, (), setup_args)

