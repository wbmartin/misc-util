#!/usr/bin/python

import sys
from subprocess import call

def main():
  christmasTree(sys.argv[1])


def christmasTree(ipRange):
  call(["echo",ipRange])



if __name__ == '__main__':
  main()

