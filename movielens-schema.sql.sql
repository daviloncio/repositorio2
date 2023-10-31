
CREATE TYPE movie_status AS ENUM ('Canceled','In Production', 'Planned','Post Production','Released', 'Rumored');

CREATE TABLE gender ( --id gender_id?
    id integer NOT NULL PRIMARY KEY,
    name int,
    UNIQUE(id,name) 
);

CREATE TABLE people (
    id integer NOT NULL PRIMARY KEY,
    name varchar,
    gender int,
    profile_path varchar,
    UNIQUE(id,profile_path),
    FOREIGN KEY(id)REFERENCES gender(id)
);

CREATE TABLE movie_basics (
    id integer NOT NULL PRIMARY KEY,
    title varchar NOT NULL,
    original_title varchar,
    release_date date,
    original_language varchar,
    adult boolean,
    status movie_status,
    UNIQUE(id,original_title)
);


CREATE TABLE movie_additional (
    id integer NOT NULL PRIMARY KEY ,
    imbd_id varchar,
    homepage varchar,
    budget integer CHECK (budget>0),
    overview varchar,
    popularity float,
    vote_avarage float CHECK (vote_avarage>0),
    vote_count integer CHECK (vote_count>0),
    poster_path varchar,
    tagline varchar,
    video boolean,
    runtime float,
    revenue integer,
    FOREIGN KEY(id) REFERENCES movie_basics(id),
    UNIQUE(id,imbd_id,poster_path)
);

CREATE TABLE movie_cast (
    credit_id varchar NOT NULL PRIMARY KEY ,
    movie_id integer,
    FOREIGN KEY(movie_id) REFERENCES movie_basics(id),
    person_id integer, --ref del id de la entidad person
    character varchar,
    cast_id integer,
    orden integer, --pq tiene otro color
    FOREIGN KEY(person_id) REFERENCES people(id),
    UNIQUE(credit_id,movie_id)
);

CREATE TABLE movie_crew (
    credit_id varchar NOT NULL PRIMARY KEY ,
    movie_id integer,
    FOREIGN KEY(movie_id) REFERENCES movie_basics(id),
    FOREIGN KEY(person_id) REFERENCES people(id),
    person_id integer, --ref del id de la entidad person
    deparment varchar,
    job varchar,
    profile_path varchar, --pq tiene otro color
    UNIQUE(credit_id,movie_id)
);




CREATE TABLE ratings ( --relación ratings-links??
    user_id integer NOT NULL,
    movie_id integer NOT NULL,
    rating int,
    timestamp_ timestamp,
    UNIQUE (user_id,movie_id) 
);

CREATE TABLE links_ids (
    movie_id integer PRIMARY KEY,
    imdb_id varchar,
    tmpdb_id int,
    UNIQUE(movie_id,imdb_id,tmpdb_id)
);


CREATE TABLE collections ( 
    id integer NOT NULL PRIMARY KEY, 
    name varchar NOT NULL,
    poster_path varchar,
    backrop_path varchar
);

CREATE TABLE genres(
    genre_id integer NOT NULL PRIMARY KEY ,
    name varchar, 
    UNIQUE(genre_id,name)
);

CREATE TABLE movie_genres(
    movie_id integer,
    genre_id integer,
    UNIQUE (movie_id, genre_id),
    FOREIGN KEY(movie_id) REFERENCES movie_basics(id),
    FOREIGN KEY(genre_id) REFERENCES genres(genre_id)
);

CREATE TABLE production_companies(
    company_id integer NOT NULL PRIMARY KEY,
    name varchar ,
    UNIQUE(company_id,name)
);

CREATE TABLE movie_production_companies(
    movie_id integer,
    company_id integer,
    FOREIGN KEY(movie_id) REFERENCES movie_basics(id),
    FOREIGN KEY(company_id) REFERENCES production_companies(company_id)
);

CREATE TABLE production_countries(
    iso_3166_1 char NOT NULL PRIMARY KEY,
    name varchar,
    UNIQUE(iso_3166_1,name)
);

CREATE TABLE movie_production_countries(
    movie_id integer,
    country_code char,
    FOREIGN KEY(movie_id) REFERENCES movie_basics(id),
    FOREIGN KEY(country_code) REFERENCES production_countries(iso_3166_1)
);

CREATE TABLE spoken_languages(
    iso_639_1  char NOT NULL PRIMARY KEY,
    name varchar,
    UNIQUE(iso_639_1 ,name)
);

CREATE TABLE movie_spoken_languages(
    movie_id integer,
    language_code char,
    FOREIGN KEY(movie_id) REFERENCES movie_basics(id),
    FOREIGN KEY(language_code) REFERENCES spoken_languages(iso_639_1)
);

CREATE TABLE keywords(
    keyword_id  integer NOT NULL PRIMARY KEY,
    name varchar
);

CREATE TABLE movie_keywords(
    movie_id integer,
    keyword_id integer,
    FOREIGN KEY(movie_id) REFERENCES movie_basics(id),
    FOREIGN KEY(keyword_id) REFERENCES keywords(keyword_id)
);
