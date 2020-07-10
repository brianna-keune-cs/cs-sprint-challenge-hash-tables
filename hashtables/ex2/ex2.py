#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    route = []
    cache = {ticket.source: ticket.destination for ticket in tickets}

    next_destination = cache["NONE"]
    while next_destination is not "NONE":
        route.append(next_destination)
        next_destination = cache[next_destination]

    # this is for the tests, according to the read me example
    # the source that has a destination for "NONE"
    # is not suppose to be included in the route order.
    route.append("NONE")
    return route
