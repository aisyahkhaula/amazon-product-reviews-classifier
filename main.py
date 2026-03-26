from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Inisialisasi aplikasi FastAPI
app = FastAPI(
    title="Amazon Review Classifier API",
    description="API Klasifikasi Teks Hierarkis menggunakan TF-IDF dan Logistic Regression",
    version="1.0"
)

# 1. Memuat model yang sudah dilatih (Pastikan nama file sesuai)
print("Sedang memuat model ML...")
vectorizer = joblib.load('tfidf_vectorizer.pkl')
model_cat1 = joblib.load('model_cat1.pkl')
model_cat2 = joblib.load('model_cat2.pkl')
model_cat3 = joblib.load('model_cat3.pkl')

# 2. Mendefinisikan format data yang diterima (Input)
class ReviewRequest(BaseModel):
    text: str

# 3. Membuat Jalur (Endpoint) untuk menerima request dan memberikan prediksi
@app.post("/predict")
def predict_category(request: ReviewRequest):
    # Mengubah teks input menjadi matriks angka
    teks_vektor = vectorizer.transform([request.text])
    
    # Melakukan prediksi untuk ketiga level dan mengubahnya ke teks Python standar (str)
    prediksi_cat1 = str(model_cat1.predict(teks_vektor)[0])
    prediksi_cat2 = str(model_cat2.predict(teks_vektor)[0])
    prediksi_cat3 = str(model_cat3.predict(teks_vektor)[0])
    
    # Mengembalikan hasil (Output) dalam format JSON
    return {
        "status": "success",
        "input_text": request.text,
        "predictions": {
            "Level_1_Category": prediksi_cat1,
            "Level_2_Category": prediksi_cat2,
            "Level_3_Category": prediksi_cat3
        }
    }