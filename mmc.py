"""
    Computations for a M/M/c queue
        see: https://en.wikipedia.org/wiki/M/M/c_queue
"""
import math


class MMc:
    def __init__(self, arrival_rate, service_rate, num_servers):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.num_servers = num_servers

    def _calculate_erlang_c(self):
        factor_1 = 0
        for k in range(self.num_servers):
            factor_1 += (self.num_servers * self.utilization) ** k / \
                         math.factorial(k)
        factor_2 = math.factorial(self.num_servers) / (
            (self.num_servers * self.utilization) ** self.num_servers)
        factor_3 = 1 - self.utilization
        return 1 / (1 + factor_1 * factor_2 * factor_3)

    def _validate(self):
        self.utilization = self.arrival_rate / (
            self.service_rate * self.num_servers)
        if self.utilization > 1:
            raise ValueError("The system is unstable")
        self.erlang_c = self._calculate_erlang_c()

    def response_time(self):
        self._validate()
        return (
            self.erlang_c / (
                self.service_rate * self.num_servers - self.arrival_rate)
            + 1 / self.service_rate
        )

    def customers_in_system(self):
        # Being served and waiting in queue
        self._validate()
        factor_1 = self.utilization / (1 - self.utilization)
        return factor_1 * self.erlang_c + self.num_servers * self.utilization

