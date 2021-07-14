import heapq
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph_price = defaultdict(list)
        queue = [(0, k+1, src)]
        visited = [0] * n #To avoid Loop
        #No need to maintain best Cost since Dijkstra (priority queue) already to it for us

        for start, end, d in flights:
            graph_price[start].append((end, d))

        while queue:
            curr_price, steps, current_stop = heapq.heappop(queue)
            if current_stop == dst:
                return curr_price

            if visited[current_stop] >= steps:
                continue

            visited[current_stop] = steps

            for neighbor_destination, next_price in graph_price[current_stop]:
                heapq.heappush(queue, (curr_price + next_price, steps - 1, neighbor_destination))

        return -1
