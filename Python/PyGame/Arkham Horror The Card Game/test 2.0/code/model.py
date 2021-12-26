from models import player
from models import investigator
from models import location
from models import scenario
players = player.players
investigators = investigator.investigators
locations = location.locations
scenarios = scenario.scenarios


def main():
    investigator.get_investigators()
    player.get_players(2)
    location.get_locations()
    scenario.get_scenarios()
