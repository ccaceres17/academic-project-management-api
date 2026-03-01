-- Role catalog (Student, Teacher, Coordinator)
CREATE TABLE role (
    id_role SERIAL PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Project status catalog (Active, In Review, Finished, Cancelled)
CREATE TABLE project_status (
    id_status SERIAL PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Research lines catalog
CREATE TABLE research_line (
    id_research_line SERIAL PRIMARY KEY,
    research_line_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Document types catalog
CREATE TABLE document_type (
    id_document_type SERIAL PRIMARY KEY,
    document_type_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- Project role catalog (Leader, Researcher, Tutor)
CREATE TABLE project_role (
    id_project_role SERIAL PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- Delivery status catalog (Pending, Delivered, Approved, etc.)
CREATE TABLE delivery_status (
    id_delivery_status SERIAL PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);


-- ============================================================
--  USERS
-- ============================================================

-- Main user table
CREATE TABLE user_account (
    id_user SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    phone VARCHAR(20),
    id_role INTEGER NOT NULL,
    is_active BOOLEAN NOT NULL DEFAULT TRUE,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),

    CONSTRAINT fk_user_role
    FOREIGN KEY (id_role) REFERENCES role(id_role)
);

-- Student table (inherits from user_account)
CREATE TABLE student (
    id_user INTEGER PRIMARY KEY,
    semester INTEGER NOT NULL,

    CONSTRAINT fk_student_user
    FOREIGN KEY (id_user) REFERENCES user_account(id_user)
);


-- ============================================================
--  PROJECTS
-- ============================================================

-- Main project table
CREATE TABLE project (
    id_project SERIAL PRIMARY KEY,
    project_name VARCHAR(200) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    id_status INTEGER NOT NULL,
    id_research_line INTEGER,
    created_by INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),

    FOREIGN KEY (id_status) REFERENCES project_status(id_status),
    FOREIGN KEY (id_research_line) REFERENCES research_line(id_research_line),
    FOREIGN KEY (created_by) REFERENCES user_account(id_user)
);


-- ============================================================
--  PROJECT - USER RELATIONSHIP (Many-to-Many)
-- ============================================================

CREATE TABLE project_user (
    id_project_user SERIAL PRIMARY KEY,
    id_project INTEGER NOT NULL,
    id_user INTEGER NOT NULL,
    id_project_role INTEGER NOT NULL,
    assigned_date DATE NOT NULL DEFAULT CURRENT_DATE,

    FOREIGN KEY (id_project) REFERENCES project(id_project),
    FOREIGN KEY (id_user) REFERENCES user_account(id_user),
    FOREIGN KEY (id_project_role) REFERENCES project_role(id_project_role),

    CONSTRAINT unique_project_user UNIQUE (id_project, id_user)
);


-- ============================================================
--  DOCUMENTS
-- ============================================================

CREATE TABLE document (
    id_document SERIAL PRIMARY KEY,
    id_project INTEGER NOT NULL,
    id_user INTEGER NOT NULL,
    id_document_type INTEGER NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL,
    description TEXT,
    uploaded_at TIMESTAMP NOT NULL DEFAULT NOW(),

    FOREIGN KEY (id_project) REFERENCES project(id_project),
    FOREIGN KEY (id_user) REFERENCES user_account(id_user),
    FOREIGN KEY (id_document_type) REFERENCES document_type(id_document_type)
);


-- ============================================================
--  PROGRESS & COMMENTS
-- ============================================================

CREATE TABLE progress (
    id_progress SERIAL PRIMARY KEY,
    id_project INTEGER NOT NULL,
    id_user INTEGER NOT NULL,
    description TEXT NOT NULL,
    progress_percentage DECIMAL(5,2) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),

    FOREIGN KEY (id_project) REFERENCES project(id_project),
    FOREIGN KEY (id_user) REFERENCES user_account(id_user)
);

CREATE TABLE comment (
    id_comment SERIAL PRIMARY KEY,
    id_progress INTEGER NOT NULL,
    id_user INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),

    FOREIGN KEY (id_progress) REFERENCES progress(id_progress),
    FOREIGN KEY (id_user) REFERENCES user_account(id_user)
);


-- ============================================================
--  PROJECT STATUS HISTORY
-- ============================================================

CREATE TABLE project_status_history (
    id_history SERIAL PRIMARY KEY,
    id_project INTEGER NOT NULL,
    id_previous_status INTEGER,
    id_new_status INTEGER NOT NULL,
    changed_by INTEGER NOT NULL,
    changed_at TIMESTAMP NOT NULL DEFAULT NOW(),

    FOREIGN KEY (id_project) REFERENCES project(id_project),
    FOREIGN KEY (id_previous_status) REFERENCES project_status(id_status),
    FOREIGN KEY (id_new_status) REFERENCES project_status(id_status),
    FOREIGN KEY (changed_by) REFERENCES user_account(id_user)
);


-- ============================================================
--  SCHEDULED DELIVERIES
-- ============================================================

CREATE TABLE scheduled_delivery (
    id_delivery SERIAL PRIMARY KEY,
    id_project INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    due_date DATE NOT NULL,
    description TEXT,
    id_delivery_status INTEGER NOT NULL,

    FOREIGN KEY (id_project) REFERENCES project(id_project),
    FOREIGN KEY (id_delivery_status) REFERENCES delivery_status(id_delivery_status)
);

-- ============================================================
--  TEST DATA FOR PROFESSOR VALIDATION
--  (Basic Inserts & Queries)
-- ============================================================

-- =====================
--  TEST 1: Insert Role and User
-- =====================

-- Insert a role
INSERT INTO role (role_name, description)
VALUES ('Student', 'Undergraduate student');

-- Insert a user with that role
INSERT INTO user_account (first_name, last_name, email, password_hash, id_role)
VALUES ('Camila', 'Caceres', 'camila@test.com', 'hashed_password_example', 1);

-- Validate
SELECT * FROM user_account;



-- =====================
--  TEST 2: Create Project and Assign User
-- =====================

-- Insert project status
INSERT INTO project_status (status_name)
VALUES ('Active');

-- Insert project
INSERT INTO project (project_name, start_date, id_status, created_by)
VALUES ('AI Research Project', CURRENT_DATE, 1, 1);

-- Insert project role
INSERT INTO project_role (role_name)
VALUES ('Leader');

-- Assign user to project
INSERT INTO project_user (id_project, id_user, id_project_role)
VALUES (1, 1, 1);

-- Validate relationship
SELECT 
    p.project_name,
    u.first_name,
    pr.role_name
FROM project_user pu
JOIN project p ON pu.id_project = p.id_project
JOIN user_account u ON pu.id_user = u.id_user
JOIN project_role pr ON pu.id_project_role = pr.id_project_role;



-- =====================
--  TEST 3: Insert Progress and Comment
-- =====================

-- Insert progress
INSERT INTO progress (id_project, id_user, description, progress_percentage)
VALUES (1, 1, 'Initial research completed', 25.00);

-- Insert comment
INSERT INTO comment (id_progress, id_user, content)
VALUES (1, 1, 'Good progress so far');

-- Validate
SELECT 
    p.project_name,
    prg.description,
    c.content
FROM comment c
JOIN progress prg ON c.id_progress = prg.id_progress
JOIN project p ON prg.id_project = p.id_project;