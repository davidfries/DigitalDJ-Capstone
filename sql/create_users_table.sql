CREATE TABLE users
(
    column_id serial,
    client_key character varying(10) NOT NULL,
    email character varying(320) NOT NULL,
    password text NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (client_key)
)