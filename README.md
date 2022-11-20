DOCUREADER
=

# Introduction
**DOCUREADER** is a script to support the operation of **search and extraction** of text inside a set of documents.

**DOCUREADER** flow example:
- Script accept following parameters:
  - keyword to search (mandatory);
  - source path (default: *input/docs*)
  - target path (default: *output/results*)
- Read documents from source directory;
- Extract metadata from document (eg. title, author, number of pages);
- Search keyword inside documents, and for each instance found:
  - Extract phrase that contains keyword;
  - Extract text (about 500 characters) containing keyword;
- Produce a file inside target path with name <keyword><datetime>.txt

## Output example
This is an example of result for *test* keyword. 

Filename: **test11-20-2022,10:31:09.193.txt**

```txt
Title: <title example>
Subject: 
Keywords: 
Author: <author example> 
Year: 2021
Pages: 18
Found 23 occurrences
Page: 4
Phrase:  This eval-
uation can be considered inadequate since they
used 5-fold cross-validation; therefore, data from 245
the same person was present both in the train-
ing and testing phases.
Text: n
accuracies of 87.32% to 91.63% using keystroke
dynamics on their GREYC dataset. This eval-
uation can be considered inadequate since they
used 5-fold cross-validation; therefore, data from 245
the same person was present both in the train-
ing and testing phases. Fairhurst & Da Costa-
Abreu (2011), besides user identity classication,
performed gender classication on the same GR-
EYC dataset. Again they report results based on 250
10-fold cross-validation. Antal & Nemes (2016) ex-
ploited key

Page: 5
Phrase:  Lastly, our method
has been tested not only on smartphones but also
on tablets.
Text: n to perform the recognition task. Fur-
thermore, we found that pinch-to-zoom is more dis- 295
criminant than swipe and drag-and-drop and com-
bination of such are very eective when compared
with swipe and drag-and-drop. Lastly, our method
has been tested not only on smartphones but also
on tablets. 300
3.2. Age-group recognition based on touch gestures
Several researchers employed gestures for age-
group classication. In more details, Vatavu et al.
```

# Installation 
Follow this procedure to install locally **DOCUREADER**.

## Prerequisite
This project use **Python 3.9.5** version. 

### Optional
We use *pyenv* to set and use a virtualenv instead global environment.

## Dependencies
Dependencies are stored into [requirements.txt](requirements.txt). Install through pip from project directory:
```shell
pip install -r requirements.txt
```

## Directories
It's necessary to create default input and output directories.

Path **input/docs** is the default input location for files to analyze.

Path **output/results** is the default output location for results.

From directory project: 
```shell
mkdir -p input/docs
mkdir -p output/results
```

# Usage
From project directory launch **DOCUREADER** through:
```shell
launch.py [-h] -s SEARCH [-i INPUT_PATH] [-r RESULT_PATH]

optional arguments:
  -h, --help            show this help message and exit
  -s SEARCH, --search SEARCH
                        Search key into files
  -i INPUT_PATH, --input_path INPUT_PATH
                        Directory path containing files
  -r RESULT_PATH, --result_path RESULT_PATH
                        Directory path containing results
```
