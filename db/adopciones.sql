-- =====================================================
-- BASE DE DATOS: ADOPCIONES
-- Proyecto: Huellitas de Amor
-- =====================================================

CREATE DATABASE IF NOT EXISTS adopciones_db;

USE adopciones_db;

-- =====================================================
-- TABLA: mascotas
-- =====================================================

CREATE TABLE IF NOT EXISTS mascotas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    tipo VARCHAR(50) NOT NULL,
    raza VARCHAR(100),
    edad VARCHAR(50) NOT NULL,
    sexo VARCHAR(20),
    tamaño VARCHAR(30),
    descripcion TEXT,
    ciudad VARCHAR(100),
    estado VARCHAR(30) DEFAULT 'Disponible',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- TABLA: adoptantes
-- =====================================================

CREATE TABLE IF NOT EXISTS adoptantes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20) NOT NULL,
    correo VARCHAR(150) NOT NULL,
    ciudad VARCHAR(100) NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =====================================================
-- TABLA: adopciones
-- =====================================================

CREATE TABLE IF NOT EXISTS adopciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    mascota_id INT NOT NULL,
    adoptante_id INT NOT NULL,
    fecha_adopcion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    estado VARCHAR(30) DEFAULT 'En proceso',

    FOREIGN KEY (mascota_id)
        REFERENCES mascotas(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    FOREIGN KEY (adoptante_id)
        REFERENCES adoptantes(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);

-- =====================================================
-- DATOS DE EJEMPLO
-- =====================================================

INSERT INTO mascotas
(nombre, tipo, raza, edad, sexo, tamaño, descripcion, ciudad, estado)
VALUES
(
    'Luna',
    '🐶 Perrito',
    'Criolla',
    '2 años',
    'Hembra',
    'Mediano',
    'Luna es una perrita cariñosa, juguetona y busca una familia responsable.',
    'Bogotá',
    'Disponible'
),
(
    'Milo',
    '🐱 Gatito',
    'Criollo',
    '8 meses',
    'Macho',
    'Pequeño',
    'Milo es un gato tranquilo y curioso que busca un hogar lleno de cariño.',
    'Bogotá',
    'Disponible'
),
(
    'Coco',
    '🦜 Ave Doméstica',
    'Periquito',
    '1 año',
    'Macho',
    'Pequeño',
    'Coco es un ave doméstica activa y sociable.',
    'Bogotá',
    'Disponible'
);