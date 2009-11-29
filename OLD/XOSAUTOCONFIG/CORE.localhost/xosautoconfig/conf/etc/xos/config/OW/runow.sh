#!/bin/sh


## You need the right library for running OWBridge, including the one with the class itself. This means that a valid path with OWBridge in -cp option
## should be provided. Basically this path could be the srds.jar package.
## SRDS=/home/carlini/gforge/SRDS

if [ -d $SRDS ];
   then
   #can't read env variable!!!! write absolute path
   #java -version;
   java -Djava.util.logging.config.file=owlogging.properties -cp $SRDS/lib/*:$SRDS/srds.jar eu.xtreemos.ads.dht.ow.OWBridge;
else
   echo "$SRDS not found" ;
fi
