from flask import Flask, render_template, request, jsonify
import requests
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

# Your API key
API_KEY = '2e7f7c95d01e6a8051896295c799f1c1'

@app.route('/')
def home():
    """Main page - shows the form"""
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    """Handle the weather request"""
    try:
        # Get city name from the form
        city_name = request.form.get('city', '').strip()
        
        if not city_name:
            return jsonify({'error': 'Please enter a city name'})
        
        # Create the API URL
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}"
        
        # Make the API request
        response = requests.get(url, verify=False)
        
        if response.status_code == 200:
            weather_data = response.json()
            
            # Extract the information we need
            result = {
                'success': True,
                'city': weather_data['name'],
                'country': weather_data['sys']['country'],
                'temperature': round(weather_data['main']['temp'] - 273.15, 1),  # Convert from Kelvin to Celsius
                'description': weather_data['weather'][0]['description'],
                'humidity': weather_data['main']['humidity'],
                'pressure': weather_data['main']['pressure'],
                'wind_speed': weather_data['wind']['speed']
            }
            return jsonify(result)
            
        else:
            error_data = response.json()
            return jsonify({'error': f"Error: {error_data.get('message', 'Unknown error')}"})
            
    except Exception as e:
        return jsonify({'error': f'Something went wrong: {str(e)}'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
