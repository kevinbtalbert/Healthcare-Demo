#!/usr/bin/bash


source /home/cdsw/solr/scripts/set_solr_env.sh

JAVA_TGZ=openjdk-${JAVA_VER}_linux-x64_bin.tar.gz
JAVA_DL_URL="https://download.java.net/java/GA/jdk11/13/GPL/${JAVA_TGZ}"

SOLR_TGZ="solr-${SOLR_VER}.tgz"
SOLR_DL_URL="https://www.apache.org/dyn/closer.lua/solr/solr/${SOLR_VER}/${SOLR_TGZ}?action=download"

BANANA_GIT="https://github.com/lucidworks/banana.git"

mkdir solr-app 2>/dev/null
cd solr-app

## Install Java ##
wget --no-verbose -O ${JAVA_TGZ} ${JAVA_DL_URL}
tar xzf ${JAVA_TGZ} && rm ${JAVA_TGZ}


## Install Solr ##
wget --no-verbose -O ${SOLR_TGZ} ${SOLR_DL_URL}
tar xzf ${SOLR_TGZ} && rm solr-${SOLR_VER}.tgz

## Install Banana ##
cd solr-${SOLR_VER}
cd server
cd solr-webapp
cd webapp
git clone ${BANANA_GIT}