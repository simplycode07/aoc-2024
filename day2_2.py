with open("input.txt") as file:
    reports_raw = file.readlines()

reports = []

for i, report in enumerate(reports_raw):
    reports.append([])
    for data in report.split():
        reports[i].append(int(data))

def is_safe(report):
    increasing = report[0] < report[1] 
    for i in range(len(report) - 1):
        if ((increasing and report[i] < report[i+1]) or (not increasing and report[i] > report[i+1])) and 1 <= abs(report[i] - report[i+1]) <= 3:
            continue
        else:
            return False, i

    return True, 0

safe = 0

for i, report in enumerate(reports):
    safety, bad_level = is_safe(report)
    if safety:
        safe += 1
    else:
        # try removing elements around the bad level
        for j in range(-1, 2):
            if is_safe(report[:bad_level + j] + report[bad_level + 1 + j:])[0]:
                safe += 1
                break

print(safe)

