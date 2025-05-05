def evaluate_solution(solution, items, capacity):
    total_weight = 0
    total_value = 0

    for included, item in zip(solution, items):
        if included:
            total_weight += item.weight
            total_value += item.value

    if total_weight > capacity:
        return 0  # ou penalização
    return total_value
