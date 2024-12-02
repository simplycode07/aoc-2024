with open("input.txt") as file:
    reports_raw = file.readlines()

reports = []

for i, report in enumerate(reports_raw):
    reports.append([])
    for data in report.split():
        reports[i].append(int(data))


safe = 0

for report in reports:
    increasing = report[0] < report[1] 
    for i in range(len(report) - 1):
        if ((increasing and report[i] < report[i+1]) or (not increasing and report[i] > report[i+1])) and 1 <= abs(report[i] - report[i+1]) <= 3:
            continue
        else:
            # print("unsafe", report)
            break
    else:
        safe += 1

print(safe)

