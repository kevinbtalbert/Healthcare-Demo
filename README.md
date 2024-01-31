# Healthcare Demo 2024 :wave:
**Demonstration of HL7 Ingest, Extraction, LLMs, and HL7 Dashboarding with Solr for Healthcare Providers using Cloudera DataFlow, Solr, and Machine Learning**


![](/assets/amp-cover.png)

Begin by launching AMP in CML to deploy CML related components and spin up components 3 and 4 of Demo. Download the Nifi template from step 1 and deploy in CDF/Nifi. Setup the elements of step 2 to spec below in CDW/Data Viz.


### 1. Ingest/Process HL7 Data Using Nifi/CDF

Download/Deploy in CDF/Nifi: [hl7 demo](/1_nifi_cfm_assets/hl7-demo.json)

![](/assets/nifi-ingest.png)

![](/assets/nifi-processing.png)

### 2. Warehouse/Store HL7 Data in CDW / Generate Dashboard

Optional component, this is a great way to show loading medical data directly into CDW and Using Data Viz for visuals.

### 3. Use Solr/Banana to show indexing patient conditions from logged HL7 data 
Note that the below 2 components require completing the Final AMP Setup (Manual) at the bottom of the Readme.

#### Solr component

Browse to https://[SOLR SERVER CML APPLICATION]/solr to Solr homepage and view the `hl7_messages` collection **hl7**

![](/assets/solr-dashboard.png)

#### Banana UI component

Accessing the SOLR collection from BANANA: Go to  `https://[SOLR SERVER CML APPLICATION]/solr/banana/src/index.html#/dashboard`

Leverage the created dashboard json file in 4_solr if not loaded automatically: `chronic-symptoms-solr-dashboard.json`

![](/assets/chronic-symptoms.png)

### 4. Generative AI for Patient Advising by Physician
Open the Physician Portal in the CML Application to access and interface with this component.

![](/assets/physician-portal.png)

## Final AMP Setup (Manual)

1. Setup Solr app instance for unauthenticated app access (IMPORTANT! Must do before next step!)

![](/assets/unauthenticated-access.png)

2. Execute Solr Setup Scripts (can be done in session or by the created Job) - Create collection, generate data, add data, add stopwords, make dashboard

    If in session, run script: `4_solr/execute-solr-scripts.py`

    If by job, run `Execute Solr Scripts` job that was created during AMP setup (preferred)

3. Navigate to `https://[CML APPLICATION]/solr/banana/src/index.html#/dashboard` to view Banana UI