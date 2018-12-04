import datetime
from operator import itemgetter

log = []

# Section 1
# Produce a sorted log
with open('input.txt') as f:
    for line in f:
        action_log = {}
        action_log['date'] = datetime.datetime.fromisoformat(line[1:17])
        if 'begins' in line:
            action_log['action'] = 'begin'
            action_log['guard_id'] = line[26:].strip(' begins shift\n')
        elif 'wakes' in line:
            action_log['action'] = 'wake'
        else:
            action_log['action'] = 'sleep'
        log.append(action_log)
log.sort(key=lambda x:x['date'])

# Add guard IDs to all log entries
for index, entry in enumerate(log):
    if entry['action'] == 'begin':
        # Populate the sleep and wake entries with the guard ID, up until the next shift begin
        for sub_index, sub_entry in enumerate(log[index + 1:]):
            if (sub_entry['action'] == 'wake') or (sub_entry['action'] == 'sleep'):
                log[sub_index + index + 1]['guard_id'] = entry['guard_id']
            else:
                break

# Find which guard slept the most
guard_tally = {}
for index, entry in enumerate(log):
    if entry['action'] == 'sleep':
        time_slept = log[index + 1]['date'] - entry['date']
        if entry['guard_id'] not in guard_tally:
            guard_tally[entry['guard_id']] = time_slept
        else:
            guard_tally[entry['guard_id']] += time_slept
sorted_guard_tally = sorted(guard_tally.items(), key=itemgetter(1), reverse=True)
sleepy_guard = sorted_guard_tally[0][0]
print(f'Guard {sleepy_guard} slept for {int(sorted_guard_tally[0][1].seconds/60)} minutes')

# Find which minute he was asleep for the most
minutes_log = []
for index, entry in enumerate(log):
    if (entry['guard_id'] == sleepy_guard) and (entry['action'] == 'sleep'):
        temp_log = [minute for minute in range(entry['date'].minute, log[index + 1]['date'].minute)]
        minutes_log.extend(temp_log)

# Now find the most frequent minute in the list
minute = max(set(minutes_log), key=minutes_log.count)
print(f'Guard {sleepy_guard} is most often asleep in minute {minute}')
answer = int(sleepy_guard) * minute
print(f'Your answer is {answer}')


# Part 2
minutes_log = {}
for index, entry in enumerate(log):
    if entry['action'] == 'sleep':
        if entry['guard_id'] not in minutes_log:
            minutes_log[entry['guard_id']] = []
        temp_log = [minute for minute in range(entry['date'].minute, log[index + 1]['date'].minute)]
        minutes_log[entry['guard_id']].extend(temp_log)

results = {}
for log in minutes_log.items():
    minute_most_slept = max(set(log[1]), key=log[1].count)
    results[log[0]] = {'minute_most_slept': minute_most_slept, 'count': log[1].count(minute_most_slept)}
sorted_results = sorted(results.items(), key=lambda x: x[1]['count'], reverse=True)
print(f"Guard {sorted_results[0][0]} slept the most on minute {sorted_results[0][1]['minute_most_slept']} for {sorted_results[0][1]['count']} minutes")
answer = int(sorted_results[0][0]) * sorted_results[0][1]['minute_most_slept']
print(f"Answer to part two is {answer}")