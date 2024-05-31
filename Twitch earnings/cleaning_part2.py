import pandas as pd

df_earningstw = pd.read_csv("twitchearnings.csv")
df_twdata = pd.read_csv("df_twitchdata_limpio2.csv")
df_earningstw.columns = df_earningstw.columns.str.replace("UserID", "channel_id")
df_earningstw.columns = df_earningstw.columns.str.replace("Rank", "Rank_GrossEarning")
#df_earningstw["channel_name"] = df_earningstw["channel_name"].str.lower() 
df_earningstw2 = pd.merge(df_earningstw, df_twdata, on = "channel_id")
df_EsTw = df_earningstw2[df_earningstw2['stream_language'] == 'es']
df_EnTw = df_earningstw2[df_earningstw2['stream_language'] == 'en']
#print(df_earningstw)
df_earningstw2.to_csv("df_twitchdata.csv")
df_EnTw.to_csv("df_StreamersEn.csv")
df_EsTw.to_csv("df_StreamersEs.csv")