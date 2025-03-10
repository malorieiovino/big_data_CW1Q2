import matplotlib.pyplot as plt

# K values and corresponding SSE values from your data
K_values = [5, 10, 15, 20]
SSE_values = [258710, 431288, 578497, 628358]  # Your real values

plt.figure(figsize=(8, 5))
plt.plot(K_values, SSE_values, marker='o', linestyle='-')
plt.xlabel("Number of Clusters (K)")
plt.ylabel("Sum of Squared Errors (SSE)")
plt.title("Elbow Method for Optimal K")
plt.grid()
plt.show()

