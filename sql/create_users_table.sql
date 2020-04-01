CREATE TABLE users
(
    client_key integer NOT NULL,
    email character varying(40) NOT NULL,
    password character varying(20) NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (client_key)
)