weekday = {
    "mon":[[],[]],
    "tue":[[],[]],
    "wed":[[],[]],
    "thu":[[],[],[]],
    "fri":[[],[],[]],
    "sat":[[],[],[]],
    "sun":[[],[],[]],
    }

teamA = ["David", "Francis", "Sibiri", "Jasper", "Courage", "Bassey", "Magdalene"]
teamB = ["Esther", "Uzoma", "Grace", "Columbus", "James", "Augustina", "Yankson"]

for name in teamA:
         weekday["mon"][0].append(name)
         weekday["tue"][1].append(name)
         weekday["wed"][0].append(name)

for name in teamB:
         weekday["mon"][1].append(name)
         weekday["tue"][0].append(name)
         weekday["wed"][1].append(name)

print(weekday)
