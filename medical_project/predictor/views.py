"""
heart/views.py  — drop-in replacement for your existing Django prediction view.

Changes vs. original:
  • Loads the TUNED model (rf_tuned.joblib) and its matching scaler / feature list.
  • Computes the 3 engineered features before prediction so the API stays backward-
    compatible: the caller still sends the original 11 clinical inputs; the view
    derives the new features automatically.
  • All other Django / URL wiring stays exactly the same.
"""

import os, joblib, numpy as np
from django.shortcuts import render
from django.http import JsonResponse
import json

# ── Load artefacts once at import time ───────────────────────────────────────
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..', '..', 'heart_model'))

model = joblib.load(os.path.join(MODEL_DIR, 'rf_tuned.joblib'))
scaler       = joblib.load(os.path.join(MODEL_DIR, 'scaler_tuned.joblib'))
feature_names = joblib.load(os.path.join(MODEL_DIR, 'feature_names.joblib'))

# Original 11 clinical features (after CFS from the notebook)
CLINICAL_FEATURES = [
    'thal', 'ca', 'oldpeak', 'thalach', 'exang',
    'cp', 'slope', 'sex', 'age', 'restecg', 'trestbps',
]


def _engineer(data: dict) -> dict:
    """Add the 3 interaction features derived in Bonus Cell 2."""
    data['age_thalach_ratio']  = data['age']     / (data['thalach'] + 1e-5)
    data['st_depression_rate'] = data['oldpeak']  * (data['slope'] + 1)
    data['thal_ca_product']    = data['thal']    *  data['ca']
    return data


def predict(request):
    """
    Handle GET request by showing the form.
    Handle POST request by processing form data, running prediction, and showing result.
    """
    if request.method == 'GET':
        return render(request, 'predictor/index.html')

    if request.method == 'POST':
        try:
            # Build full feature dict (clinical)
            data = {}
            for k in CLINICAL_FEATURES:
                if k not in request.POST:
                    return render(request, 'predictor/index.html', {'error': f'Missing field: {k}'})
                data[k] = float(request.POST[k])

            # Engineer features
            data = _engineer(data)

            # Arrange in the exact column order the model was trained on
            row = np.array([[data[f] for f in feature_names]])

            row_scaled   = scaler.transform(row)
            prediction   = int(model.predict(row_scaled)[0])
            probability  = float(model.predict_proba(row_scaled)[0][1])

            prob_percent = round(probability * 100, 1)

            if prob_percent < 30:
                risk_tier = 'low'
                risk_tier_label = 'Low Risk'
            elif prob_percent < 70:
                risk_tier = 'medium'
                risk_tier_label = 'Moderate Risk'
            else:
                risk_tier = 'high'
                risk_tier_label = 'High Risk'

            context = {
                'prediction': prediction,
                'probability': prob_percent,
                'risk_tier': risk_tier,
                'risk_tier_label': risk_tier_label,
            }
            return render(request, 'predictor/index.html', context)

        except Exception as e:
            return render(request, 'predictor/index.html', {'error': f'An error occurred: {str(e)}'})

# ── Optional: health-check endpoint ──────────────────────────────────────────
def health(request):
    return JsonResponse({
        'status':          'ok',
        'model':           'Tuned Random Forest (Bonus Cell 2)',
        'n_features':      len(feature_names),
        'feature_names':   feature_names,
    })


def info_page(request):
    return render(request, 'predictor/info.html')


def how_to_use(request):
    return render(request, 'predictor/howto.html')

