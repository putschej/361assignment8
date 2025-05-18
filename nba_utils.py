# Jennifer Putsche
# putschej@oregonstate.edu
# CS361 Spring 2025
# S2.6 - Assignment 8: "Microservice A"
# See docs for nba_api: https://github.com/swar/nba_api/tree/master

from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster

# Build a dictionary of abbreviations to team IDs
try:
    # docs: https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/static/teams.md
    team_map = {team['abbreviation'].upper(): team['id'] for team in teams.get_teams()}
except Exception as e:
    print(f"Failed to load team map: {e}")
    team_map = {}


def get_team_roster(team_abbr, alphabetical_order):
    """
    Get the team roster for the requested 3-letter team abbreviation, and return a list of objects containing the
    jersey number, player name, sorted by jersey order, or sorted by alphabetical order if requested.
    :param team_abbr: 3-letter string representing a team name
    :param alphabetical_order: boolean representing desired results sort order (true = alphabetical, false = numerical)
    :return: {"valid": BOOL, [{"jersey_num": NUM, "name": NAME}...sorted on num or name if valid]}
    """
    team_abbr = team_abbr.upper()

    # if the request is not a valid team, return false and empty results
    if team_abbr not in team_map:
        return {"valid": False, "results": []}

    # we have a valid team, get the player roster: jersey numbers and player names
    team_id = team_map[team_abbr]
    try:
        # docs: https://github.com/swar/nba_api/blob/master/docs/nba_api/stats/endpoints/commonteamroster.md
        roster = commonteamroster.CommonTeamRoster(team_id=team_id)
        # docs: https://github.com/swar/nba_api/blob/master/src/nba_api/stats/endpoints/commonteamroster.py
        players = roster.get_data_frames()[0]
    except Exception as e:
        print(f"Failed to get team roster: {e}")
        return {"valid": False, "results": []}

    # build the results list
    result_list = []
    for _, player in players.iterrows():
        try:
            jersey = int(player["NUM"]) if player["NUM"].isdigit() else None
            name = player["PLAYER"]
            if jersey is not None and name:
                result_list.append({"jersey_num": jersey, "name": name})
        except Exception as e:
            print(f"Skipping player due to parse error: {e}")
            continue

    # order the results based on alphabetical or jersey number order
    if alphabetical_order:
        result_list.sort(key=lambda x: x["name"].lower())
    else:
        result_list.sort(key=lambda x: x["jersey_num"])

    return {"valid": True, "results": result_list}
