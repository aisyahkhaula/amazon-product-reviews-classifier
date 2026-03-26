# 1. Gunakan Python image official yang ringan
FROM python:3.10-slim

# 2. Set folder kerja di dalam container
WORKDIR /app

# 3. Copy file requirements.txt terlebih dahulu (agar build cache efisien)
COPY requirements.txt .

# 4. Install library yang dibutuhkan (tambah uvicorn jika belum ada)
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy seluruh file kode dan model (.py dan .pkl) ke dalam container
COPY . .

# 6. Expose port 8080 (Standar Google Cloud Run)
EXPOSE 8080

# 7. Perintah untuk menjalankan FastAPI menggunakan Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]