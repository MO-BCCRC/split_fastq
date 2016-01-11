#splitfastq: 
outputs a chunk of the fastq files with lines that lie within the specified range.


```
Development information

date created : Aug 28 2014
last update  : Sep 19  2014
Developer    : Diljot Grewal (dgrewal@bccrc.ca)
Input        : fastq file
Output       : chunk of the input (fastq format)
Parameters   : range (beginning and end separated by colon (:))
Seed used    : 
```

###Usage:
The range format is (The interval file):

```

1:40   -> first chunk from 40 equal splits 
2:40   -> second chunk from 40 equal splits
...
...
40:40  -> last chunk from 40 equal splits

```

###Dependencies

- python

###Known issues


###Last updates

