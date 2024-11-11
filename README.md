This is a 2 phase mapreduce task which takes a collection of articles from different news sources and calculates the similarity of sources.

For this I used Jaccard Similarity which is not the best for comparing text it is a good starting point.

Phase 1:

Mapper - Cleans Raw data by tokenizing and normalizing all the urls that come from the same source, but have slightly different urls
        Output in form of {source:::text}

Reducer - Takes the output of the mapper and combines all articles which come from the same source
        Output in form of {source:::combined_text}

Phase 2:

Mapper - Takes the output of phase 1 and generates all combinations of different news outlets in order to prepare for calculation of jaccard similarity
        Output in form of {'A': source_0, 'B': source_1}

Reducer - Takes each combination given by the mapper and computes the Jaccard similarity between each, and writes it to a file.

