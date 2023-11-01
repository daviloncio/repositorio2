export PGDATABASE:=movielens
export PGUSER :=alumnodb
export PGPASSWORD :=alumnodb
export PGHOST:=localhost

all:
	dropdb --if-exists movielens
	createdb -U alumnodb movielens
	psql -U alumnodb movielens < movielens_schema.sql
	psql -U alumnodb movielens < createdb_script.sh 
