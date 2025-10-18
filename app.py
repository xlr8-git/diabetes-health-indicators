from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

pipeline = pickle.load(open('diabetes_pipeline.pkl', 'rb'))
model = pipeline['model']
scaler = pipeline['scaler']
model_features = pipeline['features']

categorical_cols = [
    'gender', 'ethnicity', 'education_level',
    'income_level', 'employment_status',
    'smoking_status'
]

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()  
        df = pd.DataFrame([data])

        df_encoded = pd.get_dummies(df, columns=categorical_cols)

        df_encoded = df_encoded.reindex(columns=model_features, fill_value=0)

        num_features = [
            'age', 'alcohol_consumption_per_week', 'physical_activity_minutes_per_week',
            'diet_score', 'sleep_hours_per_day', 'screen_time_hours_per_day',
            'family_history_diabetes', 'hypertension_history', 'cardiovascular_history',
            'bmi', 'waist_to_hip_ratio', 'systolic_bp', 'diastolic_bp', 'heart_rate',
            'cholesterol_total', 'hdl_cholesterol', 'ldl_cholesterol', 'triglycerides',
            'glucose_fasting', 'glucose_postprandial', 'insulin_level', 'hba1c'
        ]
        df_encoded[num_features] = scaler.transform(df_encoded[num_features])

        prediction = model.predict(df_encoded)[0]
        return jsonify({'prediction': int(prediction)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
