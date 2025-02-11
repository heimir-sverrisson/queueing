"""
    Compare 1, and 4 servers
"""
from mmc import MMc


def sweep():
    arrival_rate = 400
    service_rate = 100
    print("1 server,4 servers")
    for rate in range(1, arrival_rate):
        server_response_times = []
        for num_servers in [1, 4]:
            if num_servers == 1 and rate >= service_rate:
                server_response_times.append(None)
            else:
                mmk = MMc(rate, service_rate, num_servers)
                response_time = mmk.response_time()
                server_response_times.append(response_time)
        if server_response_times[0]:
            print(",".join(str(100 * x) for x in server_response_times))
        else:
            print(f",{100 * server_response_times[1]}")


if __name__ == "__main__":
    sweep()
