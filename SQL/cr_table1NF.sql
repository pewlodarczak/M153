CREATE TABLE customers (
    id                            INT(6) AUTO_INCREMENT PRIMARY KEY,
    name                          VARCHAR(255),
    industry                      VARCHAR(255),
    contact_person_id             INT(6),
    contact_person                VARCHAR(300),
    contact_person_role           VARCHAR(300),
    phone_number                  VARCHAR(12),
    address                       VARCHAR(255),
    city                          VARCHAR(255),
    zip                           VARCHAR(5)
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