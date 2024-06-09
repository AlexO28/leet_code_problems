# Given a list of accounts where each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.
# Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some common email to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.
# After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        if len(accounts) == 1:
            emails = list(set(accounts[0][1:]))
            emails.sort()
            res = [accounts[0][0]]
            res.extend(emails)
            return res
        merged_accounts = [accounts[0]]
        for j in range(1, len(accounts)):
            intersection_inds = []
            for i in range(len(merged_accounts)):
                intersection = [elem for elem in accounts[j][1:] if elem in merged_accounts[i][1:]]
                if len(intersection) > 0:
                    intersection_inds.append(i)
            if len(intersection_inds) == 0:
                merged_accounts.append(accounts[j])
            else:
                res_accounts = []
                new_account = accounts[j]
                for i in range(len(merged_accounts)):
                    if i in intersection_inds:
                        new_account.extend(merged_accounts[i][1:])
                    else:
                        res_accounts.append(merged_accounts[i])
                emails = list(set(new_account[1:]))
                res_account = [new_account[0]]
                res_account.extend(emails)
                res_accounts.append(res_account)
                merged_accounts = res_accounts
        for i in range(len(merged_accounts)):
            emails = list(set(merged_accounts[i][1:]))
            emails.sort()
            res = [merged_accounts[i][0]]
            res.extend(emails)
            merged_accounts[i] = res
        return merged_accounts
