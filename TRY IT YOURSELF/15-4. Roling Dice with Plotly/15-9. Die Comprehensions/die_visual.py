from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and store results in a list.
results = [die.roll() for roll_num in range(1000)]

# Analyze the results.
frequencies = [results.count(value) for value in range (1, die.num_sides+1)]

# Visualize the results.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(
    title='Results of rolling one D6 1000 times',
    xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='TRY IT YOURSELF/results/d6.html')