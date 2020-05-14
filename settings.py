#coding:utf-8

"""
*author:linkin
*date:20200202
"""

SUIT = {
        (700,771):{

            #用户资料 接口的请求路径
            'USER_PROFILE':'/user/profile/homepage/v7/',
            #用户发布作品（全部/视频/文章/小视频等） 接口的请求路径
            'USER_POSTS':'/api/feed/profile/v1/',
            # 用户粉丝 接口的请求路径
            'USER_FOLLOWERS':'/user/relation/fans/v2/',
            # 用户关注 接口的请求路径
            'USER_FOLLOWINGS':'/user/relation/following/v2/',
            # 视频/文章评论 接口的请求路径
            'VIDEO_COMMENTS':'/article/v4/tab_comments/',
        },
        (700,700):{

            # 用户文章信息 接口的请求路径
            'ARTICLE_INFO':'/2/article/information/v25/',
            # 用户信息 接口的请求路径
            'USER_INFO':'/user/profile/homepage/v7/',
            # 相关用户推荐 接口的请求路径
            'USER_RECOMMEND':'/user/relation/user_recommend/v1/supplement_recommends/',
            # 关键词搜索 接口的请求路径
            'SEARCH':'/api/search/content/',
            # 分类推荐流 接口的请求路径
            'FEEDS':'/api/news/feed/v88/',

        }

    }

SEC_SUIT = {

    (700,700):{
        'SEND_SMS_CODE':'/passport/mobile/send_code/',
        'SMS_LOGIN':'/passport/mobile/sms_login/',
        'SMS_RESET_PWD':'/passport/password/change/',
        'PWD_LOGIN':'/passport/mobile/login/',
    }
}

HOSTS = {

    700:'https://is-hl.snssdk.com',
    771:'https://api3-normal-c-lf.snssdk.com',

}

COMMENT_HOSTS = {

    700:'https://ic.snssdk.com',
    771:'https://api100-quic-c.snssdk.com',

}

SEC_HOSTS = {

    700:'https://security-hl.snssdk.com',

}

VCOMMENTS = 'https://is.snssdk.com/article/v2/tab_comments/'
VINFO = 'https://is.snssdk.com/video/app/user/home/v4/'
VVINFO ='https://is.snssdk.com/video/app/article/information/v23/'

UA = 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; {device_type} Build/{builder}) NewsArticle/{app_version} okhttp/3.10.0.{version}'

