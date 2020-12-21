CREATE DATABASE NewsManagementSystem
GO

USE NewsManagementSystem
GO

CREATE TABLE Account
(	
	Username NVARCHAR(100) PRIMARY KEY,
	Password NVARCHAR(200) NOT NULL,
	AccountType INT NOT NULL
)
GO

CREATE TABLE FacebookType
(
	FacebookTypeID NVARCHAR(100) PRIMARY KEY,
	FacebookTypeName NVARCHAR(200) NOT NULL,
	Description NVARCHAR(500),	
)
GO

CREATE TABLE WatchList
(
	FacebookID NVARCHAR(100) PRIMARY KEY,
	FacebookName NVARCHAR(500),
	FacebookUrl NVARCHAR(500) UNIQUE,
	FacebookTypeID NVARCHAR(100),
	Status BIT NOT NULL,
	InBlackList BIT NOT NULL
	FOREIGN KEY(FacebookTypeID) REFERENCES FacebookType(FacebookTypeID)
)
GO

CREATE TABLE NewsLabel
(	
	NewsLabelID NVARCHAR(100) PRIMARY KEY,
	NewsLabelName NVARCHAR(200) NOT NULL,
)
GO

CREATE TABLE SentimentLabel
(
	SentimentLabelID NVARCHAR(100) PRIMARY KEY,
	SentimentLabelName NVARCHAR(200) NOT NULL,
)

CREATE TABLE Post
(
	PostID NVARCHAR(100) PRIMARY KEY,
	PostUrl NVARCHAR(500),
	UserUrl NVARCHAR(500),
	PostContent NVARCHAR(MAX),
	Image NVARCHAR(MAX),
	UploadTime NVARCHAR(200),
	TotalLikes INT,
	TotalComment INT,
	TotalShare INT,
	FacebookID NVARCHAR(100),
	NewsLabelID NVARCHAR(100) NOT NULL,
	SentimentLabelID NVARCHAR(100) NOT NULL,

	FOREIGN KEY(FacebookID) REFERENCES WatchList(FacebookID),
	FOREIGN KEY(NewsLabelID) REFERENCES NewsLabel(NewsLabelID),
	FOREIGN KEY(SentimentLabelID) REFERENCES SentimentLabel(SentimentLabelID)

)

-----INSERTDATA-----
--SystemAccount--
INSERT INTO Account VALUES(N'admin', N'123456', 1)
INSERT INTO Account VALUES(N'bqhai01', N'123456', 0)
INSERT INTO Account VALUES(N'bqhai02', N'123456', 0)
INSERT INTO Account VALUES(N'bqhai03', N'123456', 0)
--FacebookType--
INSERT INTO FacebookType VALUES(N'PAGE', N'Trang', NULL)
INSERT INTO FacebookType VALUES(N'GR', N'Nhóm công khai', N'Public groups, nơi mọi người có thể xem tất cả nội dung và các thành viên.')
INSERT INTO FacebookType VALUES(N'CGR', N'Nhóm kín', N'Closed groups, nơi mọi người có thể xem tên nhóm và thành viên, nhưng không xem được nội dung của nhóm.')
INSERT INTO FacebookType VALUES(N'PGR', N'Nhóm bí mật', N'Secret groups, nơi bạn phải được mời để có thể tham gia vào nhóm.')
INSERT INTO FacebookType VALUES(N'USER', N'Tài khoản người dùng', N'Tài khoản của người dùng thông thường')

--BlackList--
INSERT INTO WatchList VALUES(N'viettan', N'Việt Tân', N'https://www.facebook.com/viettan', N'PAGE', 1, 0)
INSERT INTO WatchList VALUES(N'nhatkyyeunuoc1', N'Nhật Ký Yêu Nước', N'https://www.facebook.com/nhatkyyeunuoc1', N'PAGE', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan/', N'GR', 1, 0)

INSERT INTO WatchList VALUES(N'nhabaocongdan2', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan2/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan3', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan3/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan4', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan4/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan5', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan5/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan6', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan6/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan7', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan7/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan8', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan8/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan9', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan9/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan10', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan10/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan11', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan11/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan12', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan12/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan13', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan13/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan14', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan14/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan15', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan15/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan16', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan16/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan17', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan17/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan18', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan18/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan19', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan19/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan20', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan20/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan21', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan21/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan22', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan22/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan23', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan23/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan24', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan24/', N'GR', 1, 0)
INSERT INTO WatchList VALUES(N'nhabaocongdan25', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan25/', N'GR', 1, 0)
--NewsLabel--
INSERT INTO NewsLabel VALUES(N'TTH', N'Thể thao')
INSERT INTO NewsLabel VALUES(N'AN', N'Âm nhạc')
INSERT INTO NewsLabel VALUES(N'NS', N'Nhịp sống')
INSERT INTO NewsLabel VALUES(N'CN', N'Công nghệ')
INSERT INTO NewsLabel VALUES(N'TS', N'Thời sự')
INSERT INTO NewsLabel VALUES(N'TG', N'Thế giới')
INSERT INTO NewsLabel VALUES(N'TTR', N'Thời trang')
INSERT INTO NewsLabel VALUES(N'DL', N'Du lịch')
INSERT INTO NewsLabel VALUES(N'ST', N'Sống trẻ')
INSERT INTO NewsLabel VALUES(N'GD', N'Giáo dục')
INSERT INTO NewsLabel VALUES(N'KD', N'Kinh Doanh')
INSERT INTO NewsLabel VALUES(N'PL', N'Pháp luật')
INSERT INTO NewsLabel VALUES(N'GT', N'Giải trí')
INSERT INTO NewsLabel VALUES(N'PA', N'Phim ảnh')
INSERT INTO NewsLabel VALUES(N'XE', N'Xe')
INSERT INTO NewsLabel VALUES(N'AT', N'Ẩm thực')
INSERT INTO NewsLabel VALUES(N'SK', N'Sức khỏe')
INSERT INTO NewsLabel VALUES(N'XB', N'Xuất bản')
INSERT INTO NewsLabel VALUES(N'ANTT', N'An ninh trật tự')
INSERT INTO NewsLabel VALUES(N'ANQG', N'An ninh quốc gia')

--SentimentLabel--
INSERT INTO SentimentLabel VALUES(N'POS', N'Tích cực')
INSERT INTO SentimentLabel VALUES(N'NEG', N'Tiêu cực')
INSERT INTO SentimentLabel VALUES(N'NEU', N'Bình thường')
