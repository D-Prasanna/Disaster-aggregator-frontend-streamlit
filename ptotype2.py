import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go

# Load the dataset
file_path = "C:\\Users\\prasa\\Hackathon\\Dataset cleaning\\merged_data.csv"
df = pd.read_csv(file_path,)

# # Generate simulated dates (for timeseries plotting)
# np.random.seed(0)
# df['created_at'] = pd.to_datetime(
#     np.random.choice(pd.date_range(start='2023-01-01', end='2023-12-31'), len(df))
# )

# # Group by date for the timeseries plot
# tweet_counts_by_date = df['created_at'].value_counts().sort_index()


st.markdown(
    """
    <style>
    .main {
        background-color: black;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def home_page():
    st.title("Disaster Aggregation Dashboard")

    st.image("C:\\Users\\prasa\\Hackathon\\testing stuff\\Post-and-Grant-Avenue-Look.jpg", use_column_width=True, caption="Real-time Disaster Monitoring")

    st.subheader("Introduction")
    st.write("""
    The Disaster Aggregation Dashboard is your one-stop solution for real-time monitoring and analysis of disaster-related tweets. 
    This platform aggregates data from various sources to provide insights into the frequency and location of disasters, helping users stay informed and prepared.
    """)

    st.subheader("Key Features")
    st.write("""
    - **Real-time Tweet Monitoring:** Track disaster-related tweets from around the world.
    - **Interactive Dashboard:** Visualize data with heatmaps, graphs, and timelines.
    - **Comprehensive Analysis:** Get detailed insights into disaster trends and patterns.
    """)

    st.subheader("Get Started")
    st.write("Use the navigation options on the left to explore the Dashboard and learn more about us.")


def dashboard_page():
    st.title("Disaster Dashboard")
    st.write("Monitor real-time disaster data through interactive visualizations.")

    # Heatmap Placeholder (Existing Code)
    st.subheader("Heatmap of Tweet Density by Region")
    st.write("This heatmap shows the density of disaster-related tweets from different regions.")
    
    # Sample data for the heatmap (Placeholder for actual data)
    data = [
        [1, 20, 30, 50, 1],
        [20, 1, 60, 80, 30],
        [30, 60, 1, -10, 20]
    ]

    heatmap_fig = px.imshow(data, color_continuous_scale='Viridis')
    st.plotly_chart(heatmap_fig, use_container_width=True)

    # Simulated Real-time Bar Chart for Label Distribution
    st.subheader("Disaster Type Tweet Distribution")
    st.write("This bar chart displays the number of tweets for each disaster type.")
    
    location_counts = df['location'].value_counts()

    # Create the bar chart using the location data
    bar_fig = px.bar(x=location_counts.index, y=location_counts.values, 
                    labels={'x':'Location', 'y':'Tweet Count'},
                    title="Distribution of Tweets by Location")
    st.plotly_chart(bar_fig, use_container_width=True)

    # Simulated Real-time Timeline of Tweets
    st.subheader("Timeline of Tweets")
    st.write("This timeline shows the frequency of disaster-related tweets over time.")
    
    tweet_counts_by_date = df['created_at'].value_counts().sort_index()

    fig = go.Figure()

    # Add a trace to the figure object
    fig.add_trace(go.Scatter(x=[], y=[], mode='lines+markers', name='Tweet Count'))

    # Plot initial empty graph
    plot = st.plotly_chart(fig, use_container_width=True)

    for i in range(1, len(tweet_counts_by_date) + 1):
        fig.data[0].x = tweet_counts_by_date.index[:i]
        fig.data[0].y = tweet_counts_by_date.values[:i]
        plot.plotly_chart(fig, use_container_width=True)
        time.sleep(0.7)  # Simulating real-time plotting
    
def about_page():
    st.title("About Us")
    st.write("""
    We are a team of passionate students participating in the Smart India Hackathon. 
    Our goal is to develop an innovative disaster aggregation and analysis platform 
    that can assist in improving disaster response efforts. By leveraging real-time data 
    from social media and other sources, our platform aims to provide timely and accurate 
    information to help organizations, governments, and individuals respond to disasters more effectively.
    
    This project is part of our effort to make a meaningful contribution to society 
    and showcase our technical skills on a national stage.
    """)


def contact_page():
    st.title("Contact Us")
    st.write("Details on how to contact us.")

def main():
    st.sidebar.title("Navigation")
    option = st.sidebar.radio(
        'Select a page:',
        ('Home', 'Dashboard', 'About Us', 'Contact Us')
    )
    
    if option == 'Home':
        home_page()
    elif option == 'Dashboard':
        dashboard_page()
    elif option == 'About Us':
        about_page()
    elif option == 'Contact Us':
        contact_page()

if __name__ == "__main__":
    main()