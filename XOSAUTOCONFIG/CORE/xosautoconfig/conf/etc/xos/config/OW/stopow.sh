#!/bin/bash

ow=Bridge

pid=`ps -A -o pid,cmd | grep $ow | grep -v grep | awk '{print $1}'`

if [ $pid > 0 ]
then
  kill -9 $pid
fi


