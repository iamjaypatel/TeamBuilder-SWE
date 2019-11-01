-- Drop Schema if Already Exists
DROP SCHEMA IF EXISTS team_builder CASCADE;

-- Create Schema
CREATE SCHEMA team_builder;

-- Create Seperate tables
CREATE TABLE team_builder.user
(
    userID     SERIAL NOT NULL PRIMARY KEY,
    username   VARCHAR(20) UNIQUE,
    pass       VARCHAR(20),
    first_name VARCHAR(20),
    last_name  VARCHAR(20),
    email      VARCHAR(20),
    phone_no   VARCHAR(20)
);

CREATE TABLE team_builder.projects
(
    projectID          SERIAL NOT NULL PRIMARY KEY,
    projectAdmin       INT    NOT NULL,
    projectName        VARCHAR(20),
    projectDescription VARCHAR(300),
    maxCapacity        INT DEFAULT 10,
    spaceTaken         INT NOT NULL DEFAULT 1,
    spaceAvailable     INT NOT NULL ,
    FOREIGN KEY (projectID) REFERENCES team_builder.projects,
    FOREIGN KEY (projectAdmin) REFERENCES team_builder.user

);

CREATE TABLE team_builder.project_involved
(
    userID    INT NOT NULL,
    projectID INT NOT NULL,
    PRIMARY KEY (userID, projectID),
    FOREIGN KEY (userID) REFERENCES team_builder.user,
    FOREIGN KEY (projectID) REFERENCES team_builder.projects
);


-- Test Inserts
INSERT INTO team_builder.user (username, pass, first_name, last_name, email, phone_no)
VALUES ('user1','password1','Jay', 'Patel', 'jay.patel@gmail.com', '123-223-1234');

INSERT INTO team_builder.user (username, pass, first_name, last_name, email, phone_no)
VALUES ('user2','password1','Jay', 'Patel', 'jay.patel@gmail.com', '123-223-1234');

INSERT INTO team_builder.projects(projectadmin, projectname, projectdescription, spaceAvailable)
VALUES (1,'ProjectName', 'ProjectDescriprion', '1');