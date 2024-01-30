#!/bin/bash

# Text to be appended
text_to_append="adjustments
Admitted
because
blood
changes
complained
Discharged
Discussed
Drew
Evaluated
for
hospital
me
medication
of
patient
Performed
Prescribed
Reason
Recommended
Started
tests
The
to
treatment
visit
Visited
was"

# Append text to the first file
echo "$text_to_append" >> "./solr-app/solr-9.3.0/server/solr/configsets/_default/conf/stopwords.txt"

# Append text to the second file
echo "$text_to_append" >> "./solr-app/solr-9.3.0/server/solr-webapp/webapp/banana/resources/banana-int-solr-4.4/banana-int/conf/stopwords.txt"
