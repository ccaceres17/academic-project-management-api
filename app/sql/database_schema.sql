-- ============================================================
-- ROLE
-- Defines system roles such as Student, Teacher, Coordinator
-- ============================================================

CREATE TABLE role (
    id_role SERIAL PRIMARY KEY,
    role_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);
CREATE TABLE faculty (
  id_faculty SERIAL PRIMARY KEY,
  faculty_name VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE program (
  id_program SERIAL PRIMARY KEY,
  program_name VARCHAR(100) NOT NULL,
  id_faculty INTEGER,
  
  FOREIGN KEY (id_faculty)
  REFERENCES faculty(id_faculty)
);

CREATE TABLE project_status (
    id_status SERIAL PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- ============================================================
-- RESEARCH LINE
-- Academic research areas (AI, Cybersecurity, Data Science)
-- ============================================================

CREATE TABLE research_line (
    id_research_line SERIAL PRIMARY KEY,
    research_line_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- ============================================================
-- RESEARCH GROUP (SEMILLERO)
-- Projects are developed inside research groups
-- ============================================================

CREATE TABLE research_group (
    id_research_group SERIAL PRIMARY KEY,
    research_group_name VARCHAR(150) NOT NULL UNIQUE,
    description TEXT,
    id_research_line INTEGER,
    created_by INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),

    FOREIGN KEY (id_research_line)
    REFERENCES research_line(id_research_line)
);

-- ============================================================
-- DOCUMENT TYPE
-- Defines document categories uploaded to projects
-- ============================================================

CREATE TABLE document_type (
    id_document_type SERIAL PRIMARY KEY,
    document_type_name VARCHAR(100) NOT NULL UNIQUE,
    description TEXT
);

-- ============================================================
-- DELIVERY STATUS
-- Status of project deliverables
-- ============================================================

CREATE TABLE delivery_status (
    id_delivery_status SERIAL PRIMARY KEY,
    status_name VARCHAR(50) NOT NULL UNIQUE,
    description TEXT
);

-- ============================================================
-- USER ACCOUNT
-- Stores all users of the system
-- ============================================================

CREATE TABLE user_account (
    id_user SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    phone VARCHAR(20),
    id_role INTEGER NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT NOW(),

    FOREIGN KEY (id_role)
    REFERENCES role(id_role)
);

-- ============================================================
-- STUDENT
-- Extension of user_account for students
-- ============================================================

CREATE TABLE student (
    id_user INTEGER PRIMARY KEY,
    semester INTEGER NOT NULL,

    FOREIGN KEY (id_user)
    REFERENCES user_account(id_user)
);

-- ============================================================
-- PROJECT
-- Central entity representing research projects
-- ============================================================

CREATE TABLE project (
    id_project SERIAL PRIMARY KEY,
    project_name VARCHAR(200) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    id_status INTEGER NOT NULL,
    id_research_group INTEGER,
    created_by INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),

    FOREIGN KEY (id_status)
    REFERENCES project_status(id_status),

    FOREIGN KEY (id_research_group)
    REFERENCES research_group(id_research_group),

    FOREIGN KEY (created_by)
    REFERENCES user_account(id_user)
);

-- ============================================================
-- PROJECT USER
-- Resolves the many-to-many relationship between
-- users and projects
-- ============================================================

CREATE TABLE project_user (
    id_project_user SERIAL PRIMARY KEY,
    id_project INTEGER NOT NULL,
    id_user INTEGER NOT NULL,
    id_role INTEGER NOT NULL,
    assigned_date DATE DEFAULT CURRENT_DATE,

    FOREIGN KEY (id_project)
    REFERENCES project(id_project),

    FOREIGN KEY (id_user)
    REFERENCES user_account(id_user),

    FOREIGN KEY (id_role)
    REFERENCES role(id_role),

    CONSTRAINT unique_project_user
    UNIQUE (id_project, id_user)
);

-- ============================================================
-- DOCUMENT
-- Stores files uploaded to a project
-- ============================================================

CREATE TABLE document (
    id_document SERIAL PRIMARY KEY,
    id_project INTEGER NOT NULL,
    id_user INTEGER NOT NULL,
    id_document_type INTEGER NOT NULL,
    file_name VARCHAR(255) NOT NULL,
    file_path TEXT NOT NULL,
    description TEXT,
    uploaded_at TIMESTAMP DEFAULT NOW(),

    FOREIGN KEY (id_project)
    REFERENCES project(id_project),

    FOREIGN KEY (id_user)
    REFERENCES user_account(id_user),

    FOREIGN KEY (id_document_type)
    REFERENCES document_type(id_document_type)
);

-- ============================================================
-- PROGRESS
-- Tracks progress updates in a project
-- ============================================================

CREATE TABLE progress (
    id_progress SERIAL PRIMARY KEY,
    id_project INTEGER NOT NULL,
    id_user INTEGER NOT NULL,
    description TEXT NOT NULL,
    progress_percentage DECIMAL(5,2) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),

    FOREIGN KEY (id_project)
    REFERENCES project(id_project),

    FOREIGN KEY (id_user)
    REFERENCES user_account(id_user)
);

-- ============================================================
-- COMMENT
-- Feedback related to progress updates
-- ============================================================

CREATE TABLE comment (
    id_comment SERIAL PRIMARY KEY,
    id_progress INTEGER NOT NULL,
    id_user INTEGER NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),

    FOREIGN KEY (id_progress)
    REFERENCES progress(id_progress),

    FOREIGN KEY (id_user)
    REFERENCES user_account(id_user)
);

-- ============================================================
-- PROJECT STATUS HISTORY
-- Tracks status changes of a project
-- ============================================================

CREATE TABLE project_status_history (
    id_history SERIAL PRIMARY KEY,
    id_project INTEGER NOT NULL,
    id_previous_status INTEGER,
    id_new_status INTEGER NOT NULL,
    changed_by INTEGER NOT NULL,
    changed_at TIMESTAMP DEFAULT NOW(),

    FOREIGN KEY (id_project)
    REFERENCES project(id_project),

    FOREIGN KEY (id_previous_status)
    REFERENCES project_status(id_status),

    FOREIGN KEY (id_new_status)
    REFERENCES project_status(id_status),

    FOREIGN KEY (changed_by)
    REFERENCES user_account(id_user)
);

-- ============================================================
-- SCHEDULED DELIVERY
-- Defines project deadlines and deliverables
-- ============================================================

CREATE TABLE scheduled_delivery (
    id_delivery SERIAL PRIMARY KEY,
    id_project INTEGER NOT NULL,
    title VARCHAR(255) NOT NULL,
    due_date DATE NOT NULL,
    description TEXT,
    id_delivery_status INTEGER NOT NULL,

    FOREIGN KEY (id_project)
    REFERENCES project(id_project),

    FOREIGN KEY (id_delivery_status)
    REFERENCES delivery_status(id_delivery_status)
);