#!/usr/bin/env python

import cloud
import os
cloud.setkey(os.environ['PICLOUD_KEY'], os.environ['PICLOUD_SECRET'])

def sys(cmd) :
  from subprocess import Popen, PIPE

  return Popen(cmd, stdout=PIPE, shell=True).communicate()[0]

def cloudsys(cmd) :
  print cloud.result(cloud.call(sys, cmd)),

from sys import argv
if len(argv) > 1 :
  cloudsys(' '.join(argv[1:]))
  exit()

from sys import stdin
while True :
  print "$ ",
  line = stdin.readline()
  cloudsys(line)
