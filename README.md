synonym-list
============

Solr Synoym mapping file for track, release and Artist Searches in the Search-API

[Taken from https://wiki.apache.org/solr/AnalyzersTokenizersTokenFilters#solr.SynonymFilterFactory](https://wiki.apache.org/solr/AnalyzersTokenizersTokenFilters#solr.SynonymFilterFactory)


\# blank lines and lines starting with pound are comments.

\#Explicit mappings match any token sequence on the LHS of "=>"
\#and replace with all alternatives on the RHS.  These types of mappings
\#ignore the expand parameter in the schema.
\#Examples:
i-pod, i pod => ipod,
sea biscuit, sea biscit => seabiscuit

\#Equivalent synonyms may be separated with commas and give
\#no explicit mapping.  In this case the mapping behavior will
\#be taken from the expand parameter in the schema.  This allows
\#the same synonym file to be used in different synonym handling strategies.
\#Examples:
ipod, i-pod, i pod
foozball , foosball
universe , cosmos

\# If expand==true, "ipod, i-pod, i pod" is equivalent to the explicit mapping:
ipod, i-pod, i pod => ipod, i-pod, i pod
\# If expand==false, "ipod, i-pod, i pod" is equivalent to the explicit mapping:
ipod, i-pod, i pod => ipod

\#multiple synonym mapping entries are merged.
foo => foo bar
foo => baz
\#is equivalent to
foo => foo bar, baz
