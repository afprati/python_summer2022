# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 14:17:06 2022

@author: Tita
"""
import tweepy
import importlib
import os
import pandas as pd

os.chdir('C:\\Users\\Tita\\Documents')
twitter = importlib.import_module("start_twitter")
api = twitter.client


wustl_user = api.get_user(screen_name='WUSTLPoliSci')


wustl_followers = api.get_follower_ids(screen_name='WUSTLPoliSci') #get ids list of followers
len(wustl_followers)

wustl_friends = api.get_friend_ids(screen_name='WUSTLPoliSci') #get ids list of following
len(wustl_friends)

wustl_followers_proof = wustl_followers[:20]

list_screenames = []
list_active = []
list_popular = []

for i in wustl_followers:
    followers_id = api.get_user(user_id=i)
    statuses_count = followers_id.statuses_count #count number of tweets 
    list_active.append(statuses_count)
    
    followers_count = followers_id.followers_count #count number of followers
    list_popular.append(followers_count)
    
    user = api.get_user(id=i)
    screen_name = user.screen_name
    list_screenames.append(screen_name)
    
    


df = pd.DataFrame({"screen_name": list_screenames, "active": list_active, "popular": list_popular})

most_popular = df.sort_values('popular',ascending=False) #get most popular follower at the beginning of df

#### @mariapaularomo 357,080 followers
most_active = df.sort_values('active',ascending=False) #get most active follower at the beginning of df
#### @ TheNjoroge 171,081 tweets


###Friends of WUSTL

wustl_friends_proof = wustl_friends[:20]

list_active_friends = []
list_popular_friends = []
list_screenames_friends = []

for i in wustl_friends:
    friends_id = api.get_user(user_id=i)
    statuses_count = friends_id.statuses_count #count number of tweets 
    list_active_friends.append(statuses_count)
    
    friends_count = friends_id.followers_count #count number of followers
    list_popular_friends.append(friends_count)
    
    user = api.get_user(id=i)
    screen_name = user.screen_name
    list_screenames_friends.append(screen_name)
    
    

df_friends = pd.DataFrame({"screen_name": list_screenames_friends, "active": list_active_friends, "popular": list_popular_friends})

#layman
layman_df = df_friends[df_friends['popular'] < 100]
most_active_layman = layman_df.sort_values('active',ascending=False) 
### Layman: usmanfalalu1 with 1440 tweets


#expert
expert_df = df_friends[df_friends['popular'].between(100, 1000, inclusive=False)]
most_active_expert = expert_df.sort_values('active',ascending=False) 
###Expert: prof_nokken with 20378 tweets


#celebrity
celebrity_df = df_friends[df_friends['popular'] > 1000]
most_active_celibrity = celebrity_df.sort_values('active',ascending=False) 
###Expert: nytimes  with 481,642 tweets
#Attempt to followers of followers
list_active_f_followers = []
list_active_f_friends = []
for i in wustl_followers:
    followers_id = api.get_user(user_id=i)
    for i in followers_id:
        f_f = api.get_user(friends_id =i)
        statuses_count = f_f.statuses_count #count number of tweets 
        list_active_f_followers.append(statuses_count)
        
#Attempt to friends of friends
for i in wustl_friends:
    ftiends_id = api.get_user(user_id=i)
    for i in followers_id:
        f_friends = api.get_user(friends_id =i)
        statuses_count = f_friends.statuses_count #count number of tweets 
        list_active_f_friends.append(statuses_count)        
        
        
        
        