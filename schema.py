instructions = [
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS user;',
    'DROP TABLE IF EXISTS curses;',
    'DROP TABLE IF EXISTS cursesregister;',
    'SET FOREIGN_KEY_CHECKS=1;',
    """
    CREATE TABLE user (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(50) UNIQUE NOT NULL,
        tel VARCHAR(18) NOT NULL,
        password VARCHAR(1000) NOT NULL,
        user_type INT NOT NULL,
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        confirmed boolean NOT NULL
    )
    """,
    """
    CREATE TABLE curses (
        id INT PRIMARY KEY AUTO_INCREMENT,
        curse_name VARCHAR(50) NOT NULL,
        created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        teacher INT NOT NULL,
        FOREIGN KEY (teacher) REFERENCES user (id)
    )
    """,
    """
    CREATE TABLE cursesregister (
        id INT PRIMARY KEY AUTO_INCREMENT,
        enrolled_user INT NOT NULL,
        curse INT NOT NULL,
        enrolled_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        progress int NOT NULL,
        FOREIGN KEY (curse) REFERENCES curses (id),
        FOREIGN KEY (enrolled_user) REFERENCES user (id)
    )
    """,
    """
    CREATE TABLE notifications (
        id INT PRIMARY KEY AUTO_INCREMENT,
        notification VARCHAR(50) NOT NULL
    )
    """,
    """
    CREATE TABLE usersnotifications (
        id INT PRIMARY KEY AUTO_INCREMENT,
        not_name INT NOT NULL,
        not_user INT NOT NULL,
        curse_from INT NOT NULL,
        not_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
        not_check BOOLEAN NOT NULL,
        FOREIGN KEY (not_name) REFERENCES notifications (id),
        FOREIGN KEY (not_user) REFERENCES user (id),
        FOREIGN KEY (curse_from) REFERENCES curses (id)
    )
    """
]