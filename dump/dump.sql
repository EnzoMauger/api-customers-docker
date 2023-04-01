CREATE TABLE IF NOT EXISTS customers (
	id int(11) NOT NULL,
	firstname varchar(200) NOT NULL,
	name varchar(200) NOT NULL,
	email varchar(200) NOT NULL,
	created datetime NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
ALTER TABLE customers ADD PRIMARY KEY (id);
ALTER TABLE customers MODIFY id int(11) NOT NULL AUTO_INCREMENT;
