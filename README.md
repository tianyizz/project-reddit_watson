# project-reddit_watson
The .py files posted will generate the .csv files.

# Implementation
The entry point is the reddit_new.py. The reddit_new.py will work on the specified data file and yield largeResult.csv which contains the Watson NLP generated results (emotions, sentiment, etc..), created time in linux time format, the orginal text, and the prepared text. Note that the prepared text is just a reference for user and it is not used in Watson NLP.

dataDisect.py will partition the dataset into 20 different files for multithreading.

The second file to be run is redditSentProcess.py, which generates timeLargeResult.json (same as the largeResult.json except converted linux time to human readable format), emotJoyHisLarge.json, and sentHIsLarge.json.

The redditProcess.py together with redditKeyProcess.py will give a detailed information on key words found, and it generates the largeKey.json and largeKeyDetail.json.

run.sh is the bash file to initiate multithreading. It will start running different reddit_new.py that is targeting on different parts of the dataset.
