class UnionFind:

    def __init__(self, n):
        self.parent = []
        self.rank = []
        for i in range(1, n + 1):
            #  at first every node will be a parent of itself
            self.parent[i] = i
            #  at first every node will have a rank of zero
            self.rank[i] = 0

    #  the union find data structures has a find and union method, the first helps find the ultimate parent of a node as while as apply path compression to improve the time complexity of future find operations. The union method unites the two nodes by first find the ultimae parents

    def find(self, node):
