import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import numpy as np

# Expanded Comprehensive Typhoon Dataset (Last 20 Years)
typhoon_data = pd.DataFrame([
    {
        'name': 'Typhoon Haiyan',
        'year': 2013,
        'latitude': 11.2426,
        'longitude': 125.0324,
        'wind_speed': 195,
        'pressure': 895,
        'category': 'Super Typhoon',
        'region': 'Philippines',
        'damage_estimate_usd': 14_000_000_000,
        'fatalities': 6300,
        'description': 'One of the most powerful tropical cyclones ever recorded, causing catastrophic damage in the Philippines.'
    },
    {
        'name': 'Typhoon Mangkhut',
        'year': 2018,
        'latitude': 20.1939,
        'longitude': 121.5450,
        'wind_speed': 165,
        'pressure': 905,
        'category': 'Super Typhoon',
        'region': 'Philippines/China',
        'damage_estimate_usd': 4_000_000_000,
        'fatalities': 200,
        'description': 'A powerful typhoon that caused significant damage across the Philippines and Southern China.'
    },
    {
        'name': 'Typhoon Melor',
        'year': 2015,
        'latitude': 13.6929,
        'longitude': 125.0324,
        'wind_speed': 140,
        'pressure': 925,
        'category': 'Typhoon',
        'region': 'Philippines',
        'damage_estimate_usd': 250_000_000,
        'fatalities': 45,
        'description': 'A typhoon that impacted the Philippines, causing moderate damage and loss of life.'
    },
    {
        'name': 'Typhoon Hagibis',
        'year': 2019,
        'latitude': 35.6762,
        'longitude': 139.6503,
        'wind_speed': 160,
        'pressure': 915,
        'category': 'Super Typhoon',
        'region': 'Japan',
        'damage_estimate_usd': 15_000_000_000,
        'fatalities': 86,
        'description': 'A devastating typhoon that caused extensive damage and flooding in Japan.'
    },
    {
        'name': 'Typhoon Meranti',
        'year': 2016,
        'latitude': 21.9314,
        'longitude': 120.6354,
        'wind_speed': 190,
        'pressure': 890,
        'category': 'Super Typhoon',
        'region': 'Taiwan',
        'damage_estimate_usd': 1_500_000_000,
        'fatalities': 64,
        'description': 'An extremely powerful typhoon that impacted Taiwan with intense winds.'
    },
    {
        'name': 'Typhoon Jebi',
        'year': 2018,
        'latitude': 34.4333,
        'longitude': 135.3333,
        'wind_speed': 155,
        'pressure': 910,
        'category': 'Super Typhoon',
        'region': 'Japan',
        'damage_estimate_usd': 12_000_000_000,
        'fatalities': 17,
        'description': 'A destructive typhoon that caused significant damage in the Kansai region of Japan.'
    },
    {
        'name': 'Typhoon Yutu',
        'year': 2018,
        'latitude': 15.2267,
        'longitude': 146.1029,
        'wind_speed': 180,
        'pressure': 900,
        'category': 'Super Typhoon',
        'region': 'Northern Mariana Islands',
        'damage_estimate_usd': 600_000_000,
        'fatalities': 4,
        'description': 'A powerful typhoon that devastated the Northern Mariana Islands.'
    },
    {
        'name': 'Typhoon Lan',
        'year': 2017,
        'latitude': 33.0121,
        'longitude': 138.9719,
        'wind_speed': 155,
        'pressure': 910,
        'category': 'Super Typhoon',
        'region': 'Japan',
        'damage_estimate_usd': 3_000_000_000,
        'fatalities': 23,
        'description': 'A significant typhoon that impacted Japan with strong winds and heavy rainfall.'
    },
    {
        'name': 'Typhoon Goni',
        'year': 2020,
        'latitude': 13.6594,
        'longitude': 123.8650,
        'wind_speed': 165,
        'pressure': 905,
        'category': 'Super Typhoon',
        'region': 'Philippines',
        'damage_estimate_usd': 1_200_000_000,
        'fatalities': 25,
        'description': 'A powerful typhoon that caused significant destruction in the Philippines.'
    },
    {
        'name': 'Typhoon Amphan',
        'year': 2020,
        'latitude': 20.2938,
        'longitude': 88.5431,
        'wind_speed': 165,
        'pressure': 905,
        'category': 'Super Typhoon',
        'region': 'India/Bangladesh',
        'damage_estimate_usd': 13_000_000_000,
        'fatalities': 128,
        'description': 'A catastrophic cyclone that caused extensive damage in India and Bangladesh.'
    },
    # Additional Typhoons
    {
        'name': 'Typhoon Soudelor',
        'year': 2015,
        'latitude': 20.7535,
        'longitude': 126.8785,
        'wind_speed': 180,
        'pressure': 890,
        'category': 'Super Typhoon',
        'region': 'Taiwan/China',
        'damage_estimate_usd': 3_500_000_000,
        'fatalities': 56,
        'description': 'A powerful typhoon that impacted Taiwan and Eastern China.'
    },
    {
        'name': 'Typhoon Talim',
        'year': 2016,
        'latitude': 24.2577,
        'longitude': 122.9927,
        'wind_speed': 150,
        'pressure': 920,
        'category': 'Typhoon',
        'region': 'Japan',
        'damage_estimate_usd': 500_000_000,
        'fatalities': 7,
        'description': 'A typhoon that caused moderate damage in southern Japan.'
    }
])

