#!/usr/bin/env python
#
#       setup.py for cputemp
#       
#       Copyright 2008, 2009, 2010, 2012 Scott Williams <vwbusguy@fedoraproject.org>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
#
#	Full License details are in the accompanying release notes.

import os,sys,getopt

user = os.geteuid()
verbose = 0
binprefix = ""
logpath = "/var/log/"
usage = 0

if user != 0 :
	print "You must be root to install this program.  Try logging is as root (su -) or using sudo.\n"
	sys.exit()

if os.path.exists ('./CPUTemp.py') == False :
	print "CPUTemp.py not found.  It must be in the same folder as this installer.  Cannot continue\n"
	sys.exit() 

try:
	opts, args = getopt.getopt(sys.argv[1:], "vh", ["verbose","binprefix=","logpath=","help"])
	for opt, arg in opts:
		if opt in ("-v","--verbose"):
			verbose = 1
		if opt in ("--binprefix"):
			binprefix = arg
		if opt in ("--logpath"):
			logpath = arg
		if opt in ("-h","--help"):
			usage = 1
except getopt.GetoptError:
	verbose = 0
	binprefix = ""
	logpath = "/var/log"
	usage = 0

if usage == 1:
	print "cputemp installation options:\n"
	print "-v/--verbose			Verbose (not currently used)"
	print "-h/--help			Display this usage info"
	print "--binprefix			Specify bin prefix (ie: /usr or /local)\n"
	sys.exit()

print "Installing cputemp:"
print "Copying program to " + binprefix + "/bin:  " ,
os.system('chmod a+x ./CPUTemp.py')
os.system('cp ./CPUTemp.py ' + binprefix + '/bin/cputemp')
print "Done."

print "Checking if log exists:  " ,
while os.path.exists (logpath + "/cputemp.log") == True :
	open (logpath + "/cputemp.log", 'r+' ).write("cputemp log    \n\n")
	print "Yes"
	break
while os.path.exists (logpath + '/cputemp.log') == False:
	print "No\n   ***Creating Log:  " ,
	open (logpath + "/cputemp.log", 'w' ).write("cputemp log    \n\n")
	os.system('chmod 666 ' + logpath + '/cputemp.log')
	print "Done."

print "Installation finished.  Type cputemp as any user to run."
sys.exit()
