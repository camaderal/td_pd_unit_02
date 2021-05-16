import constants

def clean_data(orig_players):
    players = []

    for player in orig_players:
        player = player.copy()
        player["height"] = int(player["height"].split()[0])
        player["experience"] = player["experience"] == "YES"
        player["guardians"] =  player["guardians"].split(" and ")

        # experienced players will be inserted at the front of queue
        # inexperienced players will be inserted at the tail of queue
        if player["experience"]:
            players.insert(0, player)
        else:
            players.append(player)

    return players


def balance_teams(players, teams):
    num_of_teams = len(teams)
    team_info = [{"name": team, "roster":[]} for team in teams]

    # loop through all players and assign each player to each team in order
    # experienced players will be in the front of queue so each team should get an equal number of experienced players
    for idx, player in enumerate(players):
        team_info[idx%num_of_teams]["roster"].append(player)

    return team_info

def print_team_stats(team):
    num_players = len(team['roster'])
    player_height_sum = 0
    num_exp_player = 0
    num_inexp_player = 0
    player_names = []
    all_guardians = []

    print("")
    print(f"Team: {team['name']} Stats")
    print("--------------------")


    for player in team['roster']:
        player_height_sum += player['height']
        player_names.append(player['name'])
        all_guardians.extend(player['guardians'])

        if player['experience']:
            num_exp_player += 1
        else:
            num_inexp_player += 1

    print(f"Total players: {num_players}")
    print(f"Total experienced players: {num_exp_player}")
    print(f"Total inexperienced players: {num_inexp_player}")
    print(f"Average height: {round(player_height_sum/num_players)} inches")
    print("")
    print(f"Players on Team: {', '.join(player_names)}")
    print(f"Guardians: {', '.join(all_guardians)}")

def main():

    players = clean_data(constants.PLAYERS)
    team_roster= balance_teams(players, constants.TEAMS)

    while True:
        print()
        print("---- MENU----")
        print()
        print("  Here are your choices:")
        print("    A) Display Team Stats")
        print("    B) Quit")
        print()
        choice = input("Enter an option: ")
        print()

        if choice.upper() == "A":
            for idx, team in enumerate(team_roster):
                print(f"{idx + 1}) {team['name']}")

            print()

            choice = input("Enter an option: ")
            try:
                choice = int(choice)
                if choice not in range(1, len(team_roster)+1):
                    raise ValueError
            except:
                print("Invalid input. Please try again.")
                continue

            print_team_stats(team_roster[choice -1])
            print()

        elif choice.upper() == "B":
            print("Bye!")
            print()
            break

        else:
            print("Invalid input. Please try again.")
            print()


if __name__ == "__main__":
    main()
