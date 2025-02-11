import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv('add.csv')

# Plot the data
plt.plot(data)
plt.xlabel('Arrival Rate')
plt.ylabel('Response Time')
plt.title('Response Time vs Arrival Rate')
plt.legend(['1 server', '4 servers'])
# plt.show()
plt.savefig('add.png', dpi=300)
