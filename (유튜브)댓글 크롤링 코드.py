
import pandas as pd
from googleapiclient.discovery import build


comments = list()
api_key = 'AIzaSyDMirfFkPzFdY8wpmLcbBxFHdyY3eXDKHk' #이건 내가 받은 API KEY 
video_id = 'V3ZR8bBptS4' #유튜브 영상아이디 #예시로 내가 좋아하는 채널 아이디를 넣어둔 것.
api_obj = build('youtube', 'v3', developerKey=api_key)
response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, maxResults=100).execute()

while response:
    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append([comment['textDisplay'], comment['authorDisplayName'], comment['publishedAt'], comment['likeCount']])
 
        if item['snippet']['totalReplyCount'] > 0:
            for reply_item in item['replies']['comments']:
                reply = reply_item['snippet']
                comments.append([reply['textDisplay'], reply['authorDisplayName'], reply['publishedAt'], reply['likeCount']])
 
    if 'nextPageToken' in response:
        response = api_obj.commentThreads().list(part='snippet,replies', videoId=video_id, pageToken=response['nextPageToken'], maxResults=100).execute()
    else:
        break

df = pd.DataFrame(comments)
# 엑셀(또는 csv로) 저장
df.to_csv('results.csv', header=['comment', 'author', 'date', 'num_likes'], index=None)

출처: https://untitledtblog.tistory.com/169
