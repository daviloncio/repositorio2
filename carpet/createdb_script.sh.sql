-- Database: p2_db

-- DROP DATABASE IF EXISTS p2_db;

	
	


\copy genres  -- nombre de la tabla
FROM 'genres.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY movie_genres  -- nombre de la tabla
FROM 'movie_genres.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY production_companies  -- nombre de la tabla
FROM 'production_companies.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY movie_production_companies  -- nombre de la tabla
FROM 'movie_production_companies.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY countries  -- nombre de la tabla
FROM 'countries.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY movie_production_countries  -- nombre de la tabla
FROM 'movie_production_countries.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY languages  -- nombre de la tabla
FROM 'languages.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY movie_spoken_languages  -- nombre de la tabla
FROM 'movie_spoken_languages.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY keywords  -- nombre de la tabla
FROM 'keywords.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY movie_keywords  -- nombre de la tabla
FROM 'movie_keywords.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY movie_basics  -- nombre de la tabla
FROM 'movie_basics.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY movie_additional  -- nombre de la tabla
FROM 'movie_additional.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY link_ids  -- nombre de la tabla
FROM 'link_ids.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY ratings  -- nombre de la tabla
FROM 'ratings.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY movie_crew  -- nombre de la tabla
FROM 'movie_crew.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY movie_cast  -- nombre de la tabla
FROM 'movie_cast.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY people  -- nombre de la tabla
FROM 'people.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';

COPY gender  -- nombre de la tabla
FROM 'gender.csv' -- nombre del archivo 
CSV HEADER
DELIMITER ','
QUOTE '"';


