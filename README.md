# project-reddit_watson
The .py files posted will generate the .json file posted (results).

# Implementation
The entry point is the reddit_new.py. The reddit_new.py will yield largeResult.json which contains the Watson NLP generated results (emotions, sentiment, etc..), created time in linux time format, the orginal text, and the prepared text. Note that the prepared text is just a reference for user and it is not used in Watson NLP.

The second file to be run is redditSentProcess.py, which generates timeLargeResult.json (same as the largeResult.json except converted linux time to human readable format), emotJoyHisLarge.json, and sentHIsLarge.json.

The redditProcess.py together with redditKeyProcess.py will give a detailed information on key words found, and it generates the largeKey.json and largeKeyDetail.json.
