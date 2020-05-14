

from toutiao import TTBot

if __name__ == '__main__':
    bot = TTBot()
    print('搜索用户',bot.search('美女',kind='LIVE'))
    print('用户信息：',bot.get_user_info('67845295779'))
    print('用户粉丝：',bot.get_user_followers('5857262808',offset=20))
    print('用户关注：',bot.get_user_followings('5857262808',offset=20))
    print('用户相关用户推荐：',bot.get_recommend_users('67845295779'))
    print('用户文章：',bot.get_user_posts('67845295779'))
    print('用户所有作品：',bot.get_user_posts('67845295779',kind='ALL'))
    print('用户视频：',bot.get_user_posts('67845295779',kind='VIDEO'))
    print('用户小视频：',bot.get_user_posts('5857262808',kind='SHORTVIDEO'))
    print('用户问答：',bot.get_user_posts('5857262808',kind='WENDA'))
    print('文章信息：',bot.get_item_info('6771975338621665796'))
    print('文章评论：',bot.get_item_comments('6771975338621665796'))
    # print('发送登录验证码：',bot.send_sms_code('xxx'))
    # print('短信验证码登录：',bot.login_by_sms_code('xxx','8224'))
    # print('短信验证码修改密码：',bot.send_sms_code('xxx','xxx'))
    # print('修改密码：', bot.set_password_by_sms_code('xxxxx', '2566'))
    # print('密码登录：',bot.login_by_password('XXX','password'))


