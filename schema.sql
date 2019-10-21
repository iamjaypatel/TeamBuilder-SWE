-- Drop Schema if Already Exists
DROP SCHEMA IF EXISTS team_builder CASCADE;

-- Create Schema
CREATE SCHEMA team_builder;

-- Create Seperate tables
CREATE TABLE team_builder.User
(
    userID     SERIAL NOT NULL,
    username   VARCHAR(20),
    pass       VARCHAR(20),
    first_name VARCHAR(20),
    last_name  VARCHAR(20),
    phone_no   VARCHAR(20)
);

CREATE TABLE team_builder.Projects
(
);

CREATE TABLE team_builder.Project_Involved
(
    uID SERIAL
);

