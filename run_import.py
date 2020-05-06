import os
import sys

from core.business import LoadTitles
from core.business import BuildGenreCountyGraph

print("+++++ Loading CSV file... This could take several minutes...")

load_titles = LoadTitles.LoadTitles()

titles = load_titles.load_from_csv_file(
    "./assets/netflix-shows/netflix_titles.csv", ",")

print("+++++ CSV file loaded successfully")


print("+++++ Building Graph... This could take several minutes...")
builder = BuildGenreCountyGraph.BuildGenreCountry(titles)
builder.build_graph()
builder.graph.print_graph()
