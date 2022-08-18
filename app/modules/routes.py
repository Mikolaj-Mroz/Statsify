from app import app
from flask import request, redirect, session, render_template
from .stats import Listener, cache_handler, auth_manager



@app.route('/')
@app.route('/index')
def index():
  
  if request.args.get("code"):
    # Step 2. Being redirected from Spotify auth page
    auth_manager.get_access_token(request.args.get("code"))
    return redirect('/')

  if not auth_manager.validate_token(cache_handler.get_cached_token()):
    # Step 1. Display sign in link when no token
    auth_url = auth_manager.get_authorize_url()
    return render_template('index.html.jinja2', auth_url=auth_url)

  # Step 3. Signed in, display data
  return render_template('index.html.jinja2')

# top artists
@app.route('/top/artists/<term>')
def top_artists(term):

  # if not logged in
  if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')

  user = Listener()
  user.top_artists(term)
  return render_template('artists.html.jinja2', artists = user.artists['items'])

# top songs
@app.route('/top/tracks/<term>')
def top_tracks(term):

  # if not logged in
  if not auth_manager.validate_token(cache_handler.get_cached_token()):
        return redirect('/')
        
  user = Listener()
  user.top_tracks(term)
  return render_template('songs.html.jinja2', tracks = user.tracks['items'])


#privacy policy
@app.route('/privacy-policy')
def privacy():
  return render_template('privacy.html.jinja2')

#terms of service
@app.route('/terms-of-service')
def tos():
  return render_template('tos.html.jinja2')