#synonym-list

Solr Synoym mapping file for track, release and Artist Searches in the Search-API

We will accept pull requests.

Edit the synonyms.txt file to add new synonyms. Use the syntax as described [in the Solr wiki](https://wiki.apache.org/solr/AnalyzersTokenizersTokenFilters#solr.SynonymFilterFactory).

##Explicit mappings
- Explicit mappings are declared using two word lists separated by `=>`.
- Word lists are are composed of words separated by `,`.
- Any word matching matching a word in the LHS word list is replaced by all the words in the RHS word list. A single word can be expanded to many words.

###Example
####synonym spec
```
i-pod => ipod, i pod
sea biscuit, sea biscit => seabiscuit
```
####transformations
- `i-pod` is transformed to `ipod` and `i pod`
- `sea biscuit` is transformed to `seabiscuit`
- `sea biscit` is transformed to `seabiscuit`
- other words are unchanged.

##Equivalent mappings
- Equivalent mappings are declared by as a single word list.
- Behaviour depends on `expand` parameter in schema. 7digital's schema sets `expand=true`.
- With `expand=true` equivalent mappings are the same as explicit mapping with LHS = RHS

###Example
####synonym spec
```
ipod, i-pod, i pod
```
####as explicit mappings
```
ipod, i-pod, i pod => ipod, i-pod, i pod
```
####transformations
- `ipod`, `i-pod` and `i pod` are each transformed to `ipod`, `i-pod` and `i pod`
- other words are unchanged

##Words matching multiple mappings
- If a word matches multiple mappings, they are all applied at the same time. Mappings can be defined in any order

###Example
####As multiple mappings
```
foo => foo bar
foo => baz
```
####As one mapping
```
foo => foo bar, baz
```

##Case sensitivity
- Synonyms can be both case sensitive and insensitive.
- 7digital's schema is case insensitive.

###Example
####synonym spec
```
ipod => i pod
```
####transformations
- `iPod`, `IpOd` and `IPOD` are all transformed to `i pod`

##Comments and blank lines
- Blank lines and comments are ignored.
- Comments are lines starting with `#`
