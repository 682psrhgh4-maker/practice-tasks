# 1. Ойын ағашы мен терминалдық мәндерді сақтау.
tree = {
    "A": ["B", "C"],
    "B": ["D", "E"], "C": ["F", "G"],
    "D": ["H", "I"], "E": ["J", "K"],
    "F": ["L", "M"], "G": ["N", "O"]
}
payoffs = {
    "H": 4, "I": 9, "J": 7, "K": 2,
    "L": 3, "M": 8, "N": 6, "O": 1
}

# 2. Дәрістегі көмекші функциялар.
def is_terminal(state):
    return state in payoffs


def successors(state, reverse=False):
    children = tree[state]
    return list(reversed(children)) if reverse else children


def utility(state):
    return payoffs[state]


# 3. Minimax: MAX және MIN кезектесіп рекурсивті шақырылады.
def minimax(state, maximizing, counter, reverse=False):
    counter[0] += 1  # Count every call, including terminal nodes.
    if is_terminal(state):
        return utility(state)

    if maximizing:
        value = float("-inf")
        for child in successors(state, reverse):
            child_value = minimax(child, False, counter, reverse)
            value = max(value, child_value)
        return value
    else:
        value = float("inf")
        for child in successors(state, reverse):
            child_value = minimax(child, True, counter, reverse)
            value = min(value, child_value)
        return value


# 4. Alpha-Beta: alpha >= beta болса, қалған балаларды қию.
def alphabeta(state, alpha, beta, maximizing, counter,
              visited, pruned, reverse=False):
    counter[0] += 1
    visited.append(state)
    if is_terminal(state):
        return utility(state)

    children = successors(state, reverse)
    if maximizing:
        value = float("-inf")
        for index, child in enumerate(children):
            child_value = alphabeta(
                child, alpha, beta, False, counter,
                visited, pruned, reverse
            )
            value = max(value, child_value)
            alpha = max(alpha, value)
            if alpha >= beta:
                # Only children not explored are marked as pruned.
                pruned.extend(children[index + 1:])
                break
        return value
    else:
        value = float("inf")
        for index, child in enumerate(children):
            child_value = alphabeta(
                child, alpha, beta, True, counter,
                visited, pruned, reverse
            )
            value = min(value, child_value)
            beta = min(beta, value)
            if alpha >= beta:
                pruned.extend(children[index + 1:])
                break
        return value


# 5. Негізгі бағдарлама: екі өту ретін де орындау.
def main():
    for reverse in (False, True):
        order = "right-to-left" if reverse else "left-to-right"
        mm_calls = [0]
        ab_calls = [0]
        visited = []
        pruned = []

        mm_value = minimax("A", True, mm_calls, reverse)
        ab_value = alphabeta(
            "A", float("-inf"), float("inf"), True,
            ab_calls, visited, pruned, reverse
        )

        print("\nTraversal:", order)
        print("Minimax root:", mm_value, "calls:", mm_calls[0])
        print("Alpha-Beta root:", ab_value, "calls:", ab_calls[0])
        print("Alpha-Beta visited:", " -> ".join(visited))
        print("Pruned leaves:", pruned if pruned else "none")
        assert mm_value == ab_value


if __name__ == "__main__":
    main()
