import streamlit as st
import pandas as pd
import pickle
import requests



def recommend(movie):
    movie_index=movies[movies['title']== movie].index[0]

    movie_list=sorted(list(enumerate(similarity[movie_index])),reverse=True,key=lambda x:x[1])[1:6]

    recommended_movie=[]

    for i in movie_list:
        movie_id=i[0]
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie


similarity=pickle.load(open('similarity.pkl','rb'))

movie_dict=pickle.load(open('movies_dict.pkl','rb'))

movies=pd.DataFrame(movie_dict)

st.title('movie_recommander_system')        

selected_movie=st.selectbox(
    'which movie like you to prefer?',
    (movies['title'].values)
)
if st.button('Recommend'):
   for i in recommend(selected_movie):
       st.write(i)
    