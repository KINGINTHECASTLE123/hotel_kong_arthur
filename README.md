# Hotel Kong Arthur – Microservice Arkitekturprojekt

Dette projekt er en tværfaglige miniprojekt på IT-Arkitektur 3. semester.  
Formålet er at opbygge et mikrotjenestebaseret system, der understøtter Hotel Kong Arthurs forretningsprocesser.

---

## Struktur

Projektet består af følgende microservices:

| Mappe           | Beskrivelse                         |
|------------------|--------------------------------------|
| `guest_service`  | Håndterer gæsteinformationer         |
| `booking_service`| Håndterer booking af værelser        |
| `room_service`   | Information om værelser og priser    |
| `drinks_service` | Håndterer salg af drinks             |
| `api_gateway`    | Et samlet indgangspunkt for frontend |
| `streamlit_ui`   | Frontend bygget i Streamlit          |

---

## Kom i gang

### 1. Klon projektet

```bash
git clone https://github.com/<DIT-BRUGERNAVN>/hotel_kong_arthur.git
cd hotel_kong_arthur