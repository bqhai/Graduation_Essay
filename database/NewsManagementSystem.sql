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
	Status BIT NOT NULL
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
	UploadTime DATETIME,
	CrawledTime DATETIME,
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
INSERT INTO FacebookType VALUES(N'USER', N'Cá nhân', N'Tài khoản của người dùng thông thường')

--BlackList--
INSERT INTO WatchList VALUES(N'viettan', N'Việt Tân', N'https://www.facebook.com/viettan', N'PAGE', 1)
INSERT INTO WatchList VALUES(N'nhatkyyeunuoc1', N'Nhật Ký Yêu Nước', N'https://www.facebook.com/nhatkyyeunuoc1', N'PAGE', 1)
INSERT INTO WatchList VALUES(N'nhabaocongdan', N'Góc nhìn báo chí - Công dân', N'https://www.facebook.com/groups/nhabaocongdan/', N'GR', 1)
INSERT INTO WatchList VALUES(N'DuaLeo.Stand.up.comedian', N'Dưa Leo - Stand up comedian', N'https://www.facebook.com/DuaLeo.Stand.up.comedian', N'PAGE', 1)
INSERT INTO WatchList VALUES(N'1752456318197543', N'Xây Dựng Đảng', N'https://www.facebook.com/groups/1752456318197543', N'GR', 1)
INSERT INTO WatchList VALUES(N'phapluatvacuocsong.vn', N'Pháp luật & Cuộc sống', N'https://www.facebook.com/phapluatvacuocsong.vn', N'PAGE', 1)
INSERT INTO WatchList VALUES(N'cafekubua2', N'Cafe Ku Búa + Friends', N'https://www.facebook.com/cafekubua2', N'PAGE', 1)
INSERT INTO WatchList VALUES(N'TamConXuyenDiep', N'Tam Côn Xuyên Diệp', N'https://www.facebook.com/groups/TamConXuyenDiep', N'GR', 1)
INSERT INTO WatchList VALUES(N'187530275233978', N'BÀN LUẬN về KINH TẾ - CHÍNH TRỊ 2', N'https://www.facebook.com/groups/187530275233978', N'GR', 1)
INSERT INTO WatchList VALUES(N'kinhtechinhtrixahoivn', N'Bàn Luận về Kinh Tế - Chính Trị', N'https://www.facebook.com/groups/kinhtechinhtrixahoivn', N'GR', 1)
INSERT INTO WatchList VALUES(N'1648199831900386', N'Triệt Hạ Bò Đỏ', N'https://www.facebook.com/groups/1648199831900386/', N'GR', 1)
INSERT INTO WatchList VALUES(N'didoicongly', N'Lê Chí Thành', N'https://www.facebook.com/didoicongly/', N'PAGE', 1)
INSERT INTO WatchList VALUES(N'bao.luong.5011516', N'Luong Quang Bao', N'https://www.facebook.com/bao.luong.5011516', N'USER', 1)
INSERT INTO WatchList VALUES(N'thuc.tranhuynhduy', N'Trần Huỳnh Duy Thức', N'https://www.facebook.com/thuc.tranhuynhduy', N'USER', 1)
INSERT INTO WatchList VALUES(N'BinhLuanVeDangCongSan', N'Bình Luận Về Đảng Cộng Sản', N'https://www.facebook.com/BinhLuanVeDangCongSan', N'PAGE', 1)
INSERT INTO WatchList VALUES(N'vietnamconghoa123', N'Việt Nam Cộng Hòa', N'https://www.facebook.com/vietnamconghoa123', N'PAGE', 1)
INSERT INTO WatchList VALUES(N'90trieunguoi', N'VIỆT NAM DÂN CHỦ', N'https://www.facebook.com/90trieunguoi', N'PAGE', 1)
INSERT INTO WatchList VALUES(N'HuyFreedomSaigon', N'Huỳnh Quốc Huy (John Whale)', N'https://www.facebook.com/HuyFreedomSaigon', N'USER', 1)
INSERT INTO WatchList VALUES(N'mothermushroom', N'Mẹ Nấm', N'https://www.facebook.com/mothermushroom/', N'USER', 1)
INSERT INTO WatchList VALUES(N'lukhach', N'Nguyen Huy Vu', N'https://www.facebook.com/lukhach', N'USER', 1)
INSERT INTO WatchList VALUES(N'thong.luan.1', N'Tập Hợp Dân Chủ Đa Nguyên', N'https://www.facebook.com/thong.luan.1', N'PAGE', 1)

--NewsLabel--
INSERT INTO NewsLabel VALUES(N'TTH', N'Thể thao')
INSERT INTO NewsLabel VALUES(N'AN', N'Âm nhạc')
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
