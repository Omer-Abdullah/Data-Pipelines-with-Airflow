CREATE TABLE public.artists (
	artistid varchar(256) NOT NULL,
	name varchar(256),
	location varchar(256),
	lattitude numeric(18,0),
	longitude numeric(18,0)
);

CREATE TABLE public.songplays (
	playid int IDENTITY(0,1) PRIMARY KEY,
	start_time timestamp NOT NULL,
	userid int NOT NULL,
	"level" varchar,
	songid varchar,
	artistid varchar,
	sessionid int4,
	location varchar,
	user_agent varchar,
);

CREATE TABLE public.songs (
	songid varchar(256) NOT NULL,
	title varchar(256),
	artistid varchar(256),
	"year" int4,
	duration numeric(18,0),
	CONSTRAINT songs_pkey PRIMARY KEY (songid)
);

CREATE TABLE public.staging_events (
	artist varchar,
	auth varchar,
	firstname varchar,
	gender varchar,
	iteminsession varchar,
	lastname varchar,
	length float,
	"level" varchar,
	location varchar,
	"method" varchar,
	page varchar,
	registration varchar,
	sessionid int,
	song varchar,
	status int,
	ts bigint,
	useragent varchar,
	userid int
);


CREATE TABLE public.staging_songs (
	num_songs int4,
	artist_id varchar(256),
	artist_name varchar(256),
	artist_latitude numeric(18,0),
	artist_longitude numeric(18,0),
	artist_location varchar(256),
	song_id varchar(256),
	title varchar(256),
	duration numeric(18,0),
	"year" int4
);

CREATE TABLE public.users (
	userid int4 NOT NULL,
	first_name varchar(256),
	last_name varchar(256),
	gender varchar(256),
	"level" varchar(256),
	CONSTRAINT users_pkey PRIMARY KEY (userid)
);

CREATE TABLE public.time (
start_time timestamp NOT NULL,
hour int4 NOT NULL,
day int4 NOT NULL,
week int4 NOT NULL,
month int4 NOT NULL,
year int4 NOT NULL,
dayofweek int4 NOT NULL,
);




