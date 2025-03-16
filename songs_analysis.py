import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
from scipy import stats

# Set style for plots
plt.style.use('fivethirtyeight')
sns.set(font_scale=1.2)

# Create a directory for saving figures
os.makedirs('songs_figures', exist_ok=True)

# Download dataset
print("Downloading songs dataset...")
path = kagglehub.dataset_download("waqi786/songs-dataset-2000-2020-50k-records")
print(f"Dataset downloaded to: {path}")

# Load the dataset
# Assuming the CSV file is in the downloaded directory
csv_files = [f for f in os.listdir(path) if f.endswith('.csv')]
if not csv_files:
    raise FileNotFoundError("No CSV files found in the downloaded dataset")

# Print available files to identify the correct one
print(f"Available files: {os.listdir(path)}")

# Let's try to load the first CSV file
songs_data = pd.read_csv(os.path.join(path, csv_files[0]))

# Display basic info about the dataset
print("\nDataset Overview:")
print(f"Shape: {songs_data.shape}")
print("\nColumns:")
print(songs_data.columns.tolist())
print("\nSample data:")
print(songs_data.head())

# Check for missing values
print("\nMissing values:")
print(songs_data.isnull().sum())

# Function to save figures
def save_figure(fig, filename):
    fig.savefig(os.path.join('songs_figures', filename), bbox_inches='tight', dpi=300)
    plt.close(fig)

# Clean and prepare data
# Identify key columns
# Try to find popularity column
popularity_columns = [col for col in songs_data.columns if any(word in col.lower() for word in ['popular', 'stream', 'listen', 'like'])]
if popularity_columns:
    popularity_column = popularity_columns[0]
    print(f"\nFound popularity column: {popularity_column}")
else:
    # Use a numerical column as proxy for popularity
    numerical_cols = songs_data.select_dtypes(include=[np.number]).columns.tolist()
    if numerical_cols:
        print(f"No obvious popularity column found. Using numerical column: {numerical_cols[0]}")
        popularity_column = numerical_cols[0]
    else:
        raise ValueError("Could not identify a column for popularity")

# Try to find duration column
duration_columns = [col for col in songs_data.columns if any(word in col.lower() for word in ['duration', 'length', 'time'])]
if duration_columns:
    duration_column = duration_columns[0]
    print(f"Found duration column: {duration_column}")
else:
    duration_column = None
    print("No duration column identified")

# Try to find genre column
genre_columns = [col for col in songs_data.columns if any(word in col.lower() for word in ['genre', 'category', 'type', 'style'])]
if genre_columns:
    genre_column = genre_columns[0]
    print(f"Found genre column: {genre_column}")
else:
    genre_column = None
    print("No genre column identified")

# Try to find name/title column
name_columns = [col for col in songs_data.columns if any(word in col.lower() for word in ['name', 'title', 'song'])]
if name_columns:
    name_column = name_columns[0]
    print(f"Found song name column: {name_column}")
else:
    # Use first string column as name
    string_cols = songs_data.select_dtypes(include=['object']).columns
    name_column = string_cols[0] if len(string_cols) > 0 else songs_data.columns[0]
    print(f"Using {name_column} as song name column")

# Try to find artist column
artist_columns = [col for col in songs_data.columns if any(word in col.lower() for word in ['artist', 'band', 'singer', 'performer'])]
if artist_columns:
    artist_column = artist_columns[0]
    print(f"Found artist column: {artist_column}")
else:
    artist_column = None
    print("No artist column identified")

# Analysis 1: Top 20 songs of all time by popularity score
try:
    # Convert popularity to numeric if it's not already
    if not pd.api.types.is_numeric_dtype(songs_data[popularity_column]):
        songs_data[popularity_column] = pd.to_numeric(songs_data[popularity_column], errors='coerce')
    
    # Sort by popularity and get top 20
    top_songs = songs_data.sort_values(by=popularity_column, ascending=False).head(20)
    
    # Create plot
    fig, ax = plt.subplots(figsize=(14, 10))
    
    # If we have artist information, add it to the labels
    if artist_column:
        y_labels = top_songs.apply(lambda x: f"{x[name_column]} - {x[artist_column]}", axis=1)
    else:
        y_labels = top_songs[name_column]
    
    # Create the bar plot
    bars = sns.barplot(x=popularity_column, y=y_labels, data=top_songs, ax=ax)
    
    # Adjust the plot
    ax.set_title('Top 20 Songs of All Time by Popularity Score')
    ax.set_xlabel('Popularity Score')
    ax.set_ylabel('Song Title')
    
    # Save figure
    save_figure(fig, 'top20_popular_songs.png')
    print("Top 20 songs by popularity plot saved")
