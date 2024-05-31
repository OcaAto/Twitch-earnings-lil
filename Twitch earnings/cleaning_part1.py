import pandas as pd
import numpy as np
#btw limpio means clean

df_channels_Twitch = pd.read_csv('channel.csv')
df_timedata_Twitch = pd.read_csv('time_data.csv')
df_views_Twitch = pd.read_csv('views.csv')
df_conjunto = pd.merge(df_channels_Twitch, df_timedata_Twitch, on ='channel_id')
df_twitchdatas = pd.merge(df_conjunto, df_views_Twitch, on ='channel_id')
df_twitchdata = df_twitchdatas.drop_duplicates()


df_twitchdata_limpio = df_twitchdata.drop(['platform_y', 'channel_name_x', 'channel_name_y', 'platform_x'], axis=1)
df_twitchdata_limpio['last_streamed_game'] = df_twitchdata_limpio['last_streamed_game'].str.replace('Pokémon Community Game', 'Pokemon Community Game')
# i did this change because if you open this csv in excel it will appear PokÃ©mon Community Game
df_twitchdata_limpio["airtime_in_m"] = round(df_twitchdata_limpio['airtime_in_m'] / 60 , 1)
# i changed the minutes for hours also a i used round to get a more clear result
df_twitchdata_limpio.drop(32, inplace=True)
# this row was a stream made by bts they did it only once based on the info i searched in google ... so i deleted :D

#   ** df if you want to get columns in other df = df_twitchdata_limpio[df_twitchdata_limpio["] == ""]
#    **df twitchdata limpio without the columns you desire = df_twitchdata_limpio[df_twitchdata_limpio[""] != ""]
df_twitchdata_limpio['channel_type'].fillna('Organization', inplace=True)
# there was some organizations that had null values
df_organization = df_twitchdata_limpio[df_twitchdata_limpio['channel_type'] == 'Organization']
df_twitchdata_limpio2 = df_twitchdata_limpio[df_twitchdata_limpio['channel_type'] != 'Organization']
# and this code is for looking into the column channel type and filter the organization rows
#print(df_twitchdata_limpio2)
#df_twitchdata_limpio2.to_csv('df_twitchdata_limpio2.csv')    
#df_organization.to_csv('df_organization.csv')

