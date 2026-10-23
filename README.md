# pacers-injury-analysis

How did the Indiana Pacers change with and without Tyrese Haliburton, and how much of that was injuries versus everything else? This repo analyzes team performance across three seasons using public NBA data.

## The three seasons

| Season | Context |
|---|---|
| **2024-25** | Finals run. Haliburton tore his Achilles in Game 7 of the 2025 Finals, which the Pacers lost. This season is the healthy baseline. |
| **2025-26** | Haliburton missed the entire season, and the roster was hit by other injuries too. The Pacers went 19-63, and it's debated how much of the year was a deliberate push for draft position. |
| **2026-27** | Haliburton returns from the Achilles injury. The season is in progress, so results here are preliminary and will be updated as games are played. |

## Questions

1. How did the offense change (pace, shot profile, ball movement, four factors) across seasons?
2. Which lineups drove the changes, and how reliable are those numbers?
3. How much value did the team lose to injuries, and how much of that was one player?
4. How does the team look in 2026-27 compared to the healthy baseline, as the sample grows? Do players like Zubac and Oubre Jr. make a significant difference compared to Turner and Mathurin?

## Data

- Team and player game logs, lineups, and shot data from the NBA's stats API via [`nba_api`](https://github.com/swar/nba_api)
- Stored locally in DuckDB (raw pulls are cached in `data/raw/`)

## Repo structure
