
class Config():
    SECRET_KEY = "dKiC2p8lC2ZjnWJPs09mFbUwgkxk"
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "postgres://hzpcmpfb:dKiC2p8lC2ZjnWJPs09mFbUwgkxk--Iy@raja.db.elephantsql.com:5432/hzpcmpfb"

#dict para las diferentes configuraciones

config = {
    'development': DevelopmentConfig
}
