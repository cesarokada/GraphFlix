import os
import sys
import datetime
from core.business import LoadTitles
from core.business import BuildGenreCountyGraph
from core.utils.NetworkConverter import NetworkConverter
from core.utils.GephiFormatConverter import GephiFormatConverter
from core.utils.StatisticsNetwork import StatisticsNetwork

local_path = os.path.abspath(os.path.dirname(__file__))
output_path = os.path.join(local_path, "out")

print("+++++ Loading CSV file... This could take several minutes...")

load_titles = LoadTitles.LoadTitles()

titles = load_titles.load_from_csv_file(
    "./assets/netflix-shows/netflix_titles.csv", ",")

print("+++++ CSV file loaded successfully")


print("+++++ Building GENRE-COUNTRY Graph... This could take several minutes...")
builder = BuildGenreCountyGraph.BuildGenreCountry(titles)
builder.build_graph()
genre_country_network = NetworkConverter.get_network(builder.graph)
GephiFormatConverter.generate_file(genre_country_network, output_path, 'genre-country.gexf')
StatisticsNetwork.get_full_report(genre_country_network)