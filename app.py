import streamlit as st, pandas as pd
import pickle



# fetching the movie_list,we could have fetched directly usng pickle
# but the streamlit application was not accepting in that format
# so we needed to fetch in the form of dictionary using pandas dataframe


movies = pickle.load(open('/movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies)

st.title('Movie Recommender System')

option = st.selectbox(
    'Write the Movie Name you want recommendation for:',
    label_visibility="collapsed",
    options= movies['title'].values,
    index = None,
    placeholder="Search for Movie",
    )

selected_movie = option



similarity = pickle.load(open("/similarity.pkl", 'rb'))

def recommend (movie):
    movie_index = movies[movies['title'] == movie].index[0] # fetching index of movie
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = list()
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]]['title'])
    return recommended_movies

if st.button('Recommend'):
    st.write('Recommendations for: ', option)
    ans = recommend(selected_movie)
    for item in ans:
        st.write(item)