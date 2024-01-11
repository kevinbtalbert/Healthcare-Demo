SOLR_VER="9.3.0"
JAVA_VER="11.0.1"
export SOLR_VER="9.3.0"
export JAVA_VER="11.0.1"

export SOLR_HEAP=1g     #This may not work

SOLR_PORT=${1:-${CDSW_APP_PORT:-8983}}
SOLR_URL="http://localhost:${SOLR_PORT}"
SOLR_URL=https://solr9.ml-758fd61d-88e.se-sandb.a465-9q4k.cloudera.site

COLLECTION_NAME=vectors
COLLECTION_CONF="/home/cdsw/solr/solr_configs/vectors_conf"

export JAVA_HOME="/home/cdsw/solr-app/jdk-${JAVA_VER}"
export SOLR_HOME="/home/cdsw/solr-app/solr-${SOLR_VER}"