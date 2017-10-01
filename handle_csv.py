import csv
import datetime

PROBLEM_HASHTAG = '#косяк'
GOAL_DAY_HASHTAG = '#цельнадень'
GOAL_WEEK_HASHTAG = '#цельнанеделю'
N = 200

today = datetime.date.today()
today_str = str(today)
filename = "backups/TickTick-backup-{}.csv".format(today)
date_format = '%Y-%m-%dT%X%z'

# Delete unused info
f = open(filename, 'r+')
lines = f.readlines()
if lines[0].find('''"Date:''') > -1:
    lines = lines[6:]
    print('find')

f.close()

new_f = open(filename, 'w')
new_f.writelines(lines)
new_f.close()

# Open it's as csv
f = open(filename, 'r+')
csvreader = csv.reader(f, delimiter=',', quotechar='"')
fieldnames = next(csvreader)

completed = []
uncompleted = []
problems = []
goals_on_day = []
goals_on_week = []
csvdictreader = csv.DictReader(f, fieldnames=fieldnames)
for l in csvdictreader:
    status = l['Status'].strip()
    completed_time = l['Completed Time'].strip()
    order = int(l['Order'].strip())
    start_date = l['Start Date'].strip()
    title = l['Title'].strip()

    # Completed
    if completed_time.startswith(today_str) and status == '2':
        completed.append(l)
    elif title.find(PROBLEM_HASHTAG) >= 0 and status == '0':
        problems.append(l)
    elif title.find(GOAL_DAY_HASHTAG) >= 0:
        goals_on_day.append(l)
    elif title.find(GOAL_WEEK_HASHTAG) >= 0:
        goals_on_week.append(l)
    # UnCompleted
    elif status == '0' and len(start_date) > 0:
        start_date = datetime.datetime.strptime(start_date, date_format).date()
        if start_date <= today:
            uncompleted.append(l)

uncompleted = sorted(uncompleted, key=lambda x: x['Priority'], reverse=True)
completed = sorted(completed, key=lambda x: x['Priority'], reverse=True)
# output_dict = {'completed': completed, 'uncompleted': uncompleted, 'problems': problems, 'goals': goals}


first_date = today - datetime.timedelta(days=today.weekday())
last_date = first_date + datetime.timedelta(days=6)
sum_filename = "summaries/Summary_of_week_{}-{}.csv".format(first_date, last_date)

output = []
for i in range(N):
    tmp = [''] * N
    output.append(tmp)

sum_file = open(sum_filename, 'w')
csv_writer = csv.writer(sum_file)

output[0][0] = 'Цель на неделю'
output[0][1] = 'Цель на день'
output[0][2] = 'Косяки'
for i, goal in enumerate(goals_on_week):
    output[i + 1][0] = goal['Title']

for i, goal in enumerate(goals_on_day):
    output[i + 1][1] = goal['Title']

for i, pr in enumerate(problems):
    output[i + 1][2] = pr['Title']

task_col = 4
output[0][task_col] = 'Выполненные задачи'
output[0][task_col + 1] = 'Их приоритеты'
output[0][task_col + 2] = 'Невыполненные задачи'
output[0][task_col + 3] = 'Их приоритеты'

for i, c in enumerate(completed):
    output[i + 1][task_col] = c['Title']
    output[i + 1][task_col + 1] = c['Priority']

for i, uc in enumerate(uncompleted):
    output[i + 1][task_col + 2] = uc['Title']
    output[i + 1][task_col + 3] = uc['Priority']

retro_row = max(len(problems), max(len(goals_on_day), len(goals_on_week))) + 2
output[retro_row][0] = '+'
output[retro_row][1] = '-'
output[retro_row][2] = 'Ретро'

for i in range(N):
    csv_writer.writerow(output[i])
