CREATE OR ALTER PROC sp_init_schema
AS
BEGIN

    DROP TABLE IF EXISTS tblChannels
    ;

    CREATE TABLE tblChannels
    (
        id INT NOT NULL IDENTITY(1,1) PRIMARY KEY,
        channel_name VARCHAR(100),
        "url" VARCHAR(1000),
        is_active BIT,
        date_added DATETIME
    );

    PRINT 'Channel Table created successfully!'

    INSERT INTO tblChannels
        (channel_name, url, is_active, date_added)
    VALUES
        ('MBC 1'
      , 'https://d3o3cim6uzorb4.cloudfront.net/out/v1/0965e4d7deae49179172426cbfb3bc5e/index.m3u8'
      , 1
      , GETDATE()
);

END