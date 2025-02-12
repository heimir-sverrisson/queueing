"""
    Compute queue length for four servers
"""
from mmc import MMc


def sweep():
    arrival_rate = 400
    service_rate = 100
    num_servers = 4
    print("customers_in_system")
    for rate in range(1, arrival_rate):
        mmk = MMc(rate, service_rate, num_servers)
        customers = mmk.customers_in_system()
        print(f"{customers}")


if __name__ == "__main__":
    sweep()
