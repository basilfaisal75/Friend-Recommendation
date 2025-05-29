class Database:
    def __init__(self):
        self._nw = {}  # Initialize the social network dictionary
        self._file_path = ''  # Store the file path

    def open_file(self):
        my_file = input("What file would you like to open? ")
        while my_file != 'nw1.txt':
            my_file = input('Sorry, this file does not exist. Please try again or type "done" to quit: ')
            if my_file == 'done':
                print("Quitting...")
                exit()
        self._file_path = my_file
        print('This file will now be opened')
        try:
            with open(my_file, 'r') as file:
                num_members = int(file.readline().strip())  # Read the number of members from the first line
                names = [name.strip() for name in file.readlines()[:num_members]]  # Read the member names

                for name in names:
                    self._nw[name] = []  # Initialize an empty list of friends for each member

                file.seek(0)
                next(file)

                for line in file:
                    line = line.strip()
                    if line:
                        person, *friends = [name.strip() for name in line.split(',')]
                        self._nw[person] = friends  # Update the friend list for each member

                if len(names) < num_members:
                    raise Exception("Error: There are fewer names in the data than the number of members specified.")
                elif len(names) > num_members:
                    raise Exception("Error: There are more names in the data than the number of members specified.")

                display_network = input("Do you want to display the social network? (yes/no) ")
                if display_network.lower() == "yes":
                    self.display_network()

        except FileNotFoundError:
            print("File not found.")
        except Exception as e:
            print("Error:", str(e))

    def display_network(self):
        print("The current social network:")
        printed_friendships = set()
        for person, friends in self._nw.items():
            if friends:
                for friend in friends:
                    if (person, friend) not in printed_friendships and (friend, person) not in printed_friendships:
                        print(f"{person} is friends with {friend}")
                        printed_friendships.add((person, friend))
            else:
                print(f"{person} is friends with none")

    def delete_member(self, member):
        if member in self._nw:
            del self._nw[member]  # Remove the member from the network dictionary
            for friends in self._nw.values():
                if member in friends:
                    friends.remove(member)  # Remove the member from the friend lists

            print(f"{member} has been deleted from the social network.")

            # Update the text file
            num_members = len(self._nw)
            with open(self._file_path, 'w') as file:
                file.write(str(num_members) + '\n')
                for member, friends in self._nw.items():
                    line = member + ',' + ','.join(friends) + '\n'
                    file.write(line)

        else:
            print(f"{member} is not found in the social network.")


class SocialNetworkAnalyzer(Database):
    def __init__(self):
        super().__init__()

    def get_friend_group_sizes(self):
        group = input("Would you like to see the size of the friend groups? (yes/no) ")
        if group.lower() == "yes":
            group_sizes = {}
            group_shapes = {
                1: "singleton",
                2: "pair",
                3: "triangle or tripod",
                4: "polygon",
                # Add more shapes as needed
            }

            for friends in self._nw.values():
                group_sizes[len(friends) + 1] = group_sizes.get(len(friends) + 1, 0) + 1

            print("The size of friend groups:")
            for size in range(1, 6):
                count = group_sizes.get(size, 0)
                shape = group_shapes.get(size, "")
                print(f"Number of groups with {size} member(s): {count} ({shape})")
        else:
            print("The friend groups will not be shown")
            exit()

class FriendStatistics(Database):
    def __init__(self):
        super().__init__()

    def display_average_friends(self):
        total_friends = sum(len(friends) for friends in self._nw.values())
        total_members = len(self._nw)
        average_friends = total_friends / total_members

        print(f"The average number of friends in the social network: {average_friends}")


DB = SocialNetworkAnalyzer()
DB.open_file()
DB.get_friend_group_sizes()

