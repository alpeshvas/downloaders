import urllib2
BASE_DIR = '/home/vas/anime/{tv_series_name}/{season}/{episode}'
BASE_URL = 'http://mp4watch.tv/media/{tv_series_name}_season{season}_sub/{tv_series_name}_s{season}e{episode}_sub.mp4'
anime = {'aot' : {'season':3,'episodes':25 }}
anime_name='aot'
def download_it(name,season,episode):

def download_season(name):
	map(lambda season:(map(lambda:episode: download_it(name,season,episode),range(1,anime['name']['episodes']) )), range(1,anime['name']['season'] ))
def main():
	download_season('aot')
if __name__ == '__main__':
	main()