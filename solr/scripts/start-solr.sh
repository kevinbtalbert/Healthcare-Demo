#!/bin/bash -x
# CDSW_APP_PORT will be used for a deployed CML Application.
# So, we default to CDSW_APP_PORT. If it is not set and no 
# port is provided, use 8983

SOLR_VER="9.3.0"
JAVA_VER="11.0.1"

cd $(dirname $(readlink -f $0))
source ./set_solr_env.sh

SOLR_PORT=${1:-${CDSW_APP_PORT:-8983}}
echo CDSW_APP_PORT=$CDSW_APP_PORT
echo SOLR_PORT=$SOLR_PORT


/home/cdsw/solr-app/solr-${SOLR_VER}/bin/solr start -c -p ${SOLR_PORT} 
