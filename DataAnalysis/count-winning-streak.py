#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Static implementation of players summary of their games. 
# L - Loss and W - Win.
player_one_summary = ['L', 'W', 'W', 'W', 'L', 'W']
player_two_summary = ['W', 'W', 'L', 'W', 'L', 'W']
player_three_summary = ['L', 'L', 'L', 'L', 'L', 'W']
player_four_summary  = ['L', 'L', 'L', 'L', 'L', 'L']

def winning_streak(player_summary: list[str]) -> int:
    counter = 0
    for i in range(0, len(player_summary)):
        for j in range(i + 1, len(player_summary)):
            if (player_summary[i] == 'W') and (player_summary[j] == 'W'):
                counter += 1
            else:
                break
    if counter == 1:
        counter = 2
    return counter


def main() -> None:
    player_one_streak = winning_streak(player_one_summary)
    player_two_streak = winning_streak(player_two_summary)
    player_three_streak = winning_streak(player_three_summary)
    player_four_streak  = winning_streak(player_four_summary)

    print(
        f"Player one: {player_one_streak}",
        f"Player two: {player_two_streak}",
        f"Player three: {player_three_streak}",
        f"Player four: {player_four_streak}",
        sep="\n\n"
    )
    return

if __name__ == "__main__":
    main()
