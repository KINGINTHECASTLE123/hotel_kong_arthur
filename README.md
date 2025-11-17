# Hotel Kong Arthur – Microservice Arkitekturprojekt

Et tværfagligt 3. semester projekt på IT-Arkitektur.  
Formålet er at bygge et mikrotjenestebaseret system, der understøtter Hotel Kong Arthurs forretningsprocesser.

---

## Struktur

| Mappe | Funktion |
|-------|-----------|
| `guest_service`  | Håndterer gæsteinformationer |
| `booking_service`| Håndterer bookinger |
| `room_service`   | Værelsestyper og priser |
| `drinks_service` | Drinks-salg og KPI’er |
| `api_gateway`    | Samlet indgangspunkt (backend) |
| `streamlit_ui`   | Frontend bygget i Streamlit |

---

## Teknologier

- Python (Flask)
- MySQL
- Streamlit
- Docker Compose

---

## Kom i gang

### 1. Klon projektet
    git clone https://github.com/KINGINTHECASTLE123/hotel_kong_arthur.git
    cd hotel_kong_arthur

### 2. Opret et virtual environment   

### 3. Opret .env-fil
    Credentials sendt i separat fil

### 4. Start systemet
    docker compose up --build

---

## URLs

| Service         | URL |
|-----------------|-----|
| Streamlit UI    | http://localhost:8520 |
| API Gateway     | http://localhost:5050 |
| Booking Service | http://localhost:5001 |
| Drinks Service  | http://localhost:5002 |
| Guest Service   | http://localhost:5003 |
| Room Service    | http://localhost:5004 |
