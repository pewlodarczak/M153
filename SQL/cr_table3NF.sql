CREATE TABLE customers (
    id                            INT(6) AUTO_INCREMENT PRIMARY KEY,
    name                          VARCHAR(255),
    industry                      VARCHAR(255),
    contact_person_id             INT(6),
    phone_number                  VARCHAR(12),
    address                       VARCHAR(255),
    zip                           VARCHAR(5)
);

CREATE TABLE zips (
    zip   VARCHAR(5) PRIMARY KEY, 
    city  VARCHAR(255)
);

CREATE TABLE project_feedbacks (
    id                  INT(6) AUTO_INCREMENT PRIMARY KEY,
    project_id          INT(6), 
    customer_id         INT(6),
    project_feedback    TEXT
);

CREATE TABLE projects (
    id                  INT(6) AUTO_INCREMENT PRIMARY KEY,
    name                VARCHAR(300),
    start_date          DATE,
    end_date            DATE
);

CREATE TABLE contact_persons (
    id              INT(6) PRIMARY KEY,
    name            VARCHAR(300),
    role            VARCHAR(300),
    phone_number    VARCHAR(15)
);