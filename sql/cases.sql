USE `nlrb_data`;
CREATE TABLE IF NOT EXISTS `cases` (
    `id` INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
    `case_type` TEXT,
    `region` TEXT,
    `case_number` VARCHAR(64) UNIQUE NOT NULL,
    `case_name` TEXT,
    `case_status` TEXT,
    `date_filed` DATE,
    `date_closed` DATE,
    `reason_closed` TEXT,
    `city` TEXT,
    `states_and_territories` TEXT,
    `employees_involved` TEXT,
    `allegations_raw` TEXT,
    `participants_raw` TEXT,
    `docket_activity_raw` TEXT,
    `union_name` TEXT,
    `unit_sought` TEXT,
    `voters` INT,
    `allegations_parse_error` BOOLEAN,
    `participants_parse_error` BOOLEAN,
    `docket_activity_parse_error` BOOLEAN
) ENGINE=InnoDB CHARSET=utf8mb4
