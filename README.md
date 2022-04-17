# spotifysearch
(Work-in-progress) Uses Spotify API to find 1) top 10 songs for an artist and 2) Audio features of a selected track

Identifies the music features of a song that a user searches up
-User specifies song + artist

-Identifies the music characteristics of songs in an album a user searches up


-If user only specifies song, provide list of 10 results and user selects 1 for audio_features

-If user only specifies artist, provide lis.. i think this will require debugging Analyze() function esp if i imagine the users selection being called in the Analyze() function

**Potential Add-Ons**
-Create function to export to CSV
-Allows user to select the values for features-app then shows 10 songs that fit those characteristics 
	
	-user is able to refresh for 10 different songs of same characteristics, printed to terminal
	
-Add GUI so user interacts with external window
	
	-Add sliding scale for each characteristic 
		-Assigning numeric ranges to end point
	-Have the song name user selected playing in background (15s snip)

-Allow user to add songs to a playlist in their Spotify account
	
	-or "Like" all 10 songs so its added to their liked songs