except Exception as e:
    print(f"Error in analysis 1: {e}")

# Analysis 2: How duration affects popularity
if duration_column:
    try:
        # Convert duration to numeric if needed
        if not pd.api.types.is_numeric_dtype(songs_data[duration_column]):
            songs_data[duration_column] = pd.to_numeric(songs_data[duration_column], errors='coerce')
        
        # Remove any NaN values
        data_clean = songs_data.dropna(subset=[duration_column, popularity_column])
        
        # Create scatter plot
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.scatterplot(x=duration_column, y=popularity_column, data=data_clean, alpha=0.6, ax=ax)
        
        # Add regression line
        sns.regplot(x=duration_column, y=popularity_column, data=data_clean, scatter=False, ax=ax, color='red')
        
        # Calculate correlation
        correlation, p_value = stats.pearsonr(data_clean[duration_column], data_clean[popularity_column])
        
        # Add correlation info to plot
        ax.annotate(f"Correlation: {correlation:.2f}\nP-value: {p_value:.4f}", 
                    xy=(0.05, 0.95), xycoords='axes fraction',
                    ha='left', va='top',
                    bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5))
        
        ax.set_title('Relationship Between Song Duration and Popularity')
        ax.set_xlabel('Song Duration')
        ax.set_ylabel('Popularity Score')
        
        # Save figure
        save_figure(fig, 'duration_vs_popularity.png')
        print("Duration vs popularity plot saved")
        
        # Create a boxplot of popularity by duration bins
        # Create duration bins
        duration_bins = pd.qcut(data_clean[duration_column], 5)
        
        # Group by bins and get mean popularity
        duration_popularity = data_clean.groupby(duration_bins)[popularity_column].mean().reset_index()
        
        # Create boxplot
        fig, ax = plt.subplots(figsize=(12, 8))
        sns.boxplot(x=duration_column, y=popularity_column, data=data_clean, ax=ax)
        
        ax.set_title('Popularity Distribution by Song Duration')
        ax.set_xlabel('Song Duration')
        ax.set_ylabel('Popularity Score')
        
        # Save figure
        save_figure(fig, 'duration_popularity_boxplot.png')
        print("Duration popularity boxplot saved")
        
    except Exception as e:
        print(f"Error in analysis 2: {e}")
else:
    print("Cannot analyze duration effects without duration information")

# Analysis 3: Which genre is most popular
if genre_column:
    try:
        # Group by genre and calculate mean popularity
        genre_popularity = songs_data.groupby(genre_column)[popularity_column].agg(['mean', 'count']).reset_index()
        
        # Filter genres with at least 10 songs
        genre_popularity = genre_popularity[genre_popularity['count'] >= 10].sort_values(by='mean', ascending=False)
        
        # Create bar plot for top genres by mean popularity
        fig, ax = plt.subplots(figsize=(14, 10))
        sns.barplot(x='mean', y=genre_column, data=genre_popularity.head(15), ax=ax)
        
        ax.set_title('Average Popularity by Music Genre')
        ax.set_xlabel('Average Popularity Score')
        ax.set_ylabel('Genre')
        
        # Save figure
        save_figure(fig, 'genre_popularity.png')
        print("Genre popularity plot saved")
        
        # Create pie chart for genre distribution (top genres)
        top_genres = songs_data[genre_column].value_counts().head(10)
        
        fig, ax = plt.subplots(figsize=(12, 12))
        ax.pie(top_genres, labels=top_genres.index, autopct='%1.1f%%', startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
        
        plt.title('Distribution of Top 10 Music Genres')
        
        # Save figure
        save_figure(fig, 'genre_distribution.png')
        print("Genre distribution plot saved")
        
    except Exception as e:
        print(f"Error in analysis 3: {e}")
else:
    print("Cannot analyze genre popularity without genre information")

print("\nSongs analysis completed!") 