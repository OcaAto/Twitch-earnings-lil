SELECT COUNT(average_viewers) AS streamers_over5k
FROM df_twitchdata_limpio2
WHERE average_viewers >= 5000