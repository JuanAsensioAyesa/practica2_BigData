-- Actores cuyas películas han sido mejorar valoradas junto con la media de sus películas
SELECT 
    a.Nombre, 
    avg(v.Puntuacion) Media_Peliculas
FROM 
    Cast c 
INNER JOIN 
    Voto v ON c.ClvCast = v.ClvPelicula
INNER JOIN 
    MiembroCast a ON a.ClvMiembroCast = c.ClvMiembroCast
GROUP BY 
    a.Nombre
HAVING 
    count(v.Puntuacion) > 2;
ORDER BY 
    Media_Peliculas DESC;

-- Peliculas más votadas por los usuarios y valoracion media
SELECT
    p.Titulo,
    COUNT(*) Numero_Votos,
    avg(v.Puntuacion) Media_Puntuacion
FROM
    Voto v
INNER JOIN 
    Pelicula p ON p.ClvPelicula = v.ClvPelicula
GROUP BY
    p.Titulo
ORDER BY
    Numero_Votos DESC;

-- Media de puntuaciones por genero principal
SELECT
    g.Genero1,
    avg(v.Puntuacion) Media_Puntuacion
FROM
    Voto v
INNER JOIN 
    Genero g ON g.ClvGenero = v.ClvGenero
GROUP BY
    g.Genero1
ORDER BY
    Media_Puntuacion DESC;

-- Media de puntuaciones por genero principal y secundario
SELECT
    g.Genero1,
    g.Genero2,
    avg(v.Puntuacion) Media_Puntuacion
FROM
    Voto v
INNER JOIN 
    Genero g ON g.ClvGenero = v.ClvGenero
GROUP BY
    g.Genero1,
    g.Genero2
ORDER BY
    Media_Puntuacion DESC;

-- Media de puntuaciones por genero principal, secundario y terciario
SELECT
    g.Genero1,
    g.Genero2,
    g.Genero3,
    avg(v.Puntuacion) Media_Puntuacion
FROM
    Voto v
INNER JOIN 
    Genero g ON g.ClvGenero = v.ClvGenero
GROUP BY
    g.Genero1,
    g.Genero2,
    g.Genero3
ORDER BY
    Media_Puntuacion DESC;
