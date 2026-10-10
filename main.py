# Smart Energy Monitor

consumption = [8.2, 7.5, 9.1, 6.8, 10.2, 12.5, 11.4]

days =  ["Monday","Tuesday","Wednesday","Thusday","Friday","Saturday","Sunday"]
average = sum(consumption) / len(consumption)
maximum = max(consumption)
minimum = min(consumption)
max_index = consumption.index(maximum)
max_day = days[max_index]

print("Highest consumption day:", max_day)

print("SMART ENERGY MONITOR")
print("--------------------")

print("Daily consumption:", consumption)
print("Average consumption:", round(average, 2), "kWh")
print("Maximum consumption:", maximum, "kWh")
print("Minimum consumption:", minimum, "kWh")
if average > 10:
    print("Energy consumption is high!")
else:
    print("Energy consumption is normal.")
print("\n===== ENERGY REPORT =====")

print("Number of days:", len(consumption))
print("Total consumption:", round(sum(consumption), 2), "kWh")
print("Average consumption:", round(average, 2), "kWh")
print("Highest consumption:", maximum, "kWh")
print("Lowest consumption:", minimum, "kWh")
print("Highest consumption day:", max_day)
import matplotlib.pyplot as plt

plt.plot(days, consumption, marker="o")

plt.title("Weekly Energy Consumption")
plt.xlabel("Days")
plt.ylabel("Consumption (kWh)")

plt.grid(True)
plt.tight_layout()
plt.show()
# Simple Energy Prediction

last_days = consumption[-3:]

predicted_consumption = sum(last_days) / len(last_days)

print("\n===== ENERGY PREDICTION =====")
print("Last 3 days:", last_days)
print("Predicted consumption for tomorrow:",
      round(predicted_consumption, 2), "kWh")
# Energy Consumption Classification

print("\n===== ENERGY CLASSIFICATION =====")

for i in range(len(consumption)):

    if consumption[i] < 8:
        status = "Low"

    elif consumption[i] <= 12:
        status = "Normal"

    else:
        status = "High"

    print(days[i], ":", consumption[i], "kWh -", status)
# High Consumption Analysis

print("\n===== HIGH CONSUMPTION ANALYSIS =====")

threshold = 10
high_days = []

for i in range(len(consumption)):
    if consumption[i] > threshold:
        high_days.append(days[i])

print("Consumption threshold:", threshold, "kWh")
print("Number of high consumption days:", len(high_days))
print("High consumption days:", high_days)