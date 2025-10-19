# Diabetes Health Indicators Prediction System

A machine learning-based web application that predicts diabetes risk using comprehensive health indicators and lifestyle factors. The system uses a trained Random Forest model to analyze various health metrics and provide risk predictions through both a Flask API and Streamlit web interface.

## Features

- **Comprehensive Health Analysis**: Evaluates 29 different health indicators including biometric measurements, lifestyle factors, and medical history
- **Real-time Prediction**: Instant diabetes risk assessment through web interface
- **RESTful API**: Flask-based API for integration with other applications
- **Interactive Web Interface**: User-friendly Streamlit dashboard for health data input
- **Machine Learning Pipeline**: Pre-trained Random Forest model with data preprocessing pipeline

## Health Indicators Analyzed

### Biometric Measurements
- Age, BMI, Waist-to-Hip Ratio
- Blood Pressure (Systolic/Diastolic)
- Heart Rate
- Cholesterol Levels (Total, HDL, LDL)
- Triglycerides
- Glucose Levels (Fasting, Postprandial)
- Insulin Level, HbA1c

### Lifestyle Factors
- Physical Activity (minutes per week)
- Diet Score
- Sleep Hours (per day)
- Screen Time (hours per day)
- Alcohol Consumption (per week)
- Smoking Status

### Medical History
- Family History of Diabetes
- Hypertension History
- Cardiovascular History

### Demographic Information
- Gender, Ethnicity
- Education Level, Income Level
- Employment Status

## Installation

1. Clone the repository:
```bash
git clone https://github.com/xlr8-git/diabetes-health-indicators.git
cd diabetes-health-indicators
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Option 1: Streamlit Web Application

Run the Streamlit application:
```bash
streamlit run streamlit_app.py
```

The application will open in your browser at `http://localhost:8501`. Enter your health information in the form and click "Predict" to get your diabetes risk assessment.

### Option 2: Flask API

1. Start the Flask API server:
```bash
python app.py
```

2. The API will be available at `http://127.0.0.1:5000`

3. Send POST requests to `/predict` endpoint with health data:
```bash
curl -X POST http://127.0.0.1:5000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 45,
    "gender": "Male",
    "bmi": 28.5,
    "glucose_fasting": 95,
    "hba1c": 5.8,
    ...
  }'
```

## Model Information

- **Algorithm**: Random Forest Classifier
- **Dataset**: 100,000 health records with comprehensive diabetes indicators
- **Features**: 29 health and lifestyle indicators
- **Target**: Binary classification (0: No Diabetes Risk, 1: Diabetes Risk)
- **Preprocessing**: Feature scaling and categorical encoding included in pipeline

## File Structure

```
diabetes-health-indicators/
├── app.py                          # Flask API server
├── streamlit_app.py               # Streamlit web interface
├── diabetes-health-indicators1.ipynb  # Data analysis and model training notebook
├── diabetes_dataset.csv           # Training dataset
├── diabetes_pipeline.pkl          # Preprocessing pipeline
├── best_rf_model.pkl             # Trained Random Forest model
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

## API Endpoints

### POST /predict

Predicts diabetes risk based on provided health indicators.

**Request Body**: JSON object containing health indicators
**Response**: JSON object with prediction result

**Example Response**:
```json
{
  "prediction": 1
}
```

## Dependencies

- Flask: Web framework for API
- Streamlit: Web application framework
- scikit-learn: Machine learning library
- pandas: Data manipulation
- numpy: Numerical computing
- requests: HTTP library for API calls

## Data Privacy

This application processes health data locally and does not store or transmit personal information to external servers. All predictions are performed using the local machine learning model.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This application is for educational and informational purposes only. It should not be used as a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns.
