class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src: [] for src, dst in tickets}

        for src, dst in tickets:
            adj[src].append(dst)

        for src in adj:
            adj[src].sort(reverse=True)

        res = []

        def dfs(src):
            while src in adj and adj[src]:
                v = adj[src].pop()
                dfs(v)

            res.append(src)

        dfs("JFK")
        return res[::-1]