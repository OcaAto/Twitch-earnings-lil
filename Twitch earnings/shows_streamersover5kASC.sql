SELECT channel_name, channel_country, stream_language, airtime_in_m, peak_viewers, average_viewers
FROM df_twitchdata_limpio2
WHERE average_viewers >= 5000
ORDER BY average_viewers ASC
