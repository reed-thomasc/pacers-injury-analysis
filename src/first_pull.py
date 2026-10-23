from nba_api.stats.endpoints import teamgamelog

PACERS_ID = 1610612754

#call pacers stats for 2024-2025 regular season from nba stats site
log = teamgamelog.TeamGameLog(
	team_id=PACERS_ID,
	season="2024-25",
	season_type_all_star="Regular Season",
	timeout=60,
)


df = log.get_data_frames()[0]

print(df.shape)
print(df.head())
print(df["WL"].value_counts())

df.to_parquet("data/raw/pacers_teamgamelog_2024-25.parquet")
print("saved")