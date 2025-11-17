-- Opret database hvis den ikke findes
CREATE DATABASE IF NOT EXISTS hotel_kong_arthur;

-- Opret bruger og giv adgang
CREATE USER IF NOT EXISTS 'hotel_user'@'%' IDENTIFIED BY 'hotel_password';
GRANT ALL PRIVILEGES ON hotel_kong_arthur.* TO 'hotel_user'@'%';
FLUSH PRIVILEGES;

-- Brug databasen
USE hotel_kong_arthur;

-- Tabeller
CREATE TABLE IF NOT EXISTS rooms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    room_number VARCHAR(10) NOT NULL,
    room_type VARCHAR(50),
    price DECIMAL(10,2),
    is_available BOOLEAN DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS guests (
    id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    guest_id INT,
    room_id INT,
    check_in DATE,
    check_out DATE,
    FOREIGN KEY (guest_id) REFERENCES guests(id),
    FOREIGN KEY (room_id) REFERENCES rooms(id)
);

CREATE TABLE IF NOT EXISTS drinks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2)
);