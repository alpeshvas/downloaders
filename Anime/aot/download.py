import os
import requests
BASE_DIR = '/home/vas/anime/{tv_series_name}/s{season}/'
FILE_NAME = '{tv_series_name}_s{season}e{episode}_sub.mp4'
DOWNLOADING_STRING = 'Downloading {tv_series_name}_season{season}_e{episode}'
BASE_URL = 'http://mp4watch.tv/media/{tv_series_name}_season{season}_sub/{tv_series_name}_s{season}e{episode}_sub.mp4'
anime = {'aot' : {'season':3,'episodes':25 }}
anime_name='aot'
def download_using_whatever_you_want(url,location):

	request = requests.get(url, timeout=10, stream=True)
	with open(location, 'wb') as file:
	    for chunk in request.iter_content(1024 * 1024):
	        file.write(chunk)

	print "Downloaded"
def download_it(name,season,episode):
	to_be_stored_location = BASE_DIR.format(tv_series_name=name,season=season)
	file_name = FILE_NAME.format(season=season,episode=episode,tv_series_name=name)
	if season == 1 and episode < 19:
		return
	if not os.path.exists(to_be_stored_location):
		os.makedirs(to_be_stored_location)
	print DOWNLOADING_STRING.format(season=season,episode=episode,tv_series_name=name)
	url_to_be_retrieve = BASE_URL.format(tv_series_name=name,season=season,episode=episode)
	print "Url -> "+ url_to_be_retrieve
	download_using_whatever_you_want(url_to_be_retrieve,to_be_stored_location+file_name)
def download_season(name):
	map(lambda season:(map(lambda episode: download_it(name,season,episode),range(1,anime[name]['episodes']) )), range(1,anime[name]['season']) )
def main():
	download_season('aot')
if __name__ == '__main__':
	main()