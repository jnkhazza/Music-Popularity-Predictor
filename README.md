# Music Popularity Predictor

Web Application that uses several components that make up a song (loudness, acousticness, genre, etc.) to predict song popularity

The Data: CSV containing 18K rows of song data. The data was cleaned, organized and rearranged in Pandas with Python. The data was labeled as either having "Above 50%" or "50% or Below" popularity

The Machine Learning: Machine learning was done directly in Pandas via Sckit-learn and a Logistic Regression model

The Web Application: Once the Machine Learning Model was complete, I developed a web application using Flask and HTML/CSS. This application allows for user inputs the elements of their song to receive a prediction as the whether the song will high a popularity greater than or less than/equal to 50%
