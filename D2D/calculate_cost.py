import json

# Load the cost data
with open('cost.json', 'r') as f:
    cost_data = json.load(f)

# Load the channel usage data
with open('channel-cost.json', 'r') as f:
    channel_data = json.load(f)

# Calculate the total cost per day across different channels
total_cost_per_day = {}
for data in channel_data:
    date = data['date'].split(' ')[0]
    if date not in total_cost_per_day:
        total_cost_per_day[date] = {k: 0 for k in cost_data}
    for channel, count in data.items():
        if channel != 'date':
            total_cost = count * cost_data[channel]
            total_cost_per_day[date][channel] += total_cost

# Round the total cost values to 2 decimal places
for date, data in total_cost_per_day.items():
    for channel, total_cost in data.items():
        total_cost_per_day[date][channel] = round(total_cost, 2)

# Output the total cost per day across different channels as a json file
with open('total-cost.json', 'w') as f:
    json.dump(total_cost_per_day, f)

