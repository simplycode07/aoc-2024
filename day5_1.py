with open("input.txt") as file:
    raw_data = file.readlines()


page_ordering_rule = {}
updates = []

ordering_rules_done = False

for line in raw_data:
    if line == "\n":
        ordering_rules_done = True
        continue

    if not ordering_rules_done:
        if page_ordering_rule.get(line.split("|")[0]):
            page_ordering_rule[line.split("|")[0]].append(line.split("|")[1].strip())
        else:
            page_ordering_rule[line.split("|")[0]] = [line.split("|")[1].strip()]
        # page_ordering_rule.append(line.strip())
    else:
        updates.append(line.strip().split(","))


# print(page_ordering_rule)
# print(updates)

res = 0
for update in updates:
    # visited = {m:False for m in page_ordering_rule.keys()}
    visited = []
    update_ordered = True
    for page in update:
        visited.append(page)
        for num_before_page in page_ordering_rule.get(page, []):
            if num_before_page in visited:
                update_ordered = False


    if update_ordered:
        res += int(update[len(update)//2])
        print(int(update[len(update)//2]))
    # print(f"{update}: {update_ordered}")

print(res)

