import random


def generate_initial_game():
    sorted_numbers = []
    while len(sorted_numbers) < 14:
        sorted_number = random.randint(1, 25)
        if sorted_number not in sorted_numbers:
            sorted_numbers.append(sorted_number)

    return sorted_numbers


def complete_game_numbers(initial_game):
    all_games = []

    while len(all_games) < 11:
        current_game = []
        current_game.extend(initial_game)

        while len(current_game) < 15:
            sorted_number = random.randint(1, 25)

            can_add_number = True
            if sorted_number not in current_game:
                for game_ready in all_games:
                    if sorted_number in game_ready:
                        can_add_number = False

                if can_add_number:
                    current_game.append(sorted_number)
                    all_games.append(current_game)

    return all_games


def generate_magical_game():
    initial_numbers = generate_initial_game()

    return complete_game_numbers(sorted(initial_numbers))


if __name__ == '__main__':
    game_results = generate_magical_game()
    for game in game_results:
        print(game)