from __future__ import print_function    #(at top of module)
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth 
import json
import time
import sys
import pprint
import inquirer 

cid = '5dd7ddba79e44ca58ad9c38fde81498a'
secret = '0a01bb4a13244105a004db2c5ac304dc'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(cid,secret))
pp = pprint.PrettyPrinter(indent=4, sort_dicts=False)

#Gives you Audio Features with Track + Artist Entry
			#Main problem: Song + Artist combo isn't giving correct result. Need to debug analyze() function
def analyze(track=None,artist=None):
	r = sp.search(q='artist:' + track, type="track", limit=10)

	#isolates song name
	R = r['tracks']['items'][0]['name']

	#isolates track ID
	idx = r['tracks']['items'][0]['id']

	#isolates artist name
	x = r['tracks']['items'][0]['artists'][0]['name']
	results = spotify.audio_features(idx)

	#strips excessive info
	removing = ['time_signature', 'duration_ms', 'analysis_url', 'track_href', 'uri']

	for i in removing:
		results[0].pop(i)
	print(R + " by " + x)
	pp.pprint(results)

#Prints out top 10 results of song search along with audio analysis for each track. 
#I want to remove duplicates
def ten_songs(track=None):
	r = sp.search(q='track:' + track, type="track", limit=10, market="US")
	removing = ['time_signature', 'duration_ms', 'analysis_url', 'track_href', 'uri','type','id']
	g = 0
	i=0
	while g < 10:
		idx = r['tracks']['items'][g]['id']
		R = r['tracks']['items'][g]['name']
		results = spotify.audio_features(idx)
		for x in removing:
			results[0].pop(x)
		print(R + " by " + r['tracks']['items'][g]['artists'][0]['name'])
		pp.pprint(results)
		g+=1

#Gives top 10 songs of artist
			#Main problem: How does code differentiate between whether an artist is entered or song is entered. E.g.{
						#J.I.D doesn't return JID songs, only JID features.
						#Ne-Yo returns Tyler Creator songs, which differ from when the arg = Tyler the creator
						#Trying to use inquirer library to make list of artist's songs selection-based
						#}
def ten_from_artist(artist=None):
	x=0
	i=0
	#gives artist info...searching by artist for their songs
	r = sp.search(q='artist:' + artist, type='track',limit=10,market="US")

	#isolates artist id
	r_id = r['tracks']['items'][0]['artists'][0]['id']

	#isolates and prints FIRST 10 RESULTS
	while x<10:
		r_name = r['tracks']['items'][x]['name']
		# print(r_name)
		x+=1

	#finds tracks using artist ID
	idx = sp.artist_top_tracks(r_id)
	# pp.pprint(idx)	

	#prints artist's TOP 10 SONGS
	while i < 10:
		topsongname = idx['tracks'][i]['name']
		#isolates artist name
		g = idx['tracks'][0]['artists'][0]['name']
		print(topsongname + " by " + g)
		# print(ls)
		# lss=[]
		# lss.append(topsongname)
		i+=1
		# print(lss)
	# ls = [inquirer.List('size',message="Which song do you want to see?", choices=lss)]
	# answers = inquirer.prompt(ls)

#User enters Track + Artist
if len(sys.argv) > 2:
	track = sys.argv[1]
	artist = sys.argv[2]
	analyze(track, artist)

#User only enters artist name, is given top 10 songs
elif len(sys.argv) > 1:
	artist = sys.argv[1]
	ten_from_artist(artist)


print("---DONE WITH CODE---")
















