# Ambine Python Coding Challenge

## The task

Your task is to create a simple web service serving NHL regular season team standings. To simplify things a bit, you can consider all the teams to be in one league. So there is no need to consider the different divisions or conferenses when producing the standings calculation.

Example of expected solution:

```bash
# Web service serving standings for selected season
# http://localhost:<port>/standings/<seasonid>

curl -i http://localhost:5000/standings/20182019
HTTP/1.0 200 OK
Content-Type: application/json; charset=utf-8
Content-Length: xx
Server: Werkzeug/1.0.1 Python/3.7.6
Date: Tue, 09 Feb 2021 12:15:39 GMT

[
    {
        "team": "Tampa Bay Lighting",
        "points": 128
    },
    {
        "team": "Calgary Flames",
        "points": 107
    },
    ...
]
```

**Setup:**

The repository has a skeleton Flask app for convenience.

-   Use correct [Python version](.python-version)
-   Initialize development environment `source ./init-project.sh`
    - Or optionally Dockerize the application
-   Start the development server `make run`

**Other remarks:**

-   Return the teams in descending order based on total points
-   If you want to go the extra mile, return also stats for games played, wins, losses and overtime losses (includes shootout losses)
- Return data must be JSON
- Since the data is historical, you don't need to worry about it being dynamically updated in the future for this service

## Data description

The dataset consist of two files containing match results and team meta data. Datasets haven't been cleaned up so they contain columns you won't need to complete this task.

### [game_data.csv](data/game_data.csv)

Contains match results for all NHL regular season and play off games from seasons 2011-2012 to 2018-2019.

| Key                    | Description                                                        |
| ---------------------- | ------------------------------------------------------------------ |
| game_id                | Game key field as assigned by the NHL                              |
| season                 | Season identifier                                                  |
| type                   | R=Regular Season, P=Playoff                                        |
| date_time              | Match day                                                          |
| date_time_GMT          | Match day and time in GMT                                          |
| away_team_id           | Away team identifier                                               |
| home_team_id           | Home team identifier                                               |
| away_goals             | Away team goals                                                    |
| home_goals             | Home team goals                                                    |
| outcome                | REG=regular time, OT=overtime, SO=shootouts                        |
| home_rink_side_start   | Indicates the direction of play relative to the Time/Score keepers |
| venue                  |                                                                    |
| venue_link             |                                                                    |
| venue_time_zone_id     |                                                                    |
| venue_time_zone_offset |                                                                    |
| venue_time_zone_offset |                                                                    |
| venue_time_zone_tz     |                                                                    |

### [team_info.csv](data/team_info.csv)

Contains team metadata information.

| Key          | Description            |
| ------------ | ---------------------- |
| team_id      | Team identifier        |
| franchiseId  | Franchise identifier   |
| shortName    | Team short name        |
| teamName     | Team name              |
| abbreviation | Team name abbreviation |
| link         |                        |

## How to calculate team points

That's quite simple:

-   If a team wins in regular time, overtime or in the shootouts, the team gets two points
-   If a team loses in regular time, the team gets zero points
-   If a team loses in overtime or in the shooutouts, the team gets one point

## Evaluation criteria

Your solution is evaluated based on the following criteria:

-   Individual git commits

    -   Readable commit messages
    -   Commit size

-   Python usage

    -   Readability
    -   Performance
    -   Packages used
    -   Code quality (data stucturs etc.)
    -   Using type hints
    -   Following linting rules (flake8)

-   Tests
    -   HTTP endpoint(s) should have tests for at least
        -   Success cases (200)
        -   Error cases (eg. invalid season id)
    -   Unit tests where applicable
