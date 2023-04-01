CREATE OR ALTER PROC sp_init_schema
AS
BEGIN

DROP TABLE IF EXISTS tblChannels ;

CREATE TABLE tblChannels
(
    id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
    channel_name VARCHAR(100),
    "url" VARCHAR(1000),
    is_active BIT,
    date_added DATETIME
);

PRINT 'Channel Table Created successfully!'
END