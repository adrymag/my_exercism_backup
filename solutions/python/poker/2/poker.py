from collections import Counter

def best_hands(hands):
    """
    Evaluate a list of poker hands and return the best one(s).
    Each hand is a string like "4D 5S 6S 8D 3C".
    Returns a list of the best hand string(s).
    Handles all standard poker hand rankings per Wikipedia:
    Straight Flush, Four of a Kind, Full House, Flush, Straight,
    Three of a Kind, Two Pair, One Pair, High Card.
    """

    RANK_ORDER = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
        '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    def parse_hand(hand_str):
        """Parse hand string into list of (rank_value, suit) tuples."""
        cards = hand_str.split()
        parsed = []
        for card in cards:
            suit = card[-1]
            rank_str = card.removesuffix(suit)
            '''
            if len(card) == 3:          # e.g., "10H"
                rank_str = card[:2]
                suit = card[2] # -1
            else:                       # e.g., "4D"
                rank_str = card[0]
                suit = card[1] # -1
            '''
            parsed.append((RANK_ORDER[rank_str], suit))
        return parsed

    def evaluate(hand_str):
        """
        Return a comparison tuple for a hand.
        Higher tuple = better hand. Tuples compare lexicographically.
        """
        cards = parse_hand(hand_str)
        ranks = sorted([c[0] for c in cards], reverse=True)
        suits = [c[1] for c in cards]
        rank_counts = Counter(ranks)

        # Group ranks by frequency: sort by freq desc, then rank desc
        freq_groups = sorted([(-freq, -rank) for rank, freq in rank_counts.items()])

        is_flush = len(set(suits)) == 1

        # --- Straight detection ---
        is_straight = False
        straight_high = 0
        unique_ranks = sorted(set(ranks), reverse=True)

        # Normal straight
        if len(unique_ranks) == 5 and unique_ranks[0] - unique_ranks[4] == 4:
            is_straight = True
            straight_high = unique_ranks[0]
        # Ace-low straight: A-2-3-4-5
        elif set(ranks) == {14, 2, 3, 4, 5}:
            is_straight = True
            straight_high = 5   # Ace plays as 1, so high card is 5

        # 1. Straight Flush (includes Royal Flush)
        if is_straight and is_flush:
            return (9, straight_high)

        # 2. Four of a Kind
        if freq_groups[0][0] == -4:
            four_rank = -freq_groups[0][1]
            kicker = -freq_groups[1][1]
            return (8, four_rank, kicker)

        # 3. Full House
        if freq_groups[0][0] == -3 and freq_groups[1][0] == -2:
            trip_rank = -freq_groups[0][1]
            pair_rank = -freq_groups[1][1]
            return (7, trip_rank, pair_rank)

        # 4. Flush
        if is_flush:
            return (6, *ranks)

        # 5. Straight
        if is_straight:
            return (5, straight_high)

        # 6. Three of a Kind
        if freq_groups[0][0] == -3:
            trip_rank = -freq_groups[0][1]
            kickers = [r for r in ranks if r != trip_rank]
            return (4, trip_rank, *sorted(kickers, reverse=True))

        # 7. Two Pair
        if freq_groups[0][0] == -2 and freq_groups[1][0] == -2:
            high_pair = -freq_groups[0][1]
            low_pair = -freq_groups[1][1]
            kicker = -freq_groups[2][1]
            return (3, high_pair, low_pair, kicker)

        # 8. One Pair
        if freq_groups[0][0] == -2:
            pair_rank = -freq_groups[0][1]
            kickers = [r for r in ranks if r != pair_rank]
            return (2, pair_rank, *sorted(kickers, reverse=True))

        # 9. High Card
        return (1, *ranks)

    # Evaluate all hands and sort descending
    scored = [(evaluate(h), h) for h in hands]
    scored.sort(reverse=True)

    best_score = scored[0][0]
    return [hand for score, hand in scored if score == best_score]