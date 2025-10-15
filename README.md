# 🌤️ Weather Web App

A beautiful, responsive weather application built with Flask and Python that provides real-time weather information for any city worldwide.

## ✨ Features

- **Real-time Weather Data**: Get current weather conditions for any city
- **Beautiful UI**: Modern, responsive design that works on all devices
- **Multiple Weather Metrics**: Temperature, humidity, pressure, wind speed, and weather description
- **Error Handling**: Graceful error handling with user-friendly messages
- **Loading Animation**: Smooth loading experience while fetching data
- **Temperature Conversion**: Automatic conversion from Kelvin to Celsius

## 🚀 Live Demo

[Deploy your own version](#deployment) or run locally!

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **API**: OpenWeatherMap API
- **Styling**: Custom CSS with modern design principles

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Get API Key**
   - Go to [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Get your API key
   - Replace the API key in `app.py` (line 11)

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   - Go to `http://127.0.0.1:5000`
   - Enter a city name and enjoy!

## 📁 Project Structure

```
weather-app/
├── app.py                 # Main Flask application
├── templates/
│   └── index.html        # Web page template
├── static/
│   └── style.css         # Styling
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## 🎯 How It Works

1. **User Interface**: Clean, modern form for city input
2. **API Integration**: Connects to OpenWeatherMap API for real-time data
3. **Data Processing**: Converts and formats weather data
4. **Dynamic Display**: Updates the page with weather information
5. **Error Handling**: Shows helpful messages for invalid inputs

## 🌐 Deployment

### Heroku (Recommended)
1. Create a Heroku account
2. Install Heroku CLI
3. Create `Procfile`:
   ```
   web: gunicorn app:app
   ```
4. Deploy:
   ```bash
   git add .
   git commit -m "Initial commit"
   heroku create your-app-name
   git push heroku main
   ```

### Railway
1. Connect your GitHub repository
2. Railway will automatically detect Flask
3. Add your API key in environment variables
4. Deploy!

## 🔧 Configuration

### Environment Variables
For production deployment, set these environment variables:
- `API_KEY`: Your OpenWeatherMap API key
- `FLASK_ENV`: Set to `production`

## 📱 Screenshots

![Weather App Interface](screenshot.png)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [OpenWeatherMap](https://openweathermap.org/) for providing the weather API
- [Flask](https://flask.palletsprojects.com/) for the web framework
- [Font Awesome](https://fontawesome.com/) for icons

## 📞 Support

If you have any questions or need help, please open an issue or contact me!

---

**Made with ❤️ by [Your Name]**


## 🚀 Live Demo

**🌐 Live App**: [https://weather-app-yner.onrender.com/](https://weather-app-yner.onrender.com/)

Try it out! Enter any city name and get real-time weather data.
