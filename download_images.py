import requests
import os
from urllib.parse import urlparse

# Create directories
os.makedirs('static/images/destinations', exist_ok=True)
os.makedirs('static/images/testimonials', exist_ok=True)

images = {
    'maldives.jpg': 'https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=1920&h=1080&fit=crop',
    'bali.jpg': 'https://images.unsplash.com/photo-1518676590629-3dcbd9c5a5c9?w=1920&h=1080&fit=crop',
    'paris.jpg': 'https://images.unsplash.com/photo-1543782249-3f02e0b2f36c?w=1920&h=1080&fit=crop',
    'dubai.jpg': 'https://images.unsplash.com/photo-1546412178-5fad6269c389?w=1920&h=1080&fit=crop',
    'goa.jpg': 'https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=1920&h=1080&fit=crop',
    'switzerland.jpg': 'https://images.unsplash.com/photo-1534450290765-205b8f248bab?w=1920&h=1080&fit=crop',
    'newyork.jpg': 'https://images.unsplash.com/photo-1492684223066-81342ee5ff30?w=1920&h=1080&fit=crop',
    'mauritius.jpg': 'https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=1920&h=1080&fit=crop',
    'himachal.jpg': 'https://images.unsplash.com/photo-1571780935502-d89771a99192?w=1920&h=1080&fit=crop',
    'singapore.jpg': 'https://images.unsplash.com/photo-1552519507-da3b142c6e3d?w=1920&h=1080&fit=crop',
    'hero-bg.jpg': 'https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=3840&h=2160&fit=crop'
}

for filename, url in images.items():
    try:
        response = requests.get(url)
        path = f'static/images/destinations/{filename}'
        with open(path, 'wb') as f:
            f.write(response.content)
        print(f"✅ Downloaded: {filename}")
    except Exception as e:
        print(f"❌ Error downloading {filename}: {e}")

print("🎉 All images downloaded successfully!")