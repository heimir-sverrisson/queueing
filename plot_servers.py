import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv('servers.csv')
df = pd.DataFrame(data)

# Plot the data
plt.plot(df)
plt.xlabel('Arrival Rate')
plt.ylabel('Response Time')
plt.title('Response Time vs Arrival Rate')
plt.legend(['1 server', '2 servers', '4 servers', '8 servers'])
# plt.show()
plt.savefig('servers.png', dpi=300)
