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

def check_update(update):
    visited = []
    for page in update:
        visited.append(page)
        for num_before_page in page_ordering_rule.get(page, []):
            if num_before_page in visited:
                # print(f"faulty page: {num_before_page}, {page}, {update}")
                return False, num_before_page, page

    return True, "", ""


incorrectly_ordered = []
res = 0
i = 0
was_faulty = False
while i < len(updates):
    update = updates[i]
    faulty, page1, page2 = check_update(update)

    if not faulty:
        was_faulty = True
        page1_index = update.index(page1)
        page2_index = update.index(page2)

        temp = update[page1_index]
        update[page1_index] = update[page2_index]
        update[page2_index] = temp

    else:
        if was_faulty:
            print(update, i, int(update[len(update)//2]))
            res += int(update[len(update)//2])
        # print()
        i += 1
        was_faulty = False


print(res)
