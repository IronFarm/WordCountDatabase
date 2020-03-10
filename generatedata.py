import datetime
import json
import random

all_words = ['brexit', 'coronavirus', 'boris', 'trump']

output = {}

start_date = datetime.date(2020, 2, 1)
# Generate data files for 5 days
for day in range(5):
    dt = start_date + datetime.timedelta(days=day)
    output = {}

    for word in all_words:
        # Generate a random integer beween 0 and 1000
        output[word] = random.randint(0, 1000)

    # Save the data file
    with open('{}.json'.format(dt), 'w', encoding='utf-8') as f:
        json.dump(output, f)
