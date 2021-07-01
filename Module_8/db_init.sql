-- Milo Blake
-- 06/30/2021
-- MySQL instructions

-- drop test user if exits
drop USER if exists 'pysports_user'@'localhost';

-- create pysports_user and grant them all privileges to the pysports database
create USER 'pysports_user'@'localhost' IDENTIFIED with mysql_native_password by 'MySQLpassword!!';

-- grant all privileges to the pysports database to user pysports_user on localhost
grant ALL PRIVILEGES on pysports.* to'pysports_user'@'localhost';

-- drop tables if they are present
drop table if exists team;
drop table if exists player;

-- create the team table
create table team (
    team_id             int             not null        auto_increment,
    team_name           varchar(75)     not null,
    mascot              varchar(75)     not null,
    PRIMARY KEY(team_id) 
);

-- create the player table and set the foreign key
create table player (
    player_id           int             not null        auto_increment,
    first_name          varchar(75)     not null,
    last_name           varchar(75)     not null,
    team_id             int             not null,
    PRIMARY KEY(player_id),
    CONSTRAINT fk_team
    FOREIGN KEY(team_id)
            REFERENCES team(team_id)
);

-- insert team records
INSERT INTO team(team_name, mascot)
    VALUES('Team Evil', 'Skeleton');

INSERT INTO team(team_name, mascot)
    VALUES('Team Good', 'Lotus');

-- insert player records
INSERT INTO player(first_name, last_name, team_id)
    VALUES('BadGuy', 'One', (select team_id from team where team_name = 'Team Evil'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('BadGuy', 'Two', (select team_id from team where team_name = 'Team Evil'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('BadGuy', 'Three', (select team_id from team where team_name = 'Team Evil'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('GoodGuy', 'One', (select team_id from team where team_name = 'Team Good'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('GoodGuy', 'Two', (select team_id from team where team_name = 'Team Good'));

INSERT INTO player(first_name, last_name, team_id)
    VALUES('GoodGuy', 'Three', (select team_id from team where team_name = 'Team Good'));

