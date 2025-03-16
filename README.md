# Songs Dataset Analysis (2000-2020)

This project analyzes the "Songs Dataset 2000-2020" from Kaggle to visualize and understand music trends over the past two decades.

## Analyses Performed

1. **Top 20 Songs by Popularity**: Visualization of the most popular songs based on popularity scores.
2. **Relationship Between Song Duration and Popularity**: Analysis of how the length of a song affects its popularity.
3. **Genre Popularity Analysis**: Exploration of which music genres are most popular and their distribution.

## Requirements

- Python 3.6+
- Required packages:
  - numpy
  - pandas
  - matplotlib
  - seaborn
  - kagglehub
  - scipy

You can install all requirements using:
```
pip install -r requirements.txt
```

## Dataset

The dataset is downloaded automatically from Kaggle using the kagglehub library:
```python
kagglehub.dataset_download("waqi786/songs-dataset-2000-2020-50k-records")
```

## Usage

Simply run the Python script:
```
python songs_analysis.py
```

The script will:
1. Download the dataset from Kaggle
2. Process the data
3. Generate visualizations in the `songs_figures` directory

## Outputs

All visualizations are saved in the `songs_figures` directory:
- `top20_popular_songs.png`: Bar chart of the most popular songs
- `duration_vs_popularity.png`: Scatter plot with regression line showing relationship between song duration and popularity
- `duration_popularity_boxplot.png`: Box plot showing distribution of popularity scores across different song durations
- `genre_popularity.png`: Bar chart of genres ranked by average popularity
- `genre_distribution.png`: Pie chart showing the distribution of top music genres

If a specific column isn't found in the dataset, the script will try to use alternatives or proxies based on the available data.

## Analyses Details

### Top 20 Songs by Popularity
This analysis identifies and visualizes the most popular songs in the dataset based on popularity score.

### Duration vs. Popularity
This analysis explores whether the length of a song has any correlation with its popularity, including:
- Scatter plot with regression line
- Statistical correlation analysis
- Boxplots showing popularity distribution across different duration ranges

### Genre Popularity
This analysis examines:
- Which music genres have the highest average popularity scores
- The distribution of genres in the dataset (top 10 genres)

## Note

The script is designed to be adaptive, as the column names in the dataset may vary. It will try to identify the most appropriate columns for the analyses based on keywords in the column names. 