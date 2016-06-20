#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Parama_Fadli_Kurnia"
__date__ = "$May 26, 2016 11:28:43 AM$"

from subprocess import call

# clear cache memory
call("free && sync && echo 3 > /proc/sys/vm/drop_caches && free", shell=True)
