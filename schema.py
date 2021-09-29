instructions = [
    'SET FOREIGN_KEY_CHECKS=0;',
    'DROP TABLE IF EXISTS user;',
    'DROP TABLE IF EXISTS curses;',
    'DROP TABLE IF EXISTS cursesregister;',
    'SET FOREIGN_KEY_CHECKS=1;',
    """
    CREATE TABLE user (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(50) UNIQUE NOT NULL,
        email VARCHAR(50) UNIQUE NOT NULL,
        tel VARCHAR(18) UNIQUE NOT NULL,
        password VARCHAR(1000) NOT NULL,
        user_type INT NOT NULL
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
        completed BOOLEAN NOT NULL,
        FOREIGN KEY (curse) REFERENCES curses (id),
        FOREIGN KEY (enrolled_user) REFERENCES user (id)
    )
    """
]