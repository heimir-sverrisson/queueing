"""
    Compare the shape of the response curves of 1, 2, 4, and 8 servers
"""
from mmc import MMc


def sweep():
    arrival_rate = 100
    print("1 server,2 servers,4 servers,8 servers")
    for rate in range(1, arrival_rate):
        server_response_times = []
        for num_servers in [1, 2, 4, 8]:
            mmk = MMc(num_servers * rate, arrival_rate, num_servers)
            response_time = mmk.response_time()
            server_response_times.append(response_time)
        print(",".join(str(arrival_rate * x) for x in server_response_times))


if __name__ == "__main__":
    sweep()
