test = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]
test_q = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]
partipicants = {}
querys = {}
answer = []

for i in range(len(test)):
    partipicant = list(test[i].split(' '))
    partipicants[i] = partipicant

for i in range(len(test_q)):
    query = list(test_q[i].replace('and', '').split(' '))
    querys[i] = query

# print(test_q[0].replace("and", '').split(' '))
print(querys)
print(partipicants)
