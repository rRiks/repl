def a(g):
  for i in range(len(g)):
        if g[i] % 5 >2 and g[i] >37:
            g[i] += 5-(g[i] % 5)
  return g

g = [73,67,38,33]