def create_enhanced_globe_visualization(filtered_data):
    """Create an enhanced globe visualization with more aesthetic design and improved accuracy"""
    try:
        # Calculate marker size based on wind speed with a more nuanced scaling
        # Use a logarithmic scaling to better represent wind speed differences
        marker_sizes = np.log1p(filtered_data['wind_speed']) * 25

        # 3D Globe Visualization with Enhanced Aesthetics
        fig = go.Figure(data=[
            go.Scattergeo(
                lon=filtered_data['longitude'],
                lat=filtered_data['latitude'],
                text=filtered_data['name'],
                marker=dict(
                    size=marker_sizes,
                    color=filtered_data['wind_speed'],
                    colorscale='Inferno',
                    colorbar=dict(
                        title='Wind Speed (km/h)',
                        titleside='right',
                        titlefont=dict(size=12)
                    ),
                    reversescale=True,
                    opacity=0.8,
                    line=dict(
                        color='rgb(40, 40, 40)',
                        width=0.5
                    )
                ),
                hoverinfo='text',
                hovertemplate='<b>%{text}</b><br>Latitude: %{lat:.4f}<br>Longitude: %{lon:.4f}<br>Wind Speed: %{marker.size*4} km/h<extra></extra>'
            )
        ])

        fig.update_layout(
            title={
                'text': 'Typhoon Global Impact Visualization',
                'y':0.95,
                'x':0.5,
                'xanchor': 'center', 
                'yanchor': 'top',
                'font': dict(size=24)
            },
            geo=dict(
                showland=True,
                landcolor='rgba(230, 230, 230, 0.7)',
                countrycolor='rgba(180, 180, 180, 0.7)',
                coastlinecolor='rgba(150, 150, 150, 0.7)',
                projection_type='orthographic',  # More spherical projection
                showocean=True,
                oceancolor='rgba(200, 230, 255, 0.5)',
                showcountries=True,
                showcoastlines=True
            ),
            height=900,  # Increased height
            width=1200,  # Increased width
            margin=dict(l=0, r=0, t=50, b=0),
            paper_bgcolor='rgba(0,0,0,0)',  # Fully transparent background
            plot_bgcolor='rgba(0,0,0,0)'
        )

        # Add sphere-like border
        fig.update_layout(
            geo_scope='world',
            geo=dict(
                showframe=False,
                showcoastlines=True,
                projection_rotation=dict(
                    lon=-100,  # Rotate to show more land
                    lat=20,
                    roll=0
                )
            )
        )

        return fig
    except Exception as e:
        st.error(f"Error creating globe visualization: {e}")
        return None

def main():
    try:
        st.set_page_config(
            page_title="Global Typhoon Tracker",
            page_icon="🌪️",
            layout="wide"
        )

        st.title("🌍 Global Typhoon Insights")

        # Sidebar for Filtering
        st.sidebar.header("Typhoon Explorer")
        
        # Enhanced Dropdown with More Information
        typhoon_info = {row['name']: row for _, row in typhoon_data.iterrows()}
        selected_typhoon = st.sidebar.selectbox(
            "Select Typhoon for Detailed View", 
            list(typhoon_info.keys()),
            format_func=lambda x: f"{x} ({typhoon_info[x]['year']})"
        )

        # Get the selected typhoon's data
        typhoon = typhoon_info[selected_typhoon]

        # Main Visualization Columns
        col1, col2 = st.columns([2, 1])

        with col1:
            # Filter data for selected typhoon
            filtered_data = typhoon_data[typhoon_data['name'] == selected_typhoon]
            
            # Create enhanced globe visualization
            fig = create_enhanced_globe_visualization(filtered_data)
            if fig:
                st.plotly_chart(fig, use_container_width=True)

        with col2:
            # Typhoon Details Card
            st.header(f"{selected_typhoon} Details")
            
            # Detailed Information Display
            st.markdown(f"""
            **Year:** {typhoon['year']}
            
            **Category:** {typhoon['category']}
            
            **Wind Speed:** {typhoon['wind_speed']} km/h
            
            **Pressure:** {typhoon['pressure']} hPa
            
            **Region:** {typhoon['region']}
            
            **Damage Estimate:** ${typhoon['damage_estimate_usd']:,}
            
            **Fatalities:** {typhoon['fatalities']}
            """)
            
            # Description
            st.subheader("Description")
            st.write(typhoon['description'])

        # Additional Insights
        st.header("Typhoon Comparative Analysis")
        
        # Damage vs Wind Speed Scatter Plot
        fig_damage = px.scatter(
            typhoon_data, 
            x='wind_speed', 
            y='damage_estimate_usd', 
            color='year',
            hover_name='name',
            size='fatalities',
            labels={
                'wind_speed': 'Wind Speed (km/h)', 
                'damage_estimate_usd': 'Damage Estimate (USD)',
                'fatalities': 'Fatalities'
            },
            title='Typhoon Impact: Wind Speed, Damage, and Fatalities'
        )
        
        # Customize scatter plot aesthetics
        fig_damage.update_layout(
            height=500,
            width=1000,
            margin=dict(l=50, r=50, t=50, b=50)
        )
        
        st.plotly_chart(fig_damage, use_container_width=True)

    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()