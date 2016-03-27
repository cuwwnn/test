import folium

m = folium.Map(location=[35.687367, 139.752415], zoom_start=14)
folium.CircleMarker([35.687367, 139.752415], radius=50, color='#0033cc', fill_color='#0033cc', popup='test').add_to(m)
m.save('test.html')
