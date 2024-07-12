from collections import deque
from time import time

class RateLimiter:
    def __init__(self, max_requests, time_window):
        self.max_requests = max_requests
        self.time_window = time_window / 1000.0  # Convert milliseconds to seconds
        self.clients = {}

    def isAllowed(self, clientID):
        current_time = time()
        if clientID not in self.clients:
            self.clients[clientID] = deque()

        request_times = self.clients[clientID]

        # Remove outdated requests
        while request_times and request_times[0] <= current_time - self.time_window:
            request_times.popleft()

        if len(request_times) < self.max_requests:
            request_times.append(current_time)
            return True
        else:
            return False

# Example usage:
rate_limiter = RateLimiter(max_requests=5, time_window=1000)  # 5 requests per 1000 milliseconds

# Simulate some requests
client_id = "client1"
for i in range(10):
    print(f"Request {i+1} allowed: {rate_limiter.isAllowed(client_id)}")
