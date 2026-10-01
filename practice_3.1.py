def hill_climbing(values,start):
  current=start
  while True:
    neighbors=[]
    if current>0:
      neighbors.append(current-1)
    if current<len(values)-1:
      neighbors.append(current+1)

    best=current
    for n in neighbors:
      if values[n]>values[best]:
        best=n
    if best==current:
      break

    current=best
  return current

values=[1,3,5,8,6,4,2]
start=[0,2,4,6]

print("Бастапқы күй|Соңғы индекс|Соңғы күй")
for i in starts:
  res = hill_climbing(values1, s)
  print(f"{i:<16} | {res:<15} | {values1[res]}")
