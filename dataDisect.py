import json
from prepare_corpus import *
import csv
import pandas as pd
from watson_developer_cloud import NaturalLanguageUnderstandingV1
import watson_developer_cloud.natural_language_understanding_v1 as ai
import logging

def getKey(item):
    return int(item["created"])


    #comments_dict_temp = json.load(inputFile)
comments_dict_temp = pd.read_csv('allData.csv')
comments_dict = comments_dict_temp.sort_values('created')




# print("-----------------------------------------")

# for comment in comments_dict:
#  print(getKey(item=comment))

# data columns:
columns = ("comment_id",
           "created",
           "body")

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
for _,comment in comments_dict.iterrows():
    process+=1
    output = pd.DataFrame([], columns=columns)
    
    if process>178100+(2147863/20)*8 and process<=178100+(2147863/20)*9:
        comment={"comment_id": comment['comment_id'],
                     "body": comment['body'],
                     "created": comment['created'],
        }
        output = output.append(comment,ignore_index=True)
        output.to_csv('data9.csv', index=False, header=True if headerDisp==7 else False,mode='a', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n')
        headerDisp=8;

    if process>178100+(2147863/20)*9 and process<=178100+(2147863/20)*10:
        comment={"comment_id": comment['comment_id'],
                     "body": comment['body'],
                     "created": comment['created'],
        }
        output = output.append(comment,ignore_index=True)
        output.to_csv('data10.csv', index=False, header=True if headerDisp==8 else False,mode='a', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n')
        headerDisp=9;

    if process>178100+(2147863/20)*10 and process<=178100+(2147863/20)*11:
        comment={"comment_id": comment['comment_id'],
                     "body": comment['body'],
                     "created": comment['created'],
        }
        output = output.append(comment,ignore_index=True)
        output.to_csv('data11.csv', index=False, header=True if headerDisp==9 else False,mode='a', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n')
        headerDisp=10;
    
    if process>178100+(2147863/20)*11 and process<=178100+(2147863/20)*12:
        comment={"comment_id": comment['comment_id'],
                     "body": comment['body'],
                     "created": comment['created'],
        }
        output = output.append(comment,ignore_index=True)
        output.to_csv('data12.csv', index=False, header=True if headerDisp==10 else False,mode='a', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n')
        headerDisp=11;
    
    if process>178100+(2147863/20)*12 and process<=178100+(2147863/20)*13:
        comment={"comment_id": comment['comment_id'],
                     "body": comment['body'],
                     "created": comment['created'],
        }
        output = output.append(comment,ignore_index=True)
        output.to_csv('data13.csv', index=False, header=True if headerDisp==11 else False,mode='a', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n')
        headerDisp=12;

    if process>178100+(2147863/20)*13 and process<=178100+(2147863/20)*14:
        comment={"comment_id": comment['comment_id'],
                     "body": comment['body'],
                     "created": comment['created'],
        }
        output = output.append(comment,ignore_index=True)
        output.to_csv('data14.csv', index=False, header=True if headerDisp==12 else False,mode='a', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n')
        headerDisp=13;

    if process>178100+(2147863/20)*14 and process<=178100+(2147863/20)*15:
        comment={"comment_id": comment['comment_id'],
                     "body": comment['body'],
                     "created": comment['created'],
        }
        output = output.append(comment,ignore_index=True)
        output.to_csv('data15.csv', index=False, header=True if headerDisp==13 else False,mode='a', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n')
        headerDisp=14;
    
    if process>178100+(2147863/20)*15 and process<=178100+(2147863/20)*16:
        comment={"comment_id": comment['comment_id'],
                     "body": comment['body'],
                     "created": comment['created'],
        }
        output = output.append(comment,ignore_index=True)
        output.to_csv('data16.csv', index=False, header=True if headerDisp==14 else False,mode='a', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n')
        headerDisp=15;
    
    if process>178100+(2147863/20)*16 and process<=178100+(2147863/20)*17:
        comment={"comment_id": comment['comment_id'],
                     "body": comment['body'],
                     "created": comment['created'],
        }
        output = output.append(comment,ignore_index=True)
        output.to_csv('data17.csv', index=False, header=True if headerDisp==15 else False,mode='a', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n')
        headerDisp=16;

    if process>178100+(2147863/20)*17 and process<=178100+(2147863/20)*18:
        comment={"comment_id": comment['comment_id'],
                     "body": comment['body'],
                     "created": comment['created'],
        }
        output = output.append(comment,ignore_index=True)
        output.to_csv('data18.csv', index=False, header=True if headerDisp==16 else False,mode='a', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n')
        headerDisp=17;

    if process>178100+(2147863/20)*18 and process<=178100+(2147863/20)*19:
        comment={"comment_id": comment['comment_id'],
                     "body": comment['body'],
                     "created": comment['created'],
        }
        output = output.append(comment,ignore_index=True)
        output.to_csv('data19.csv', index=False, header=True if headerDisp==17 else False,mode='a', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n')
        headerDisp=18;
    
    if process>178100+(2147863/20)*19 and process<=178100+(2147863/20)*20:
        comment={"comment_id": comment['comment_id'],
                     "body": comment['body'],
                     "created": comment['created'],
        }
        output = output.append(comment,ignore_index=True)
        output.to_csv('data20.csv', index=False, header=True if headerDisp==18 else False,mode='a', quoting=csv.QUOTE_NONNUMERIC, line_terminator='\n')
        headerDisp=19;    
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!            ",process)

#df_plot_2_2.drop(['level_0'], axis=1).to_csv(dataPath+'digitalDPlot2_2_3d.csv', index=False)
