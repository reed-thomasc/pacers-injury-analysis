import time
from pathlib import Path

from nba_api.stats.endpoints import leaguegamelog

SEASONS = ["2024-25", "2025-26", "2026-27"]
CURRENT_SEASON = "2026-27"  # still being played, so always re-pull it

RAW = Path("data/raw")
RAW.mkdir(parents=True, exist_ok=True)


def pull(season, kind):
    """Pull one season of game logs. kind is 'T' (team rows) or 'P' (player rows)."""
    label = "team" if kind == "T" else "player"
    out = RAW / f"{label}_games_{season}.parquet"

    #  don't ask the NBA again for completed seasons
    if out.exists() and season != CURRENT_SEASON:
        print(f"skip {out.name} (already pulled)")
        return

    # Retry a few times, since stats.nba.com is sometimes slow
    for attempt in range(1, 4):
        try:
            log = leaguegamelog.LeagueGameLog(
                season=season,
                season_type_all_star="Regular Season",
                player_or_team_abbreviation=kind,
                timeout=60,
            )
            df = log.get_data_frames()[0]
            df["SEASON"] = season
            df.to_parquet(out)
            print(f"saved {out.name}: {df.shape[0]} rows")
            return
        except Exception as e:
            print(f"attempt {attempt} failed for {out.name}: {e}")
            time.sleep(5)
    print(f"GAVE UP on {out.name}")


for season in SEASONS:
    for kind in ["T", "P"]:
        pull(season, kind)
        time.sleep(2) 