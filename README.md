# HIMSS Conference Demo 2024
**Demonstration of LLMs for Healthcare Providers using Cloudera Machine Learning**

:wave:

Begin by launching AMP in CML to deploy CML related components and spin up components 3 and 4 of Demo. Download the Nifi template from step 1 and deploy in CDF/Nifi. Setup the elements of step 2 to spec below in CDW/Data Viz.


### 1. Ingest/Process HL7 Data Using Nifi/CDF

Download/Deploy in CDF/Nifi: [hl7 demo](/1_nifi_cfm_assets/hl7-demo.json)

### 2. Warehouse/Store HL7 Data in CDW / Generate Dashboard


### 3. Use Solr/Banana to show indexing patient conditions from logged HL7 data 

#### Solr component

Browse to https://[CML APPLICATION]/solr to Solr homepage and add a collection **hl7**


#### Banana UI component

Accessing the SOLR collection from BANANA: Go to  https://[CML APPLICATION]/solr/banana/src/index.html#/dashboard

Click on New icon and select Non time-series dashboard

Give any of the existing Collection Name of SOLR, in Collection area as shown in below screen for example, “<<collection name>>” then
Click on Create button in green. It will load the Optimzer collection data in Banana UI as shown below

### 4. Generative AI for Patient Advising by Physician


## Final AMP Setup (Manual)

1. Setup Solr app instance for unauthenticated app access

2. Execute Solr Setup Scripts (can be done in session) - Create collection, generate data, add data, add stopwords, make dashboard
    Run script: 4_solr/execute-solr-scripts.py

3. Navigate to https://[CML APPLICATION]/solr/banana/src/index.html#/dashboard to view Banana UI