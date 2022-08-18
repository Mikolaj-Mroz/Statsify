import spotipy
import os
from flask import session
from caching import FlaskSessionCacheHandler




# set cache handler to flask
cache_handler = FlaskSessionCacheHandler(session)
# configurate auth_manager
auth_manager = spotipy.oauth2.SpotifyOAuth(scope='user-top-read',
                                            cache_handler=cache_handler,
                                            show_dialog=True,)

class Listener:
  def __init__(self):
    # create spotify instance
    self.spotify = spotipy.Spotify(auth_manager=auth_manager)
  
  def top_tracks(self, term):
    # short_term = 4 weeks
    # medium_term = 6 months
    # long_term = all time
    self.tracks = self.spotify.current_user_top_tracks(50, 0, term)
  
  def top_artists(self, term):
    # short_term = 4 weeks
    # medium_term = 6 months
    # long_term = all time
    self.artists = self.spotify.current_user_top_artists(50, 0, term)
