
# 1. Calculate the total revenue generated y two product categories in a store.

'''Input 
category1_revenue=np.array([500,600,700,500])
category2_revenue=np.array([450,700,800,600])'''

import numpy as np

category1_revenue = np.array([500, 600, 700, 500])
category2_revenue = np.array([450, 700, 800, 600])

# Calculate the total revenue for each day
total_revenue_per_day = category1_revenue + category2_revenue

# Calculate the total revenue for all days
total_revenue = np.sum(total_revenue_per_day)

print("Total revenue for each day:", total_revenue_per_day)
print("Total revenue for all days:", total_revenue)



# 2. Calculate the profit made by a company.

revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])

# Calculate profit for each period
profit_per_period = revenue - expenses

# Calculate total profit
total_profit = np.sum(profit_per_period)

print("Profit for each period:", profit_per_period)
print("Total profit:", total_profit)
