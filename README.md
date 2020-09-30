## ICAP_Crawler v0.6
By Peter Rucker

#### TLDR:

Pulls useful antigen -> IIF ANA Pattern relationships from the ICAP autoimmune.org website, and condenses them into 
CSV formats.

To use, run main.py

#### Long Version:

This project started as a way to more easily understand the relationship between ANA IIF patterns on HEp-2/HEp-2000 cells,
and the antigens responsible for producing those pattern. Although the ICAP website maintains an exhaustive list of patterns, 
related antibodies, and their associated disease states, the information is spread across multiple locations on their website.

This script visits each of these pages, collects the official pattern name (Per ICAP), and associates the related antigens. 
It then produces two CSV files, one relating patterns -> antigens, and a much longer list relating antigens -> patterns.

#### Requirements
Please see requirements.txt

#### Roadmap
Future versions will attempts to corrolate possible disease states to IIF pattern.


