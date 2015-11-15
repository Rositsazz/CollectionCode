class Train:

    def __init__(self, number, from_destination, to_destination,
                 time_to_go, time_to_arrive):
        self.number = number
        self.from_destination = from_destination
        self.to_destination = to_destination
        self.time_to_go = time_to_go
        self.time_to_arrive = time_to_arrive

    def get_direction(self):
        return "from " + self.from_destination + " to " + self.to_destination

    def __str__(self):
        return "hey"

    def __call__(self):
        return 42

t = Train(6078, "Sofia", "Sliven", "16: 30", "21:11")
print(t)
print(t.get_direction())
