# Player card values
player1 = [10, 6, 8, 9, 7, 12, 7]
player2 = [7, 6, 9, 5, 2, 8, 11]

# Counters to track wins
player1_score = 0
player2_score = 0

# Loop through 7 rounds
for i in range(7):

    print("Round number",i + 1, ":")

    # Get cards using index
    card1 = player1[i]
    card2 = player2[i]

    # Compare cards
    if card1 > card2:
        print("Player 1 wins the round with", card1, "beating", card2)
        player1_score += 1

    elif card2 > card1:
        print("Player 2 wins the round with", card2, "beating", card1)
        player2_score += 1

    else:
        print("The round has ended in a draw.")

# Determine overall winner
if player1_score > player2_score:
    print("\nPlayer 1 wins the game, by", player1_score, "to", player2_score, "!")

elif player2_score > player1_score:
    print("Player 2 wins the game, by", player2_score, "to", player1_score, "!")