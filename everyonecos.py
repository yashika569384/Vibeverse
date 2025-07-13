import pickle
import numpy as np
from PIL import Image
import webbrowser
import pyttsx3
import requests
import re
import streamlit as st
import urllib
import pandas as pd
dfe=pd.read_csv('everyone.csv',encoding='ISO-8859-1')

def show():
  st.markdown("""
    <style>
    /* Neon-style Streamlit button styling */
    div.stButton > button:first-child {
        background-color:#0f0f0f;
        color:#2653d1;
        font-weight: bold;
        font-family: 'Courier New', Courier, monospace;
        border: 2px solid #2653d1;
        border-radius: 15px;
        padding: 25px 35px;
        font-size: 100px;
        width: 230px;
        height: 50px;
        text-shadow: 0 0 5px #2653d1, 0 0 10px #2653d1;
        box-shadow: 0 0 10px #2653d1, 0 0 20px #2653d1, 0 0 30px #2653d1;
        transition: 0.3s ease-in-out;
    }

    div.stButton > button:first-child:hover {
        background-color: #1f1f1f;
        color: #00ffff;
        border-color: #00ffff;
        text-shadow: 0 0 5px #00ffff, 0 0 10px #00ffff;
        box-shadow: 0 0 15px #00ffff, 0 0 25px #00ffff, 0 0 35px #00ffff;
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

#  search_query = st.text_input("Search for a song")
#  if search_query:
#      if len(search_query) >= 3:
#       fil_df=dft[dft.apply(lambda row: search_query.lower() in row.to_string().lower(),axis=1)]
#       if not fil_df.empty:
#        st.subheader("Search Results:")
#        if len(fil_df)==1:
#          img=fil_df['Poster'].iloc[0]
#          st.image(img,width=200)
#          s=fil_df['Name'].iloc[0]
#        else:
#         lef, mid = st.columns(2)
#         img1=fil_df['Poster'].iloc[0]
#         img2=fil_df['Poster'].iloc[1]
#         s1=fil_df['Name'].iloc[0]
#         s2=fil_df['Name'].iloc[1]
  import random
  if 'songs_evselected' not in st.session_state:
    st.session_state.songs_evselected = random.sample(dfe.to_dict('records'), 9)  # Pick 2 random songs
    st.session_state.current_song_eleft = st.session_state.songs_evselected[0]
    st.session_state.current_song_emiddle = st.session_state.songs_evselected[1]
    st.session_state.current_song_eright = st.session_state.songs_evselected[2]
    st.session_state.current_song_ele = st.session_state.songs_evselected[3]
    st.session_state.current_song_emi = st.session_state.songs_evselected[4]
    st.session_state.current_song_eri = st.session_state.songs_evselected[5]
    st.session_state.current_song_elee = st.session_state.songs_evselected[6]
    st.session_state.current_song_emii = st.session_state.songs_evselected[7]
    st.session_state.current_song_erii = st.session_state.songs_evselected[8]
    
    left, middle, right = st.columns(3)
    songev1=st.session_state.current_song_eleft
    songev2=st.session_state.current_song_emiddle
    songev3=st.session_state.current_song_eright
    songev4= st.session_state.current_song_ele 
    songev5= st.session_state.current_song_emi
    songev6= st.session_state.current_song_eri
    songev7=st.session_state.current_song_elee
    songev8=st.session_state.current_song_emii
    songev9=st.session_state.current_song_erii

    s_lev=songev1['Name']
    s_mev=songev2['Name']
    s_rev=songev3['Name']
    s_leev=songev4['Name']
    s_miev=songev5['Name']
    s_riev=songev6['Name']
    s_leeev=songev7['Name']
    s_miiev=songev8['Name']
    s_riiev=songev9['Name']

  dfe['combined_features']=dfe['Genre']+dfe['Rating']
  from sklearn.feature_extraction.text import CountVectorizer
  cv=CountVectorizer(max_features=10000, stop_words='english')
  c=cv.fit_transform(dfe['combined_features'].values.astype('U')).toarray()
  from sklearn.metrics.pairwise import cosine_similarity
  similarity=cosine_similarity(c)
  import random
  def recommand(song_name):
      idx=dfe[dfe['Name']==song_name].index[0]
      distance = sorted(list(enumerate(similarity[idx])), reverse=True, key=lambda vector:vector[1])
# 
      s=[dfe.iloc[i[0]] for i in distance[1:7]]
#  random.shuffle(s1)
  
      rec = random.sample(s, min(len(s), 7))
      for song in rec: 
#  st.write(s1)
       songs = song['Name']
       poster_url = song['Poster']    # ✅ Access poster directly
       st.image(poster_url, width=150)
       st.write(songs)
  
    
  import urllib
  import requests
  songev1=st.session_state.current_song_eleft
  songev2=st.session_state.current_song_emiddle
  songev3=st.session_state.current_song_eright
  songev4= st.session_state.current_song_ele 
  songev5= st.session_state.current_song_emi
  songev6= st.session_state.current_song_eri
  songev7=st.session_state.current_song_elee
  songev8=st.session_state.current_song_emii
  songev9=st.session_state.current_song_erii
  s_lev=songev1['Name']
  s_mev=songev2['Name']
  s_rev=songev3['Name']
  s_leev=songev4['Name']
  s_miev=songev5['Name']
  s_riev=songev6['Name']
  s_leeev=songev7['Name']
  s_miiev=songev8['Name']
  s_riiev=songev9['Name']
  left, middle, right = st.columns(3)              
  left.image(songev1['Poster'], width=150)
  with left:
     st.write(s_lev)
     if st.button("Recommendations:",key='rec_lefte'):
      recommand(s_lev)
  middle.image(songev2['Poster'], width=150)
  with middle:
     st.write(s_mev)
     if st.button("Recommendations:",key='rec_middlee'):
      recommand(s_mev)
  right.image(songev3['Poster'], width=150)
  with right:
    st.write(s_rev)
    if st.button("Recommendations:", key="play_erighte"):
      recommand(s_rev)
  le, mi, ri = st.columns(3)
  with le:
   songev4= st.session_state.current_song_ele
   st.image(songev4['Poster'], width=150)
   st.write(songev4['Name'])
   if st.button("Recommendation", key="play_ele"):
      
      recommand(s_leev)
  with mi:
    songev5 = st.session_state.current_song_emi
    st.image(songev5['Poster'], width=150)
    st.write(songev5['Name'])
    if st.button("Recommend", key="play_emie"):
      
      recommand(s_miev)
  with ri:
    songev6 = st.session_state.current_song_eri
    st.image(songev6['Poster'], width=150)
    st.write(songev6['Name'])
    if st.button("Recommendation:", key="play_erie"):
  
      recommand(s_riev)
  lee, mii, rii = st.columns(3)
  with lee:
    songev7= st.session_state.current_song_elee
    st.image(songev7['Poster'], width=150)
    st.write(songev7['Name'])
    if st.button("Recommendation:", key="play_eleee"):
      
      recommand(s_leeev)
# Middle Column - Fixed Song 2
  with mii:
    songev8 = st.session_state.current_song_emii
    st.image(songev8['Poster'], width=150)
    st.write(songev8['Name'])
    if st.button("Recomendation:", key="play_emiie"):
      
      recommand(s_miiev)

# Right Column - "Now Playing" Section
  with rii:
    songev9 = st.session_state.current_song_erii
    st.image(songev9['Poster'], width=150)
    st.write(songev9['Name'])
    if st.button("Recommendation:", key="play_eriie"):
      
      recommand(s_riiev)   
# show()  
