This is a set of scripts designed to run in CML/CDSW and is a work in progress.
Pay attention to values set in set_solr_env.sh.
If $CDSW_APP_PORT is set, that port will be used. Otherwise it will default
to Solr's default 8983.


STEP #1 
   Run 01_install-java11_n_solr.py

   This will download java11 and solr 9.3.0 into scripts/solr-app

STEP #2
   Run Solr by either:
   1) create an application in CML and use start-solr-application.py to start it.
   
   2) within a session, run 02_start-solr-application.py 
      or run solr/scripts/start-solr.sh
       
STEP #3   
   Stop Solr in a session:
   03_stop-solr.py (or run the shell script)

NOTES:
The script set_solr_env.sh and change it as needed.
There is a sample solr_config with several vector fields for testing.


# ----- TODO ---- 
  -> Upload a configset
  -> Create collection

