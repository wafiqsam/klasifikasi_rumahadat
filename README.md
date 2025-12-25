# KLASIFIKASI RUMAH ADAT #

### DESKRIPSI PROYEK ###

Proyek ini merupakan tugas Mata Kuliah Pembelajaran Mesin yang bertujuan untuk membangun Website Sederhana berbasis Streamlit untuk melakukan klasifikasi citra rumah adat Indonesia menggunakan Deep Learning dan Transfer Learning.

Sistem ini mengimplementasikan:

- 1 model Neural Network dasar (CNN Non-Pretrained)
- 2 model Pretrained (Transfer Learning : MobileNetV2 dan EfficientNet)

Pengguna dapat memilih model yang diinginkan melalui dropdown (multi-model) dan mengunggah gambar rumah adat untuk mendapatkan hasil prediksi.

### DATASET ###

🔹 Jenis Data

Data Citra 

🔹 Kelas
Dataset terdiri dari 5 kelas rumah adat Indonesia:
- Honai
- Gadang
- Joglo
- Tongkonan
- Rumah Panjang

🔹 Sumber Dataset
Dataset diperoleh dari:

Kaggle: https://www.kaggle.com/datasets/rariffirmansah/rumah-adat

###  PREPROCESSING DATA ###

Tahapan preprocessing yang dilakukan:

- Resize gambar ke ukuran 224 × 224
- Normalisasi pixel
- Augmentasi data (rotasi, zoom, flip horizontal)
- Split dataset: Training, Validation, Testing

###  MODELING ###

🔹 CNN (Non-Pretrained) 
- Dibangun dari awal (from scratch)
- Menggunakan Convolutional Layer, MaxPooling, dan Dense Layer
- Digunakan sebagai baseline model

🔹 MobileNetV2 (Transfer Learning) 
- Model pretrained dari ImageNet
- Layer awal dibekukan (freeze)
- Fine-tuning pada layer akhir

🔹 EfficientNet (Transfer Learning)
- Model pretrained dengan efisiensi tinggi
- Transfer learning + fine-tuning
- Performa terbaik pada dataset

### EVALUASI MODEL ###
Model dievaluasi menggunakan beberapa metrik, termasuk classification report dan confusion matrix.

🔹 Classification Report
Berikut adalah penjelasan tentang metrik yang digunakan dalam classification report:
- Precision: Mengukur proporsi prediksi positif yang benar.
- Recall: Mengukur proporsi sampel aktual positif yang berhasil diidentifikasi dengan benar.
- F1-Score: Rata-rata harmonis dari precision dan recall.
- Accuracy: Mengukur keseluruhan performa model.

#### Hasil Classification Report (CNN)

| Kelas       | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| Gadang     | 0.96      | 0.84   | 0.89     | 192     |
| Honai      | 0.95      | 0.52   | 0.67     | 122     |
| Joglo      | 0.57      | 0.78   | 0.66     | 144     |
| Panjang    | 0.50      | 0.53   | 0.52     | 124     |
| Tongkonan  | 0.71      | 0.77   | 0.73     | 200     |
| **Accuracy** |  |  | **0.71** | **782** |
| **Macro Avg** | 0.74 | 0.69 | 0.69 | 782 |
| **Weighted Avg** | 0.75 | 0.71 | 0.71 | 782 |

#### Hasil Confusion Matrix (CNN)

<img width="514" height="470" alt="download" src="https://github.com/user-attachments/assets/4dace028-50e1-48bd-8061-fd9a0be88e8b" />

#### Hasil Classification Report (MobileNetV2)

| Kelas       | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| Gadang     | 0.96 | 0.84 | 0.89 | 192 |
| Honai      | 0.95 | 0.52 | 0.67 | 122 |
| Joglo      | 0.57 | 0.78 | 0.66 | 144 |
| Panjang    | 0.50 | 0.53 | 0.52 | 124 |
| Tongkonan  | 0.71 | 0.77 | 0.73 | 200 |
| **Accuracy** |  |  | **0.71** | 782 |
| **Macro Avg** | 0.74 | 0.69 | 0.69 | 782 |
| **Weighted Avg** | 0.75 | 0.71 | 0.71 | 782 |

#### Hasil Confusion Matrix (MobileNetV2)

<img width="513" height="470" alt="image" src="https://github.com/user-attachments/assets/439949be-aa15-4277-a45b-b2e36278cc1b" />

#### Hasil Classification Report (EfficientNet)

| Kelas       | Precision | Recall | F1-Score | Support |
|------------|-----------|--------|----------|---------|
| Gadang     | 0.99 | 0.98 | 0.98 | 192 |
| Honai      | 0.99 | 0.99 | 0.99 | 122 |
| Joglo      | 0.99 | 0.98 | 0.98 | 144 |
| Panjang    | 0.98 | 1.00 | 0.99 | 124 |
| Tongkonan  | 0.99 | 0.99 | 0.99 | 200 |
| **Accuracy** |  |  | **0.99** | **782** |
| **Macro Avg** | **0.99** | **0.99** | **0.99** | **782** |
| **Weighted Avg** | **0.99** | **0.99** | **0.99** | **782** |

#### Hasil Confusion Matrix (EfficientNet)

<img width="513" height="470" alt="image" src="https://github.com/user-attachments/assets/fbb14f46-2389-4f2e-bfe5-0dc8b6bb7e1a" />

### KESIMPULAN ###
Berdasarkan hasil evaluasi, model berbasis transfer learning secara konsisten mengungguli CNN non-pretrained. EfficientNet menghasilkan performa terbaik dengan akurasi 99%
------------------------------------------------------------------------------------------------------------------------------------

### SISTEM STREAMLIT SEDERHANA ###

Aplikasi berbasis Streamlit ini bertujuan untuk memudahkan pengguna dalam melakukan prediksi kesuksesan akademik mahasiswa. Aplikasi ini dapat memprediksi kategori status akademik mahasiswa (Dropout, Enrolled, Graduate) berdasarkan input yang diberikan.

🔹 Fitur Website
- Upload gambar rumah adat
- Dropdown pilihan model:
  - CNN
  - MobileNetV2
  - EfficientNet
Menampilkan:
- Gambar input
- Nama kelas prediksi
- Confidence score

CONTOH :

<img width="272" height="418" alt="image" src="https://github.com/user-attachments/assets/446afcb6-18c4-45c2-ba62-863976bc00e0" />

### BIODATA ###

Nama: Wafiq Azizah

Nim: 202210370311247

Program Studi: Informatika

Universitas: Universitas Muhammadiyah Malang





