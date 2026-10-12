from tools import Decorations, StringTools


class Balance:
    def __init__(self, target, users):
        self.target = target
        self.users = []

        self.maxs = []
        self.mins = []

        [self.add_user(user) for user in users]

    def add_user(self, user):
        assert user.max >= user.min, "Error: User max must be greater than User min."

        self.maxs.append(user.max)
        self.mins.append(user.min)

        self.users.append(user)

    def pop_user(self, user=None):
        user = self.users[-1] if user is None else user

        assert user in self.users, "Error: User does not exist in Balance. Cannot remove."
        user_index = self.users.index(user)

        self.maxs.pop(user_index)
        self.mins.pop(user_index)

        self.users.pop(user_index)

    def __str__(self):
        return f"Balance(target=${self.target}, users={[user.__str__() for user in self.users]})"

    def giving(self):
        maxs_sum = sum(self.maxs)
        mins_sum = sum(self.mins)
        diff_sum = maxs_sum - mins_sum
        fairshare = (self.target - mins_sum) / (diff_sum)

        min_min = min(self.mins)
        max_max = max(self.maxs)

        bar_length = 80
        bar_start = min_min
        bar_end = max(max_max, self.target)

        print("Target (T):    ", "$"+str(self.target))
        print("Fairshare (F): ", str(round(fairshare * 100, 2))+"%")
        print(Decorations.DIVIDER)

        if self.target > maxs_sum:
            print(
                f"Error: Target (${self.target}) unreachable "
                f"(possible max ${maxs_sum}).")
        elif self.target < mins_sum:
            print(
                f"Error: Target (${self.target}) will always overshoot "
                f"(possible minimum ${mins_sum})."
            )
        else:
            for user in self.users:

                prefix = (user.min - bar_start)
                prefix = (prefix / bar_end)
                prefix = round(prefix * bar_length)

                infix = (user.max - user.min)
                infix = (infix / bar_end)
                infix = round(infix * bar_length)

                postfix = (bar_end - user.max)
                postfix = (postfix / bar_end)
                postfix = round(postfix * bar_length)

                infix = infix + (bar_length - prefix - infix - postfix)
                
                bar = prefix * "-" + infix * "|" + postfix * "-"

                fairshare_tag_index = round(prefix + (fairshare * infix))
                bar = StringTools.replace(bar, fairshare_tag_index, "F")

                bar = "[" + bar + "]"

                print(bar, "$"+str(round(user.min + (fairshare * (user.max - user.min)), 2)))

        print(Decorations.DIVIDER)



class Person:
    def __init__(self, _max, _min=0):
        assert _max > _min, "Error: Max must be greater than Min."

        self.max = _max
        self.min = _min

    def __str__(self):
        return f"Person(Max=${self.max}, Min=${self.min})"


if __name__ == "__main__":
    balance = Balance(35, [Person(30, 15), Person(20, 10), Person(7, 5)])
    balance.giving()