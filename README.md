# Songs Dataset Analysis (2000-2020)

This project analyzes the "Songs Dataset 2000-2020" from Kaggle to visualize and understand music trends over the past two decades.

## Project Overview

This analysis explores patterns and trends in popular music from 2000 to 2020, examining factors that contribute to a song's popularity and how music characteristics have evolved over time. The Jupyter notebook includes detailed code, explanations, and visualizations that provide insights into the evolution of popular music.

## Interactive Notebook

The `songs_analysis.ipynb` notebook contains all the code and fully rendered visualizations. You can view this notebook directly on GitHub to see all the charts and analysis without having to run any code. The notebook features:

- Markdown explanations before each section
- Comments throughout the code
- All visualizations rendered inline with vibrant color schemes
- Distinctive markers and line styles for different data series
- Advanced dual-axis plots for comparing different metrics

## Analyses Performed

1. **Top 20 Songs by Popularity**: Visualization of the most popular songs based on popularity scores.
2. **Song Duration vs. Popularity**: Analysis of how the length of a song affects its popularity.
3. **Popularity Distribution by Genre**: Comparison of the popularity of different music genres.
4. **Genre Distribution**: Exploration of the distribution of music genres in the dataset.
5. **Trend of Song Characteristics Over Time**: Examination of how song attributes (including duration) have evolved over the years, featuring a dual-axis visualization with distinctive styling.
6. **Danceability vs. Energy**: Analysis of the relationship between a song's danceability and energy levels.

## Key Visualizations

All visualizations are rendered directly in the notebook and feature:

- **Vibrant color schemes**: Energetic colors appropriate for music data visualization
- **Dual-axis presentations**: Special plots that compare different metrics with distinct styling
- **Custom markers and line styles**: Different shapes and patterns to distinguish data series (e.g., '*' markers with dashed lines for song duration)
- **Highlighted color palette**: Key metrics like song duration use distinctive colors (e.g., #ff3864 for duration)
- **Enhanced legends**: Clear and descriptive legends that explain each element
- **Optimized readability**: Careful contrast choices for better data interpretation

The main visualizations include:
- `top20_popular_songs.png`: Bar chart of the most popular songs
- `duration_vs_popularity.png`: Scatter plot showing relationship between song duration and popularity
- `genre_popularity.png`: Bar chart of genres ranked by average popularity
- `genre_distribution.png`: Pie chart showing the distribution of music genres
- `song_trends_over_time.png`: Dual-axis line chart showing how song characteristics and duration have changed over time
- `danceability_vs_energy.png`: Scatter plot analyzing the relationship between danceability and energy

## Data Source

The data used in this analysis is from the Kaggle dataset ["Songs Dataset 2000-2020"](https://www.kaggle.com/datasets/waqi786/songs-dataset-2000-2020-50k-records).

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

## Usage

You can either:

1. **View the notebook on GitHub**: The notebook has all visualizations pre-rendered for easy viewing
2. **Run the notebook locally**: To reproduce or modify the analysis
   - Clone this repository
   - Install requirements
   - Run `jupyter notebook songs_analysis.ipynb`

## Key Findings

- Pop songs by artists like Ed Sheeran and The Weeknd dominate in terms of popularity
- There is a slight negative correlation between song duration and popularity, suggesting shorter songs may perform better
- Pop music is the most dominant genre both in quantity and average popularity
- The trend visualization clearly shows that song durations have decreased over time (highlighted with distinctive #ff3864 color and star markers)
- While duration decreases, attributes like danceability and energy show different trends
- Most successful songs achieve a balance between danceability and energy attributes
- Streaming numbers generally correlate with popularity scores, highlighting the importance of streaming platforms

## Author

This analysis was created as part of a data science project exploring popular datasets from Kaggle. 