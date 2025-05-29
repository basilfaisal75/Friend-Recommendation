class Recommended:
    def __init__(self, social_NW):
     self.social_NW = social_NW

    def get_common_friend_count(self):
        common_friends = {}
        for user1 in self.social_NW:
            common_friends[user1] = {}
            for user2 in self.social_NW:
                if user1 == user2:
                    continue
                common_friends[user1][user2] = len(set(self.social_NW[user1]).intersection(self.social_NW[user2]))
        return common_friends

    def recommend_friend(self, common_friends, m_name):
        if m_name not in self.social_NW:
            return None
        m_friends = common_friends[m_name]
        recommended_friend = max(m_friends, key=m_friends.get)
        if m_name == recommended_friend or recommended_friend in self.social_NW[m_name]:
            return None
        else:
            return recommended_friend


social_NW = {
    "basil": ["khadija", "dylan"],
    "khadija": ["basil", "dylan"],
    "dylan": ["basil", "khadija"],
    "kevork": ['engjull,basil'],
    "engjull": ['dylan','basil'],
}

network = Recommended(social_NW)
common_friends = network.get_common_friend_count()

while True:
    m_name = input("Enter a member name or ID: ")
    recommended_friend = network.recommend_friend(common_friends, m_name)
    if recommended_friend:
        print(f"Recommended friend for {m_name} is {recommended_friend}")
        break
    else:
        if m_name not in social_NW:
            choice = input(f"This member does not exist. Would you like to try again? (yes/no): ")
            if choice.lower() == "yes":
                continue
            else:
                break
        else:
            print(f"No friend recommendation for {m_name}.")
            break
