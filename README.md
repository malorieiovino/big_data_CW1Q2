# Big Data Coursework 1 – Q2: Cluster Analysis using Apache Mahout

## 📖 Overview
This repository contains the implementation of **K-Means clustering** using **Apache Mahout** as part of the **Big Data Coursework 1**. The project involves clustering a collection of text documents using different distance measures and evaluating the clustering quality.

## 📂 Repository Structure
```
big_data_CW1Q2/
│── results/                     # Output clustering results
│   ├── centroids/               # Cluster centroids
│   ├── seqfiles/                # Sequence files generated from text data
│   ├── vectors/                 # Vector representations of text documents
│   ├── elbow_graphs/            # Elbow method plots
│── data/                        # Raw text files used for clustering
│── scripts/                     # Scripts for data processing & clustering
│── images/                      # Screenshots and plots for analysis
│── README.md                    # Project documentation
```


## 🛠️ Implementation Steps
### 1️⃣ Data Preparation
- Converted raw text documents into **sequence files**.
- Generated **sparse vector representations** for clustering.

### 2️⃣ K-Means Clustering
Performed K-Means clustering using three distance metrics:
- **Euclidean Distance**
- **Manhattan Distance**
- **Cosine Distance**

### 3️⃣ Finding Optimal Clusters (K)
- Used the **Elbow Method** to determine the optimal number of clusters.
- Evaluated **Sum of Squared Errors (SSE)** for **K = {5, 10, 15, 20}**.
- Plotted **elbow graphs** for comparison.

### 4️⃣ Results & Analysis
- **Cosine Distance** showed the most complex clustering behavior.
- **Manhattan Distance** exhibited sensitivity to intermediate cluster configurations.
- **Euclidean Distance** provided the most stable clustering.

## 📊 Key Findings
| Distance Measure | Best K | Observations |
|-----------------|--------|-------------|
| **Cosine**      | 20     | Best for semantic relationships |
| **Manhattan**   | 15     | Sensitive to intermediate clusters |
| **Euclidean**   | 20     | Most predictable clustering |

## 📸 Visualizations
Elbow graphs for different distance measures:

<img src="results/elbow_graphs/coselbow.png" alt="Elbow Graph - Cosine" width="400">
<img src="results/elbow_graphs/manelbow.png" alt="Elbow Graph - Manhattan" width="400">
<img src="results/elbow_graphs/eucelbow.png" alt="Elbow Graph - Euclidean" width="400">



## 📝 How to Run
### 1️⃣ Ensure Apache Mahout is Installed
```bash
sudo apt install mahout
```

### 2️⃣ Convert Raw Text into Sequence Files
```bash
mahout seqdirectory -i data/ -o results/seqfiles/
```

### 3️⃣ Convert Sequence Files into Sparse Vectors
```bash
mahout seq2sparse -i results/seqfiles/ -o results/vectors/
```

### 4️⃣ Run the K-Means Clustering
```bash
mahout kmeans -i results/vectors/tfidf-vectors -c results/centroids -o results/clusters -dm <distance-metric> -k <num-clusters> -ow -cl
```
Replace `<distance-metric>` with one of the following:
- `org.apache.mahout.common.distance.EuclideanDistanceMeasure`
- `org.apache.mahout.common.distance.ManhattanDistanceMeasure`
- `org.apache.mahout.common.distance.CosineDistanceMeasure`

Example command using **Cosine Distance** with **K=20**:
```bash
mahout kmeans -i results/vectors/tfidf-vectors -c results/centroids -o results/clusters -dm org.apache.mahout.common.distance.CosineDistanceMeasure -k 20 -ow -cl
```

### 5️⃣ Retrieve the Final Cluster Assignments
```bash
mahout clusterdump -i results/clusters/clusters-*-final -o results/cluster_summary.txt
```

### 6️⃣ Visualize the Elbow Graphs
Check the plots stored in the `/results/elbow_graphs/` folder.
```bash
ls results/elbow_graphs/
```




