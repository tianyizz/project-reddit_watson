import json
from prepare_corpus import *
import csv
import pandas as pd
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding_v1 as ai
import logging
logging.basicConfig(filename='error.log', level=logging.ERROR)  # This defines the name of the error log file
# If service instance provides API key authentication
# service = NaturalLanguageUnderstandingV1(
#     version='2018-03-16',
#     ## url is optional, and defaults to the URL below. Use the correct URL for your region.
#     url='https://gateway.watsonplatform.net/natural-language-understanding/api',
#     iam_apikey='your_apikey')

def getKey(item):
    return int(item["created"])

service = NaturalLanguageUnderstandingV1(
    version='2018-11-16',
    iam_apikey='AGBtqHQviQSGkj12ofCHw7J0QsNjDKEj04PW-CRnxt6s',
    url='https://gateway.watsonplatform.net/natural-language-understanding/api'
)

'''
service = NaturalLanguageUnderstandingV1(
    version='2018-03-16',
    ## url is optional, and defaults to the URL below. Use the correct URL for your region.
    url='https://gateway.watsonplatform.net/natural-language-understanding/api',
    username='c2781ef5-373f-4dcb-8ce5-8ac101f00903',
    password='gp0r4wymoCbh')
'''


with open('data1.csv', 'r') as inputFile:
    #comments_dict_temp = json.load(inputFile)
    comments_dict_temp = pd.read_csv(inputFile)

    print(comments_dict_temp["body"][0])

    comments_dict = comments_dict_temp.sort_values('created')
    #comments_dict.to_csv('tryResult.csv', index=False, header=False, mode='a', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n')




# print("-----------------------------------------")

# for comment in comments_dict:
#  print(getKey(item=comment))

# data columns:
columns = ("comment_id",
           "text",
           "text_prepared",
           "time",
           "keyword",
           "keyword_sentiment_label",
           "keyword_sentiment_score",
           "emotion_sadness",
           "emotion_joy",
           "emotion_fear",
           "emotion_disgust",
           "emotion_anger",
           "sentiment_score",
           "sentiment_label")

columnsOther=list('')

# get list of processed comments
try:
    output = pd.read_csv('largeResult.csv') # change to fit file directory used
    processed_comments = output.iloc[:,1].tolist()
    print("Found it!")
except Exception as e:
    print("Warning: unable to load processed results. Error: ", e)
    processed_comments = []
    output = pd.DataFrame([], columns=columns)

    header_string = ", ".join(columns)+'\n'
    print(header_string)
    #TODO: fix this
    with open('largeResult.csv', 'w') as f:
        f.write(header_string)

    #output.to_csv(index=False, header=True, quoting=csv.QUOTE_NONNUMERIC)

print(processed_comments)

headerDisp=0
counter = 0
process=0
with open('largeResult1.csv', 'w') as outfile:
    for _,comment in comments_dict.iterrows():
        process+=1
        if comment not in processed_comments:
            counter += 1
            comment_prepared = text_prepare(comment['body'])
            # (comment_prepared)
            if comment_prepared == "0": continue
            comment['body'] = urlRm(comment['body'])
            if len(comment['body']) < 4: continue
            try:
                print('in here')
                response = service.analyze(text=comment['body'],
                                           features=ai.Features(
                                               sentiment=ai.SentimentOptions(),
                                               emotion=ai.EmotionOptions(),
                                               keywords=ai.KeywordsOptions(sentiment=True, emotion=True, limit=5))
                                           ).get_result()
                print('passed')
                print(response)
            except Exception as e:
                print("Something went wrong.... Error: ", e)
                logging.error(e)  # This should log the error messages to an error.log file
                continue

            if ('keywords' not in response) or ('emotion' not in response) or len(response['keywords']) == 0:
                continue
            print('out!')

            print(response['keywords'])
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~')
            print(len(response['keywords']))
            print('~~~~~~~~~~~~~~~~~~~~~~~~~~')

            thisTuple = {"comment_id": comment['comment_id'],
                         "text": comment['body'],
                         "text_prepared": comment_prepared,
                         "time": comment['created'],
                         "keyword": response['keywords'][0]['text'],
                         "keyword_sentiment_label": response['keywords'][0]['sentiment']['label'],
                         "keyword_sentiment_score": response['keywords'][0]['sentiment']['score'],
                         "emotion_sadness": response['emotion']['document']['emotion']['sadness'],
                         "emotion_joy": response['emotion']['document']['emotion']['joy'],
                         "emotion_fear": response['emotion']['document']['emotion']['fear'],
                         "emotion_disgust": response['emotion']['document']['emotion']['disgust'],
                         "emotion_anger": response['emotion']['document']['emotion']['anger'],
                         "sentiment_score": response['sentiment']['document']['score'],
                         "sentiment_label": response['sentiment']['document']['label']
                         }
            output = output.append(thisTuple, ignore_index=True)
            print(output)

            if counter % 7 == 0:
              output.to_csv(outfile, index=False, header=True if headerDisp==0 else False, mode='a', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n')
              output = pd.DataFrame([], columns=columns)
              headerDisp=1
              print('dumped!')
                

        print('Process~~~~~~~~~~~~~~~~~~~~',process/2147863,'count~~~~~~~~~~~~~~~~~~~~',process)

    # DOES catch final section of output
    #json.dump(output, outfile, indent=2)
    output.to_csv(outfile, index=False, header=False,mode='a', quoting=csv.QUOTE_NONNUMERIC)

    print('final dump!')

