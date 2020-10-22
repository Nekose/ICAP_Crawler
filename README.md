## ICAP_Crawler v0.7
By Peter Rucker

#### TLDR:

Pulls useful antigen -> IIF ANA Pattern relationships from the [ICAP website](https://www.anapatterns.org/), and condenses them into 
TSV formats.

To use, run main.py

#### Long Version:

This project started as a way to more easily understand the relationship between ANA IIF patterns on HEp-2/HEp-2000 cells,
and the antigens responsible for producing those pattern. Although the ICAP website maintains an exhaustive list of patterns, 
related antibodies, and their associated disease states, the information is spread across multiple locations on their website.

The Pattern class, when initilized accepts an AC Number (per ICAP guidlines) or the URL of the ICAP pattern webpage. Afterwhich it crawls the relevant page, and collects the following information to store within the pattern object:
* AC Number
* Pattern Name
* Associated Antigens
* Previous Names
* Pattern Description

If given a list of pattern objects, the **DataWriter.antigen_data_format** or **DataWriter.pattern_data_format** will create a list of strings ready to be written to a TSV file. Antigen format creates an entry for every antigen and assocaites a pattern, while pattern format creates an entry for every name and alternative name associated with their antigens.

Lastly, **DataWriter.file_writer** accepts this output, and creates the TSV files. If a previous file with the same name is detected, and comparison is made, and differences captured to a changelog.


#### Requirements
Please see requirements.txt

#### Roadmap
Future versions will attempts to correlate possible disease states to IIF pattern.


