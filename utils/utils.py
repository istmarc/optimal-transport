
# Discretisize a distribution
def discretize(s, M):
    S = s.size
    s_min = s.min()
    s_max = s.max()
    x = np.zeros(M)
    x_int = {}
    size = (s_max - s_min) / M
    sum_x = 0.0
    for i in range(M):
      a = s_min + i * size
      b = s_min + (i + 1) * size
      x_int[i] = (a, b)
      x[i] = 0.
      for k in range(S):
        if s[k] >= a and s[k] < b:
          x[i] += 1
      sum_x += x[i]
    for i in range(M):
      x[i] /= sum_x
    return x, x_int

# Generate a gaussian
def generate_gaussian(n):
  #s = np.random.randn(n)
  #s.sort()
  #cdfs = stats.norm.pdf(s)
  x,_ = discretize(s, n)
  return x

## Generate a double gaussian
def generate_dgaussian(N, S = 10000):
  y = np.zeros(N)
  s = np.random.randn(S)
  y_dist, _ = discretize(s, N//2)
  for i in range(N//2):
    y[i] = y_dist[i]
    y[i + N//2] = y_dist[i]
  y = y / y.sum()
  return y

