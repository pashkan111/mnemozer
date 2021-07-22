CREATE TABLE `User` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`phone` VARCHAR(255) NOT NULL UNIQUE,
	`telegram` VARCHAR(255) NOT NULL UNIQUE,
	`name` VARCHAR(255) NOT NULL,
	`email` VARCHAR(255) NOT NULL,
	`registration` DATETIME NOT NULL,
	`password` VARCHAR(255) NOT NULL,
	`messengers` VARCHAR(255) NOT NULL DEFAULT '[]',
	`is_subscriber` BOOLEAN NOT NULL,
	`subscribe_until` DATETIME NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Note` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL,
	`created` DATETIME NOT NULL,
	`text` TEXT NOT NULL,
	`geo_lat` FLOAT NOT NULL,
	`geo_lng` FLOAT NOT NULL,
	`is_reminder` BOOLEAN NOT NULL,
	`reminder_date` DATETIME NOT NULL,
	`is_viewed` BOOLEAN NOT NULL,
	`viewed_date` DATETIME NOT NULL,
	`is_deleted` BOOLEAN NOT NULL,
	`deleted_date` DATETIME NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Logs` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL,
	`datetime` TIMESTAMP NOT NULL,
	`action` VARCHAR(255) NOT NULL,
	`equipment_id` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Equipment` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL,
	`title` VARCHAR(255) NOT NULL,
	`added` DATETIME NOT NULL,
	`header` TEXT NOT NULL,
	`token` VARCHAR(255) NOT NULL UNIQUE,
	`expiration` DATETIME,
	`deleted` BOOLEAN NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `Billing` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL,
	`datetime` DATETIME NOT NULL,
	`sum` FLOAT NOT NULL,
	`subscribe_type` VARCHAR(255) NOT NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE `NoteMedia` (
	`id` INT NOT NULL AUTO_INCREMENT,
	`user_id` INT NOT NULL,
	`note_id` INT NOT NULL,
	`added` DATETIME NOT NULL,
	`name` VARCHAR(255) NOT NULL,
	`file` VARCHAR(255) NOT NULL,
	`file_type` VARCHAR(255) NOT NULL,
	`mine` VARCHAR(255) NOT NULL,
	`is_deleted` BOOLEAN NOT NULL,
	`deleted_date` DATETIME NOT NULL,
	PRIMARY KEY (`id`)
);

ALTER TABLE `Note` ADD CONSTRAINT `Note_fk0` FOREIGN KEY (`user_id`) REFERENCES `User`(`id`);

ALTER TABLE `Logs` ADD CONSTRAINT `Logs_fk0` FOREIGN KEY (`user_id`) REFERENCES `User`(`id`);

ALTER TABLE `Logs` ADD CONSTRAINT `Logs_fk1` FOREIGN KEY (`equipment_id`) REFERENCES `Equipment`(`id`);

ALTER TABLE `Equipment` ADD CONSTRAINT `Equipment_fk0` FOREIGN KEY (`user_id`) REFERENCES `User`(`id`);

ALTER TABLE `Billing` ADD CONSTRAINT `Billing_fk0` FOREIGN KEY (`user_id`) REFERENCES `User`(`id`);

ALTER TABLE `NoteMedia` ADD CONSTRAINT `NoteMedia_fk0` FOREIGN KEY (`user_id`) REFERENCES `User`(`id`);

ALTER TABLE `NoteMedia` ADD CONSTRAINT `NoteMedia_fk1` FOREIGN KEY (`note_id`) REFERENCES `Note`(`id`);

