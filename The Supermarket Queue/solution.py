def queue_time(customers, tills):
    if not customers:
        return 0

    if len(customers) <= tills:
        return max(customers)

    tills_list = [0] * tills

    for customer in customers:
        tills_list[tills_list.index(min(tills_list))] += customer

    return max(tills_list)
