#! /usr/bin/python

# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "Parama_Fadli_Kurnia"
__date__ = "$May 25, 2016 11:23:32 AM$"

from subprocess import call

# restart mysql service
call("sudo service mysql restart", shell=True)

# restart lampp service
call("/opt/lampp/lampp restart", shell=True)
