import os
import sys

from core.business import LoadTitles

print("+++++ Loading CSV file... This could take several minutes...")

load_titles = LoadTitles.LoadTitles()

titles = load_titles.load_from_csv_file(
    "./assets/netflix-shows/netflix_titles.csv", ",")

print("+++++ CSV file loaded successfully")
