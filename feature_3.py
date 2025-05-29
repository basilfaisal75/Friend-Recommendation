# Class to represent a social network
class SocialNetwork:
    # Constructor to initialize the network data
    def __init__(self, network_data):
        # Dictionary to store the network relationships
        self.network = {}
        # Validate the input data
        self.validate_input(network_data)
        # Create the network
        self.create_network(network_data)
        # Dictionary to store indirect relationships
        self.indirect_friends = {}
        # Find indirect relationships
        self.find_indirect_relationships()

    # Method to validate the input data
    def validate_input(self, network_data):
        for member, friends in network_data.items():
            for friend in friends:
                if friend not in network_data:
                    raise ValueError(f"{friend} does not exist in the network")
                # Check if friend exists in network_data, if so check for mutual friendship
                elif member not in network_data[friend]:
                    if friend in network_data:
                        network_data[friend].append(member)

    # Method to create the network
    def create_network(self, network_data):
        for member, friends in network_data.items():
            self.network[member] = friends

    # Method to display number of friends of a member
    def display_number_of_friends(self, member):
        if member in self.network:
            print(f"{member} has {len(self.network[member])} friends")
        else:
            print(f"{member} does not exist in the network")

    # Method to show the members with the least number of friends
    def show_least_friends(self):
        # Initialize the least number of friends to a high value
        least_friends = float("inf")
        # List to store members with the least friends
        members_least_friends = []
        # List to store members with no friends
        no_friends = []
        # Ask the user if they want to see the members with least friends
        ask = input("would you like to view the members with the least amount of friends y/n?")
        if ask == "y":
            for member, friends in self.network.items():
                if not friends:
                    no_friends.append(member)
                elif len(friends) < least_friends:
                    least_friends = len(friends)
                    members_least_friends = [member]
                elif len(friends) == least_friends:
                    members_least_friends.append(member)
        # Print the results
        print("Members with the least number of friends:", members_least_friends)
        print("Members with no friends:", no_friends)

    # Method to show relationships of a member
    def show_relationships(self, member):
        if member in self.network:
            print(f"{member} is connected with:", self.network[member])
        else:
            print(f"{member} does not exist in the network")

    # Method to find indirect relationships
    def find_indirect_relationships(self):
        for member, friends in self.network.items():
            indirect = set()
            for friend in friends:
                indirect -= set(friends + [member])
                self.indirect_friends[member] = list(indirect)

    def display_indirect_friends(self):
        print("Indirect friends:")
        for member, indirect in self.indirect_friends.items():
            print(f"{member} -> {indirect}")


network = {
    "basil": ["khadija", "dylan"],
    "khadija": ["basil", "dylan"],
    "dylan": ["basil",],

}

sn = SocialNetwork(network)
sn.display_number_of_friends("basil")
sn.show_least_friends()
sn.show_relationships("basil")
sn.display_indirect_friends()
