import matplotlib.pyplot as plt
import numpy as np

# K values
k_values = [5, 10, 15, 20]

# Cosine Distance SSE values
cosine_sse = [3451.77, 3335.14, 3456.74, 3223.99]

# Manhattan Distance SSE values
manhattan_sse = [9.73478e+11, 9.76947e+11, 7.31981e+11, 7.71046e+11]

# Euclidean Distance SSE values
euclidean_sse = [1.57e+08, 1.37e+08, 1.37e+08, 1.35e+08]

def create_elbow_plot(k_values, sse_values, title, filename, color='blue'):
    plt.figure(figsize=(10, 6))
    
    # Plot SSE values
    plt.plot(k_values, sse_values, 'o-', color=color, linewidth=2, markersize=8)
    
    # Add data point labels
    for i, txt in enumerate(sse_values):
        plt.annotate(f"{txt:.2e}", (k_values[i], sse_values[i]), 
                    textcoords="offset points", xytext=(0,10), ha='center')
    
    # Mark the optimal K point
    optimal_idx = np.argmin(sse_values)
    plt.scatter(k_values[optimal_idx], sse_values[optimal_idx], 
                color='red', s=100, zorder=5)
    plt.annotate(f"K={k_values[optimal_idx]}", 
                (k_values[optimal_idx], sse_values[optimal_idx]),
                xytext=(20, -20), textcoords="offset points",
                arrowprops=dict(arrowstyle='->'))
    
    # Formatting
    plt.title(title, fontsize=16)
    plt.xlabel('Number of Clusters (K)', fontsize=14)
    plt.ylabel('Sum of Squared Errors (SSE)', fontsize=14)
    plt.xticks(k_values)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    plt.tight_layout()
    plt.savefig(f'../images/{filename}', dpi=300, bbox_inches='tight')
    plt.close()

# Generate individual distance measure plots
create_elbow_plot(k_values, cosine_sse, 
                  'Elbow Method - Cosine Distance', 
                  'cosine_elbow.png', 'blue')

create_elbow_plot(k_values, manhattan_sse, 
                  'Elbow Method - Manhattan Distance', 
                  'manhattan_elbow.png', 'green')

create_elbow_plot(k_values, euclidean_sse, 
                  'Elbow Method - Euclidean Distance', 
                  'euclidean_elbow.png', 'red')

# Comparative normalized plot
plt.figure(figsize=(12, 8))

# Normalize SSE values
cosine_norm = np.array(cosine_sse) / max(cosine_sse)
manhattan_norm = np.array(manhattan_sse) / max(manhattan_sse)
euclidean_norm = np.array(euclidean_sse) / max(euclidean_sse)

plt.plot(k_values, cosine_norm, 'o-', label='Cosine', linewidth=2, markersize=8)
plt.plot(k_values, manhattan_norm, 's-', label='Manhattan', linewidth=2, markersize=8)
plt.plot(k_values, euclidean_norm, '^-', label='Euclidean', linewidth=2, markersize=8)

plt.title('Comparative Elbow Analysis (Normalized)', fontsize=16)
plt.xlabel('Number of Clusters (K)', fontsize=14)
plt.ylabel('Normalized Sum of Squared Errors', fontsize=14)
plt.xticks(k_values)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('../images/comparative_elbow.png', dpi=300, bbox_inches='tight')
plt.close()

print("Elbow plots generated successfully!")
