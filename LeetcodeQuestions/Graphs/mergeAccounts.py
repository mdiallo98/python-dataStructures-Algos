class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        graph = defaultdict(set)
        email_accounts = {}
