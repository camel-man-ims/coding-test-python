changed_id = ".qdqw...."

for i in range(len(changed_id) - 1):
    print("len(changed_id) = " + str(len(changed_id)))
    print(i)
    if i!=len(changed_id)-1 and changed_id[i] == '.' and changed_id[i + 1] == '.':
        changed_id = changed_id[:i] + changed_id[i + 1:]
    else:
        changed_id = changed_id

print(changed_id)

