CREATE TABLE messages
(
    message_id serial,
    sender character varying(320) NOT NULL,
    room character varying(50) NOT NULL,
    message text NOT NULL,
    CONSTRAINT messages_pkey PRIMARY KEY (message_id)
)