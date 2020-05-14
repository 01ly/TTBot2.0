

# TTBot2.0

> 本项目纯属学习交流，严禁商业用途
>
> 返回样例数据因json格式化等部分原因 只摘取部分数据，完整数据可运行 `python TestFile.py`查看

## 更新历史
* 20200514 修复失效功能（用户信息/文章（视频）信息/文章（视频）评论），增加搜索功能
（不知道什么缘故，md无法正常解析文档json示例，故删除掉部分返回数据示例，需要查看可以看历史分支）
## Todo
* 增加评论点赞收藏等功能
* 增加关注取消关注拉黑等
* ~~增加搜索功能~~(已支持)
* 数据库支持

## 赞助支持

纯属个人维护，工作之余抽出时间进行维护（一般在周末和半夜）
> **Maybe you could buy me a cup of coffee :)**

alipay: ![aliapy](accessory/alipay.jpg)      wechat: ![wechat](accessory/wechat.png)

## 学习交流

- 微信公众号：刺派(微信号:pylinc)   
新开的公众号，分享关于python数据采集爬虫的技术经验,关注有惊喜
  
  ![公众号](accessory/qrcode.jpg)

- QQ 群: 刺派(qq群号:708736791)   
技术讨论交流 兼职接单

  ![QQ群](accessory/qq.png)
 
## 免责声明
* 本项目只作为娱乐学习使用，禁止使用本项目源码进行任何商业利用；
* 对使用本项目造成的一切风险及后果均由项目使用方负全责，请谨慎使用；

## 目录
* [0.发送登录短信验证码](#jump0)
* [1.使用短信验证码登录](#jump1)
* [2.使用账户密码登录](#jump2)
* [3.登录后修改账户密码](#jump3)
* [4.获取头条用户个人主页信息](#jump4)
* [5.获取头条用户相关用户推荐](#jump5)
* [6.获取头条用户所有发布作品](#jump6)
* [7.获取头条用户的视频](#jump7)
* [8.获取头条用户的文章](#jump8)
* [9.获取头条用户的问答](#jump9)
* [10.获取头条用户的小视频](#jump10)
* [11.获取头条用户的粉丝](#jump11)
* [12.获取头条用户的关注列表](#jump12)
* [13.获取头条多媒体（视频/文章等）信息](#jump13)
* [14.获取头条多媒体（视频/文章）的一级评论](#jump14)
* [15.关键词搜索](#jump15)


## <span id="jump0">0.发送登录短信验证码</span>

状态：**无需登录**

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
# 登录验证码
bot.send_sms_code('139****9484') 

```

返回示例：
```json5
{
	'data': {
		'mobile': '139****9484',
		'mobile_ticket': 'mobile_ticket_XFBP7VRGK2TT7F4ZXUC8WPZZ3HWRVHDD',
		'retry_time': 60
	},
	'message': 'success'
}
```

## <span id="jump1">1.使用短信验证码登录</span>

状态：**无需登录**

使用短信验证码获取方法 `bot.send_sms_code` 获得验证码

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
code = '2747' 
ret = bot.login_by_sms_code('139****9484',code)

```

返回示例：
```json5
{
	'data': {
		'app_id': 13,
		'user_id': 54009707197,
		'user_id_str': '54009707197',
		'name': '刺派',
		'screen_name': '刺派',
		'avatar_url': 'http://p3.pstatp.com/medium/fe480000747798606b4c',
		'user_verified': False,
		'verified_content': '',
		'verified_agency': '',
		'is_blocked': 0,
		'is_blocking': 0,
		'bg_img_url': 'http://p3.pstatp.com/origin/60e0000116e1e21ff9a',
		'gender': 1,
		'media_id': 1638092872195084,
		'user_auth_info': '',
		'industry': '',
		'area': '广东省广州市',
		'can_be_found_by_phone': 0,
		'mobile': '139****9484',
		'birthday': '20010506',
		'description': '公众号：pylinc,这是一个最好的时代，也是一个最差的时代',
		'new_user': 0,
		'session_key': 'xxxxxxxxxxxxxxxxxxxxxxxxx',
		'is_recommend_allowed': 1,
		'recommend_hint_message': '同时推荐给我的粉丝',
		'connects': [{
			'platform': 'weixin',
			'profile_image_url': 'http://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIUhTIh04uWrLFIUjtmEm0Hia0QdGb7rlMrjQeicGEnWDfa4kic8YdBc1EXE4zMbKNJB017JYn4WyI2g/132',
			'expired_time': 1562929171,
			'expires_in': 0,
			'platform_screen_name': 'linkin',
			'user_id': 54009707197,
			'platform_uid': 'ovT****lKQs',
			'modify_time': 1562921971
		}, {
			'platform': 'weixin',
			'profile_image_url': 'http://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTKRkOGk4ib4Pgew1V3SzvmcJxRWg4oDcr4oDXBZ2M4z96WN4f0MTfSJjQxibkEa8HvG0Q4DZicLBiaO3w/132',
			'expired_time': 1562929093,
			'expires_in': 0,
			'platform_screen_name': 'linkin',
			'user_id': 54009707197,
			'platform_uid': 'ovT******lKQs',
			'modify_time': 1562921893
		}, {
			'platform': 'weixin',
			'profile_image_url': 'http://thirdwx.qlogo.cn/mmopen/vi_32/Q0j4TwGTfTIib3CwsWs3QQjVFBMobpuaPc91sv1ETaTvgpyJOfr3f1b3MicFth5pvQmGWBVwcpevibGNOFLLcMqbQ/132',
			'expired_time': 1549558262,
			'expires_in': 0,
			'platform_screen_name': 'linkin\ue513',
			'user_id': 54009707197,
			'platform_uid': 'ov*****lKQs',
			'modify_time': 1549551062
		}],
		'followings_count': 0,
		'followers_count': 0,
		'visit_count_recent': 0,
		'skip_edit_profile': 0,
		'is_manual_set_user_info': False,
		'device_id': 0,
		'country_code': 0,
		'has_password': 0,
		'share_to_repost': -1,
		'user_decoration': '',
		'user_privacy_extend': 000000,
		'old_user_id': 54009707197,
		'old_user_id_str': '54009707197',
		'sec_user_id': 'MS************_4',
		'sec_old_user_id': 'MS***************_4',
		'vcd_account': 0,
		'vcd_relation': 0,
		'can_bind_visitor_account': False,
		'is_visitor_account': False,
		'is_only_bind_ins': False
	},
	'message': 'success'
}
```

## <span id="jump2">2. 使用账户密码登录</span>

状态：**无需登录**


调用示例：
```python
from toutiao import TTBot

bot = TTBot()
ret = bot.login_by_password('139****9484','123456')

```
如果返回：
```json5
{
	'data': {
		'captcha': '',
		'description': '为保证帐号安全，请使用手机验证码登录',
		'error_code': 1039,
		'mobile_ticket': '',
		'verify_mobile': ''
	},
	'message': 'error'
}
```
则多次重试，仍然返回以上结果使用短信验证码登录

正常返回示例：
```
结果同 1.使用短信验证码登录 返回结果一样
```

## <span id="jump3">3. 登录后修改账户密码</span>

状态：**需登录**

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
ret = bot.login_by_password('139****9484','123456')
bot.send_sms_code('139****9484',kind='PASSWORD')


# 获取短信验证码 code
code = '2245'
ret = bot.set_password_by_sms_code('new_password', code)

```

返回示例：
```
结果同 1.使用短信验证码登录 返回结果一样
```

## <span id="jump4">4. 获取头条用户个人主页信息</span>

状态：**无需登录**

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
info = bot.get_user_info('67845295779')

```
返回示例：
```json5
{
	'data': {
		'apply_auth_entry_title': '我的认证',
		'apply_auth_url': 'sslocal://reactnative?channelName=tt_user_auth&bundleName=index&moduleName=interest_certification&hide_back_buttonView=1&supportLocalAnim=true&hide_night_cover=1&fallbackUrl=sslocal%3A%2F%2Fwebview%3Fhide_bar%3D1%26use_wk%3D1%26should_append_common_param%3D1%26url%3Dhttps%253A%252F%252Fi.snssdk.com%252Ffeoffline%252Ftt_user_auth_web_55%252Ftemplate%252Finterest_certification_rn55%252Finterest_certification.html%26title%3D%25E5%25A4%25B4%25E6%259D%25A1%25E8%25AE%25A4%25E8%25AF%2581',
		'area': '湖北省武汉市',
		'article_limit_enable': 1,
		'avatar_url': 'http://p29-tt.byteimg.com/img/pgc-image/71bb4a63569b4842a6b6a1a26796fae4~202x450.jpeg',
		'big_avatar_url': 'http://p9-tt.byteimg.com/img/pgc-image/71bb4a63569b4842a6b6a1a26796fae4~640x0.image',
		'bottom_tab': [{
			'children': [{
				'name': '大学生PPT',
				'raw_value': 'https://www.toutiao.com/i6770570986430398979/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6770570986430398979&item_id=6770570986430398979',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6770570986430398979/'
			}, {
				'name': 'Excel公式函数',
				'raw_value': 'https://www.toutiao.com/i6650254675931038216/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6650254675931038216&item_id=6650254675931038216',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6650254675931038216/'
			}, {
				'name': '硬盘数据恢复',
				'raw_value': 'https://www.toutiao.com/i6650613522478662158/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6650613522478662158&item_id=6650613522478662158',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6650613522478662158/'
			}, {
				'name': 'ppt动画制作',
				'raw_value': 'https://www.toutiao.com/i6649224691007357454/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6649224691007357454&item_id=6649224691007357454',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6649224691007357454/'
			}, {
				'name': '鬼步舞技巧',
				'raw_value': 'https://www.toutiao.com/i6648507773149512199/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6648507773149512199&item_id=6648507773149512199',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6648507773149512199/'
			}],
			'name': '往期精彩',
			'raw_value': 'https://www.toutiao.com/i6602137112827396615/',
			'schema_href': 'sslocal://webview?url=https%3A%2F%2Fwww.toutiao.com%2Fi6602137112827396615%2F',
			'type': '',
			'value': ''
		}, {
			'children': [{
				'name': '电商运营',
				'raw_value': 'https://www.toutiao.com/i6636241697317585411/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6636241697317585411&item_id=6636241697317585411',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6636241697317585411/'
			}, {
				'name': '工程造价',
				'raw_value': 'https://www.toutiao.com/i6636241697317585411/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6636241697317585411&item_id=6636241697317585411',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6636241697317585411/'
			}, {
				'name': '二级建造师',
				'raw_value': 'https://www.toutiao.com/i6645807597104398852/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6645807597104398852&item_id=6645807597104398852',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6645807597104398852/'
			}, {
				'name': '小学奥数',
				'raw_value': 'https://www.toutiao.com/i6639506578422628878/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6639506578422628878&item_id=6639506578422628878',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6639506578422628878/'
			}, {
				'name': 'CAD设计技巧',
				'raw_value': 'https://www.toutiao.com/i6636241697317585411/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6636241697317585411&item_id=6636241697317585411',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6636241697317585411/'
			}],
			'name': '办公教育',
			'type': '',
			'value': ''
		}, {
			'children': [{
				'name': '吉他弹唱技巧',
				'raw_value': 'https://www.toutiao.com/i6648398556036071943/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6648398556036071943&item_id=6648398556036071943',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6648398556036071943/'
			}, {
				'name': '手工剪纸技巧',
				'raw_value': 'https://www.toutiao.com/i6645170152071496196/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6645170152071496196&item_id=6645170152071496196',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6645170152071496196/'
			}, {
				'name': '瑜伽技巧教程',
				'raw_value': 'https://www.toutiao.com/i6642558123884151300/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6642558123884151300&item_id=6642558123884151300',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6642558123884151300/'
			}, {
				'name': '拳击技巧教程',
				'raw_value': 'https://www.toutiao.com/i6641836858596655624/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6641836858596655624&item_id=6641836858596655624',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6641836858596655624/'
			}, {
				'name': '陈式太极拳',
				'raw_value': 'https://www.toutiao.com/i6636986276316709389/',
				'schema_href': 'sslocal://detail?aggr_type=2&groupid=6636986276316709389&item_id=6636986276316709389',
				'type': 'href',
				'value': 'https://www.toutiao.com/i6636986276316709389/'
			}],
			'name': '生活教程',
			'type': '',
			'value': ''
		}],
		'current_user_id': 0,
		'description': '分享教育、领导者必备知识库，职场技能!',
		'digg_count': 144239,
		'flipchat_invite': '',
		'follow_recommend_bar_height': 0,
		'followers_count': 256892,
		'followers_detail': [{
			'app_name': 'news_article',
			'apple_id': '529092160',
			'download_url': '',
			'fans_count': 248884,
			'icon': 'http://p3.pstatp.com/origin/50ed00079a1b6b8d1fb1',
			'name': '头条',
			'open_url': 'sslocal://relation/follower?uid=67845295779',
			'package_name': 'com.ss.android.article.news'
		}, {
			'app_name': 'video_article',
			'apple_id': '1134496215',
			'download_url': 'https://d.ixigua.com/kgbh/',
			'fans_count': 7967,
			'icon': 'http://p3.pstatp.com/medium/b76c0007999921c7a731',
			'name': '西瓜',
			'open_url': 'snssdk32://pgcprofile?user_id=67845295779',
			'package_name': 'com.ss.android.article.video'
		}, {
			'app_name': 'aweme',
			'apple_id': '1142110895',
			'download_url': 'https://d.douyin.com/JsvN/',
			'fans_count': 41,
			'icon': 'http://p3.pstatp.com/origin/50ec00079b64de2050dc',
			'name': '抖音',
			'open_url': 'snssdk1128://user/profile/67197674956',
			'package_name': 'com.ss.android.ugc.aweme'
		}],
		'followings_count': 155,
		'forum_following_count': 0,
		'gender': 0,
		'has_sponsor': False,
		'hide_follow_count': 0,
		'is_blocked': 0,
		'is_blocking': 0,
		'is_followed': False,
		'is_following': False,
		'live_datas': [],
		'log_id': '20200506215742010026077201214992E4',
		'medals': [],
		'media_id': 1577305632951309,
		'media_type': '5',
		'mplatform_followers_count': 256892,
		'name': '乐传壹号',
		'no_display_pgc_icon': 1,
		'pgc_custom_menu': [],
		'pgc_like_count': 0,
		'private_letter_permission': 0,
		'publish_count': 4692,
		'screen_name': '乐传壹号',
		'share_data': {
			'wechat_moments': {
				'icon_url': 'http://p29-tt.byteimg.com/img/pgc-image/71bb4a63569b4842a6b6a1a26796fae4~202x450.jpeg',
				'title': '乐传壹号的个人主页 - 今日头条',
				'url': 'https://profile.zjurl.cn/rogue/ugc/profile/?version_code=700&version_name=70000&user_id=67845295779&media_id=1577305632951309&request_source=1&active_tab=dongtai&device_id=65&app_name=news_article'
			},
			'wechat_msg': {
				'desc': '认证: 湖北乐传网络科技有限公司官方账号 教育领域创作者',
				'icon_url': 'http://p29-tt.byteimg.com/img/pgc-image/71bb4a63569b4842a6b6a1a26796fae4~202x450.jpeg',
				'title': '乐传壹号的个人主页 - 今日头条',
				'url': 'https://profile.zjurl.cn/rogue/ugc/profile/?version_code=700&version_name=70000&user_id=67845295779&media_id=1577305632951309&request_source=1&active_tab=dongtai&device_id=65&app_name=news_article'
			}
		},
		'share_url': 'https://profile.zjurl.cn/rogue/ugc/profile/?version_code=700&version_name=70000&user_id=67845295779&media_id=1577305632951309&request_source=1&active_tab=dongtai&device_id=65&app_name=news_article',
		'show_private_letter': 1,
		'sponsor_url': '',
		'status': 0,
		'top_tab': [{
			'disable_common_params': False,
			'is_default': True,
			'is_native': True,
			'load_count': 12,
			'show_name': '全部',
			'type': 'dongtai',
			'url': '/api/feed/profile/v1/?category=profile_all'
		}, {
			'disable_common_params': False,
			'is_default': False,
			'is_native': True,
			'load_count': 20,
			'show_name': '文章',
			'type': 'all',
			'url': '/api/feed/profile/v1/?category=profile_article'
		}, {
			'disable_common_params': False,
			'is_default': False,
			'is_native': True,
			'load_count': 20,
			'show_name': '视频',
			'type': 'video',
			'url': '/api/feed/profile/v1/?category=profile_video'
		}, {
			'disable_common_params': False,
			'is_default': False,
			'is_native': False,
			'native_index_url': '/user/profile/native_index/',
			'show_name': '专栏',
			'type': 'column',
			'url': ''
		}, {
			'disable_common_params': False,
			'is_default': False,
			'is_native': True,
			'load_count': 20,
			'show_name': '问答',
			'type': 'wenda',
			'url': '/api/feed/profile/v1/?category=profile_wenda'
		}, {
			'disable_common_params': False,
			'is_default': False,
			'is_native': True,
			'load_count': 20,
			'show_name': '小视频',
			'type': 'ies_video',
			'url': '/api/feed/profile/v1/?category=profile_short_video'
		}, {
			'disable_common_params': False,
			'is_default': False,
			'is_native': False,
			'native_index_url': '/market/v1/tpl/profile/community.html',
			'show_name': '圈子',
			'type': 'community',
			'url': ''
		}],
		'ugc_publish_media_id': 0,
		'user_auth_info': '{"auth_type":"3","auth_info":"湖北乐传网络科技有限公司官方账号 教育领域创作者","other_auth":{"interest":"教育领域创作者"}}',
		'user_decoration': '',
		'user_id': 67845295779,
		'verified_agency': '头条认证',
		'verified_content': '湖北乐传网络科技有限公司官方账号 教育领域创作者'
	},
	'errno': 0,
	'message': 'success'
}
```

## <span id="jump5">5. 获取头条用户相关用户推荐</span>

状态：**无需登录**

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
ret = bot.get_recommend_users('67845295779')

```
返回示例：
```json5
{
	'err_no': 0,
	'has_more': 0,
	'user_cards': [{
		'user': {
			'info': {
				'avatar_url': 'http://sf6-ttcdn-tos.pstatp.com/img/pgc-image/3d78c933b8b9411bbade0092c4298799~120x256.image',
				'desc': '专注于平面设计ps教程，不定期分享PS/CDR/AI平面设计',
				'name': 'PS教程免费学',
				'schema': 'sslocal://profile?uid=74413864489',
				'user_auth_info': '{"auth_type":"0","auth_info":"优质教育领域创作者","other_auth":{"interest":"优质教育领域创作者"}}',
				'user_decoration': '',
				'user_id': 74413864489,
				'user_verified': 0,
				'verified_content': '优质教育领域创作者'
			},
			'relation': {
				'is_followed': 0,
				'is_following': 0,
				'is_friend': 0
			},
			'relation_count': {
				'followings_count': 5,
				'followers_count': 31353
			}
		},
		'activity': None,
		'recommend_reason': '优质教育领域创作者',
		'recommend_type': -2138570752,
		'stats_place_holder': '{"card_scene":"0","impr_id":"20200506215928010026076084324BA88B","profile_user_id":"67845295779"}',
		'real_name': '',
		'intro': '3.1万粉丝 ',
		'show_name': 'PS教程免费学',
		'description': '优质教育领域创作者',
		'channel_id': 0,
		'profile_user_id': 67845295779,
		'card_type': 0
	}, {
		'user': {
			'info': {
				'avatar_url': 'http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/11778/4314151066~120x256.image',
				'desc': '《北大商业评论》总监，对设计、创意、职场的一些认识和分享！',
				'name': '图色PPT',
				'schema': 'sslocal://profile?uid=5879647342',
				'user_auth_info': '{"auth_type":"0","auth_info":"《北大商业评论》创意设计总监 职场领域创作者","other_auth":{"interest":"职场领域创作者"}}',
				'user_decoration': '',
				'user_id': 5879647342,
				'user_verified': 0,
				'verified_content': '《北大商业评论》创意设计总监 职场领域创作者'
			},
			'relation': {
				'is_followed': 0,
				'is_following': 0,
				'is_friend': 0
			},
			'relation_count': {
				'followings_count': 22,
				'followers_count': 59430
			}
		},
		'activity': None,
		'recommend_reason': '《北大商业评论》创意设计总监 职场领域创作者',
		'recommend_type': -2146959360,
		'stats_place_holder': '{"card_scene":"0","impr_id":"20200506215928010026076084324BA88B","profile_user_id":"67845295779"}',
		'real_name': '',
		'intro': '5.9万粉丝 ',
		'show_name': '图色PPT',
		'description': '《北大商业评论》创意设计总监 职场领域创作者',
		'channel_id': 0,
		'profile_user_id': 67845295779,
		'card_type': 0
	}, {
		'action_card_title': '查看更多',
		'action_schema': 'sslocal://add_friend?from_page=recommend_card',
		'is_action_card': True,
		'profile_user_id': 67845295779,
		'recommend_reason': '',
		'recommend_type': 0,
		'stats_place_holder': '{"card_scene":"0","impr_id":"20200506215928010026076084324BA88B","profile_user_id":"67845295779"}'
	}]
}
```

## <span id="jump6">6. 获取头条用户所有发布作品</span>

状态：**无需登录**

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
ret = bot.get_user_posts('67845295779',kind='ALL')

```
返回示例：第一页
```json5
{
	'message': 'success',
	'data': [{
		'content': '{"abstract":"翻开大佬们的履历就会发现，拥有快于常人的职场升迁速度，往往在于某一些关键的工作汇报中获得高层赏识，而开始得到重用Excel高逼格图表模板制作：280集视频教程+1000模板，送给你参考Excel图表制作教程领取提示：1.转发+点赞文章2.评论区回复：图表3.关注我，私信回复：我要","action_extra":"","action_list":null,"activity":null,"ad_button":null,"aggr_type":1,"allow_download":false,"article_alt_url":"","article_open_url":null,"article_sub_type":0,"article_type":0,"article_url":"http://toutiao.com/group/6815781546956423694/","article_version":0,"audio_duration":null,"ban_bury":0,"ban_comment":false,"ban_danmaku":null,"ban_digg":0,"ban_immersive":null,"behot_time":1586922804,"bury_count":0,"bury_style_show":1,"cell_ctrls":{"cell_flag":5898240,"cell_layout_style":26,"cell_height":0,"content_decoration":null,"need_client_impr_recycle":null},"cell_flag":5898240,"cell_layout_style":26,"cell_type":0,"cell_ui_type":null,"city":"","cold_start":null,"comment":null,"comment_count":329,"commoditys":null,"content_decoration":null,"control_meta":{"modify":{"hide":false,"name":"修改","permission":true,"tips":""},"remove":{"hide":false,"name":"删除","permission":true,"tips":""}},"control_panle":null,"cursor":0,"danmaku_count":null,"data_type":1,"debug_info":null,"detail_content":null,"detail_mode":null,"detail_schema":null,"digg_count":0,"digg_icon_key":null,"disallow_web_transform":null,"display_url":"http://toutiao.com/group/6815781546956423694/","entity_info":null,"feed_title":null,"filter_words":null,"follow_button_style":0,"forum_extra_data":"","forward_info":{"forward_count":92},"gallary_flag":null,"gallary_image_count":0,"gallary_style":null,"group_flags":0,"group_id":6815781546956423694,"group_source":2,"group_type":0,"has_audio":null,"has_image":true,"has_m3u8_video":false,"has_mp4_video":false,"has_video":false,"homo_lvideo_info":null,"hot":0,"hot_board_labels":null,"id":6815781546956423694,"ignore_web_transform":0,"image_list":[{"height":400,"uri":"pgc-image/235ec3ff63ab43faa1980758c90997e2","url":"http://p9-tt-ipv6.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~400x400_cs.webp","url_list":[{"url":"http://p9-tt-ipv6.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~400x400_cs.webp"},{"url":"http://p29-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~400x400_cs.webp"},{"url":"http://p26-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~400x400_cs.webp"}],"width":400}],"image_type":null,"info_desc":"","interaction_data":null,"is_original":false,"is_stick":true,"is_subject":false,"is_subscribe":null,"item_id":6815781546956423694,"item_id_str":"6815781546956423694","item_version":0,"keywords":"","label":"","label_extra":null,"label_style":0,"large_image_list":[{"height":380,"uri":"pgc-image/235ec3ff63ab43faa1980758c90997e2","url":"http://p3-tt-ipv6.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp","url_list":[{"url":"http://p3-tt-ipv6.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp"},{"url":"http://p26-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp"},{"url":"http://p3-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp"}],"width":720}],"level":0,"like_count":0,"log_pb":{"group_id_str":"6815781546956423694","impr_id":"20200506221250010027024131253034D8","is_following":"0"},"lynx_labels":null,"media_info":null,"media_name":"","middle_image":{"height":425,"uri":"list/pgc-image/235ec3ff63ab43faa1980758c90997e2","url":"http://p3-tt.bytecdn.cn/list/pgc-image/235ec3ff63ab43faa1980758c90997e2","url_list":[{"url":"http://p3-tt.bytecdn.cn/list/pgc-image/235ec3ff63ab43faa1980758c90997e2"},{"url":"http://p3-tt.bytecdn.cn/list/pgc-image/235ec3ff63ab43faa1980758c90997e2"},{"url":"http://p3-tt.bytecdn.cn/list/pgc-image/235ec3ff63ab43faa1980758c90997e2"}],"width":640},"natant_level":0,"nearby_read_info":null,"need_client_impr_recycle":null,"open_url":null,"optional_data":null,"outsourcing_id":"","packed_json_str":null,"play_auth_token":null,"play_biz_token":null,"pread_params":null,"preload_info":null,"preload_resource_url":null,"preload_web":0,"preload_web_content":null,"pseries":null,"publish_time":1586922804,"raw_data":null,"read_count":2895,"reason":"","reback_flag":0,"recommend_label":null,"recommend_reason":null,"recommond_reason":null,"repin_count":0,"repin_time":0,"req_id":null,"rid":"20200506221250010027024131253034D8","search_labels":null,"share_count":0,"share_info":null,"share_large_image":null,"share_type":null,"share_url":"http://toutiao.com/group/6815781546956423694/?iid=0\\u0026app=news_article","show_dislike":false,"show_max_line":null,"show_more":null,"show_portrait":null,"show_portrait_article":null,"small_image":null,"source":"乐传壹号","source_avatar":null,"source_desc":null,"source_desc_open_url":null,"source_icon":null,"source_icon_style":null,"source_open_url":null,"stick_style":1,"subject_group_id":0,"subject_label":null,"tag":"news_career","tag_id":6815781546956423694,"tc_head_text":"","tip":0,"title":"Excel高逼格图表模板制作：280集视频教程+1000模板，送给你参考","title_rich_span":null,"ugc_recommend":{"activity":"","reason":""},"ugc_video_cover":null,"url":"http://toutiao.com/group/6815781546956423694/","user_bury":0,"user_digg":0,"user_info":{"avatar_url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/71bb4a63569b4842a6b6a1a26796fae4~120x256.image","description":"分享教育、领导者必备知识库，职场技能!","follow":false,"follower_count":null,"live_info_type":null,"name":"乐传壹号","room_schema":null,"schema":"","user_auth_info":"{\\"auth_info\\":\\"\\",\\"auth_type\\":\\"3\\",\\"other_auth\\":{\\"interest\\":\\"教育领域创作者\\"}}","user_decoration":"","user_id":67845295779,"user_verified":false,"verified_content":""},"user_like":0,"user_repin":0,"user_repin_time":0,"user_verified":null,"verified_content":null,"video_detail_info":{"detail_video_large_image":{"height":380,"uri":"pgc-image/235ec3ff63ab43faa1980758c90997e2","url":"http://p3-tt-ipv6.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp","url_list":[{"url":"http://p3-tt-ipv6.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp"},{"url":"http://p26-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp"},{"url":"http://p3-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp"}],"width":720},"direct_play":1,"group_flags":0,"show_pgc_subscribe":0,"video_id":"","video_preloading_flag":null,"video_subject_id":null,"video_third_monitor_url":"","video_type":null,"video_url":null,"video_watch_count":null,"video_watching_count":null},"video_duration":0,"video_id":null,"video_play_info":null,"video_proportion":null,"video_proportion_article":null,"video_source":null,"video_style":0,"zzcomment":null}',
		'code': ''
	},{
		'content': '{"abstract":"","allow_download":false,"article_sub_type":0,"article_type":0,"article_url":"","ban_comment":0,"ban_immersive":0,"behot_time":1588774370,"bury_count":0,"bury_style_show":1,"cell_ctrls":{"cell_flag":5374217,"cell_layout_style":24,"cell_height":0,"content_decoration":"","need_client_impr_recycle":1},"cell_type":56,"comment_count":0,"content_decoration":"","cursor":1588774370000,"data_type":1,"digg_count":0,"has_m3u8_video":false,"has_mp4_video":0,"has_video":false,"hot":0,"id":6822177731992682499,"ignore_web_transform":0,"interaction_data":"","is_subject":false,"item_version":0,"level":0,"log_pb":{"author_id":"67845295779","fw_id":"6822079043341386244","group_source":"23","impr_id":"20200506221250010027024131253034D8","is_following":"0","is_reposted":"1","repost_gid":"6822177731992682499"},"raw_data":{"comment_base":{"action":{"bury_count":0,"comment_count":0,"ctr":null,"detail_read_count_merge":null,"detail_read_count_new":null,"detail_read_count_old":null,"digg_count":0,"display_count":null,"fans_display_count_new":null,"fans_display_count_old":null,"fans_read_count_new":null,"fans_read_count_old":null,"forward_count":0,"play_count":0,"read_count":1141,"repin_count":null,"repost_display_count":null,"repost_read_count":null,"share_count":0,"show_count":null,"stay_time":null,"user_bury":0,"user_digg":0,"user_repin":0},"city_invisible_list":[],"comment_schema":"sslocal://comment_repost_detail?category_id=profile_all\\u0026comment_id=6822177731992682499\\u0026enter_from=click_category\\u0026gd_ext_json=%7B%22category_id%22%3A%22profile_all%22%2C%22enter_from%22%3A%22click_category%22%2C%22log_pb%22%3A%22%7B%5C%22fw_id%5C%22%3A%5C%226822079043341386244%5C%22%2C%5C%22group_source%5C%22%3A%5C%2223%5C%22%2C%5C%22impr_id%5C%22%3A%5C%2220200506221250010027024131253034D8%5C%22%2C%5C%22is_following%5C%22%3A%5C%220%5C%22%2C%5C%22is_repost%5C%22%3A%5C%221%5C%22%2C%5C%22repost_gid%5C%22%3A%5C%226822177731992682499%5C%22%7D%22%2C%22refer%22%3A%22%22%7D\\u0026group_id=6822177731992682499\\u0026refer=","composition":98304,"content":"人力资源管理教程[呲牙][祈祷]","content_decoration":"","content_rich_span":"{\\"links\\":[]}","create_time":1588412035,"detail_schema":"sslocal://comment_repost_detail?category_id=profile_all\\u0026comment_id=6822177731992682499\\u0026enter_from=click_category\\u0026gd_ext_json=%7B%22category_id%22%3A%22profile_all%22%2C%22enter_from%22%3A%22click_category%22%2C%22log_pb%22%3A%22%7B%5C%22fw_id%5C%22%3A%5C%226822079043341386244%5C%22%2C%5C%22group_source%5C%22%3A%5C%2223%5C%22%2C%5C%22impr_id%5C%22%3A%5C%2220200506221250010027024131253034D8%5C%22%2C%5C%22is_following%5C%22%3A%5C%220%5C%22%2C%5C%22is_repost%5C%22%3A%5C%221%5C%22%2C%5C%22repost_gid%5C%22%3A%5C%226822177731992682499%5C%22%7D%22%2C%22refer%22%3A%22%22%7D\\u0026group_id=6822177731992682499\\u0026refer=","digg_icon_key":"","digg_text":"","group_id":6822177731992682499,"group_source":23,"id":6822177731992682499,"item_id":6822079043341386244,"level":1,"parent_id":6822079043341386244,"repost_params":{"cover_url":null,"fw_id":6822079043341386244,"fw_id_type":4,"fw_native_schema":null,"fw_share_url":null,"fw_user_id":67845295779,"has_video":null,"opt_id":6822177731992682499,"opt_id_type":1,"repost_type":211,"schema":"","title":"","title_rich_span":null},"repost_status":1,"rich_content":"人力资源管理教程\\u003ci class=\\"emoji emoji_8_laugh\\"\\u003e\\u003c/i\\u003e\\u003cspan class=\\"emoji-name\\"\\u003e[呲牙]\\u003c/span\\u003e\\u003ci class=\\"emoji emoji_54_3Q\\"\\u003e\\u003c/i\\u003e\\u003cspan class=\\"emoji-name\\"\\u003e[祈祷]\\u003c/span\\u003e","share":{"share_cover":{"uri":"","url_list":["http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/71bb4a63569b4842a6b6a1a26796fae4~120x256.image"]},"share_desc":"乐传壹号发布了一条微头条，邀请你来看","share_title":"乐传壹号：人力资源管理教程[呲牙][祈祷]","share_url":"https://weitoutiao.zjurl.cn/ugc/share/comment/6822177731992682499/?app=\\u0026target_app=13","share_weibo_desc":null},"share_info":{"cover_image":null,"description":null,"share_backup_url":null,"share_type":{"pyq":0,"qq":0,"qzone":0,"wx":0},"share_url":"https://weitoutiao.zjurl.cn/ugc/share/comment/6822177731992682499/?app=\\u0026target_app=13","title":"","token_type":1,"weixin_cover_image":null},"status":1,"user":{"block":{"is_blocked":0,"is_blocking":0},"info":{"avatar_uri":null,"avatar_url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/71bb4a63569b4842a6b6a1a26796fae4~120x256.image","ban_status":null,"create_time":null,"desc":"","live_info_type":1,"living_count":0,"medals":null,"media_id":null,"name":"乐传壹号","origin_profile_url":null,"origin_user_id":null,"real_name":null,"room_schema":null,"schema":"sslocal://profile?uid=67845295779\\u0026refer=dongtai","user_auth_info":"","user_decoration":"","user_id":67845295779,"user_verified":0,"verified_content":""},"media_info":null,"relation":{"is_followed":0,"is_following":0,"is_friend":0,"is_real_friend":null,"remark_name":null},"relation_count":{"followers_count":0,"followings_count":0}},"visibility_level":45},"comment_type":211,"gd_json":"","id":6822177731992682499,"id_str":"6822177731992682499","is_repost":1,"layout_style":0,"origin_common_content":{"business_payload":"","cover_image":{"height":222,"image_type":1,"uri":"dfic-imagehandler/7a7042be-e626-48fa-abc8-49d9ca43c97d","url":"http://p9-tt.byteimg.com/img/dfic-imagehandler/7a7042be-e626-48fa-abc8-49d9ca43c97d~339x222_noop.image","url_list":[{"url":"http://p9-tt.byteimg.com/img/dfic-imagehandler/7a7042be-e626-48fa-abc8-49d9ca43c97d~339x222_noop.image"},{"url":"http://p6-tt.byteimg.com/img/dfic-imagehandler/7a7042be-e626-48fa-abc8-49d9ca43c97d~339x222_noop.image"},{"url":"http://p1-tt.byteimg.com/img/dfic-imagehandler/7a7042be-e626-48fa-abc8-49d9ca43c97d~339x222_noop.image"}],"width":339},"group_id":6822079043341386244,"group_id_str":"6822079043341386244","has_video":false,"rich_title":"\\u003ca href=\\"sslocal://profile?uid=67845295779\\"\\u003e@乐传壹号：\\u003c/a\\u003e职场人力资源管理培训技巧：60集视频教程+1000套ppt，送给你参考","schema":"sslocal://detail?aggr_type=2\\u0026bury_style_show=1\\u0026category_id=profile_all\\u0026category_name=profile_all\\u0026enter_from=click_category\\u0026gd_ext_json=%7B%22category_id%22%3A%22profile_all%22%2C%22enter_from%22%3A%22click_category%22%7D\\u0026groupid=6822079043341386244\\u0026item_id=6822079043341386244\\u0026refer=","style":1,"title":"@乐传壹号：职场人力资源管理培训技巧：60集视频教程+1000套ppt，送给你参考","title_rich_span":"{\\"links\\":[{\\"start\\":0,\\"length\\":6,\\"link\\":\\"sslocal://profile?uid=67845295779\\",\\"type\\":1,\\"text\\":\\"@乐传壹号\\",\\"id\\":0,\\"id_type\\":0}]}","user":{"info":{"avatar_uri":null,"avatar_url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/71bb4a63569b4842a6b6a1a26796fae4~120x256.image","ban_status":null,"create_time":null,"desc":"","live_info_type":null,"living_count":0,"medals":[],"media_id":null,"name":"乐传壹号","origin_profile_url":null,"origin_user_id":null,"real_name":null,"room_schema":null,"schema":"sslocal://profile?uid=67845295779\\u0026refer=dongtai","user_auth_info":"","user_decoration":null,"user_id":67845295779,"user_verified":0,"verified_content":""},"media_info":null,"relation":null,"relation_count":null}},"origin_content_screen_shot":null,"origin_group":null,"origin_thread":null,"origin_ugc_video":null,"show_origin":1,"show_tips":"","stream_ui":{"default_text_line":3,"inner_ui_flag":0,"max_text_line":10},"title_prefix":""},"read_count":0,"req_id":"20200506221250010027024131253034D8","rid":"20200506221250010027024131253034D8","share_count":0,"share_info":null,"show_dislike":false,"show_portrait":false,"show_portrait_article":false,"small_image":null,"tip":0,"ugc_recommend":{"activity":"","reason":""},"user_repin":0,"user_verified":0,"verified_content":"","video_style":0}',
		'code': ''
	}],
	'has_more': True,
	'offset': 1588393299973,
	'tail': '',
	'preload_ack_data': None
}
```

## <span id="jump7">7. 获取头条用户的视频</span>

状态：**无需登录**

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
ret = bot.get_user_posts('67845295779',kind='VIDEO')

```
返回示例：第一页
```json5
{
	'message': 'success',
	'data': [{
		'content': '{"abstract":"","allow_download":false,"article_sub_type":0,"article_type":2,"article_url":"","ban_comment":0,"ban_immersive":null,"behot_time":1551685960,"bury_count":0,"bury_style_show":1,"cell_flag":5374209,"cell_layout_style":24,"cell_type":0,"comment_count":32,"content_decoration":"","cursor":1588774939000,"digg_count":70,"digg_icon_key":"","display_url":"http://toutiao.com/group/6664437685639184900/","forward_info":{"forward_count":4},"group_flags":32832,"group_id":6664437685639184900,"has_m3u8_video":false,"has_mp4_video":0,"has_video":true,"hot":0,"ignore_web_transform":0,"interaction_data":"","is_subject":false,"is_subscribe":false,"item_id":6664437685639184900,"item_version":0,"large_image_list":[{"height":373,"image_type":1,"uri":"tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50","url":"http://p9-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo","url_list":[{"url":"http://p9-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo"},{"url":"http://p6-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo"},{"url":"http://p6-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo"},{"url":"http://p29-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo"}],"width":660}],"level":0,"log_pb":{"author_id":"67845295779","group_id_str":"6664437685639184900","group_source":"2","impr_id":"202005062222190100260770801251530B","is_following":"0"},"lynx_server":null,"nearby_read_info":null,"open_url":"","play_auth_token":"HMAC-SHA1:2.0:1588861340030038150:bab42eac5b9e4a8eb25a91fc371ad533:Bg2BrjpbVFQRGP79jJrGutdCd0Q=","play_biz_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODg4NjEzNDAsInZlciI6InYxIiwiYWsiOiJiYWI0MmVhYzViOWU0YThlYjI1YTkxZmMzNzFhZDUzMyIsInN1YiI6InBnY18xMDgwcCJ9.pnywPJ-wQVq6r5P-g7RRUKSisyECPNkZNnD-grLYcj4","pseries":null,"publish_time":1551685960,"read_count":0,"rid":"202005062222190100260770801251530B","share_count":0,"share_info":null,"share_url":"https://m.ixigua.com/item/6664437685639184900/?iid=0","show_dislike":false,"show_portrait":false,"show_portrait_article":false,"small_image":null,"source":"乐传壹号","tip":0,"title":"全套Excel公式函数技巧0基础视频教程+365套图表模板，限时领取！","title_rich_span":"{\\"links\\":[]}","ugc_video_cover":{"height":373,"image_type":1,"uri":"tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50","url":"http://p9-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo","url_list":[{"url":"http://p9-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo"},{"url":"http://p6-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo"},{"url":"http://p6-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo"},{"url":"http://p29-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo"}],"width":660},"user_digg":0,"user_info":{"avatar_url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/71bb4a63569b4842a6b6a1a26796fae4~120x256.image","follow":false,"live_info_type":0,"living_count":0,"name":"乐传壹号","room_schema":"","user_auth_info":"{\\"auth_type\\":\\"3\\",\\"auth_info\\":\\"湖北乐传网络科技有限公司官方账号 教育领域创作者\\",\\"other_auth\\":{\\"interest\\":\\"教育领域创作者\\"}}","user_decoration":"","user_id":67845295779,"user_verified":true,"verified_content":"湖北乐传网络科技有限公司官方账号 教育领域创作者"},"user_repin":0,"user_verified":0,"verified_content":"","video_detail_info":{"detail_video_large_image":{"height":373,"image_type":1,"uri":"tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50","url":"http://p9-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo","url_list":[{"url":"http://p9-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo"},{"url":"http://p6-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo"},{"url":"http://p6-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo"},{"url":"http://p29-tt.byteimg.com/img/tos-cn-i-0004/7e2da49b523d40b0903c25abe22abd50~noop.jpeg?from=shortvideo"}],"width":660},"direct_play":1,"group_flags":32832,"show_pgc_subscribe":1,"video_id":"v02004810000bhud33d2v328dk3qvc4g","video_watch_count":1434},"video_duration":102,"video_id":"v02004810000bhud33d2v328dk3qvc4g","video_play_info":null,"video_proportion":1.7777777777777777,"video_proportion_article":1.7777777777777777,"video_source":"ugc_video","video_style":2}',
		'code': ''
	}, {
		'content': '{"abstract":"","allow_download":false,"article_sub_type":0,"article_type":2,"article_url":"","ban_comment":0,"ban_immersive":null,"behot_time":1518229860,"bury_count":0,"bury_style_show":1,"cell_flag":5374209,"cell_layout_style":24,"cell_type":0,"comment_count":1,"content_decoration":"","cursor":1588774939000,"digg_count":2,"digg_icon_key":"","display_url":"http://toutiao.com/group/6514197531914666509/","forward_info":{"forward_count":1},"group_flags":32832,"group_id":6514197531914666509,"has_m3u8_video":false,"has_mp4_video":0,"has_video":true,"hot":0,"ignore_web_transform":0,"interaction_data":"","is_subject":false,"is_subscribe":false,"item_id":6514197531914666509,"item_version":0,"large_image_list":[{"height":373,"image_type":1,"uri":"5bc10000294d290b76f3","url":"http://p1-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo","url_list":[{"url":"http://p1-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo"},{"url":"http://p3-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo"},{"url":"http://p3-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo"},{"url":"http://p6-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo"}],"width":660}],"level":0,"log_pb":{"author_id":"67845295779","group_id_str":"6514197531914666509","group_source":"2","impr_id":"202005062222190100260770801251530B","is_following":"0"},"lynx_server":null,"nearby_read_info":null,"open_url":"","play_auth_token":"HMAC-SHA1:2.0:1588861340028872792:bab42eac5b9e4a8eb25a91fc371ad533:RxKkvWt3oCbal8/0KoWHMIQx79A=","play_biz_token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODg4NjEzNDAsInZlciI6InYxIiwiYWsiOiJiYWI0MmVhYzViOWU0YThlYjI1YTkxZmMzNzFhZDUzMyIsInN1YiI6InBnY18xMDgwcCJ9.Ok_VETkD-zmeMhK0sKgac4UWiZR0OrMFktgFHnpbrlQ","pseries":null,"publish_time":1518229860,"read_count":0,"rid":"202005062222190100260770801251530B","share_count":0,"share_info":null,"share_url":"https://m.ixigua.com/item/6514197531914666509/?iid=0","show_dislike":false,"show_portrait":false,"show_portrait_article":false,"small_image":null,"source":"乐传壹号","tip":0,"title":"这招能偷偷查看对方已撤回微信消息，对方毫无察觉，好用到哭","title_rich_span":"{\\"links\\":[]}","ugc_video_cover":{"height":373,"image_type":1,"uri":"5bc10000294d290b76f3","url":"http://p1-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo","url_list":[{"url":"http://p1-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo"},{"url":"http://p3-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo"},{"url":"http://p3-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo"},{"url":"http://p6-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo"}],"width":660},"user_digg":0,"user_info":{"avatar_url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/71bb4a63569b4842a6b6a1a26796fae4~120x256.image","follow":false,"live_info_type":0,"living_count":0,"name":"乐传壹号","room_schema":"","user_auth_info":"{\\"auth_type\\":\\"3\\",\\"auth_info\\":\\"湖北乐传网络科技有限公司官方账号 教育领域创作者\\",\\"other_auth\\":{\\"interest\\":\\"教育领域创作者\\"}}","user_decoration":"","user_id":67845295779,"user_verified":true,"verified_content":"湖北乐传网络科技有限公司官方账号 教育领域创作者"},"user_repin":0,"user_verified":0,"verified_content":"","video_detail_info":{"detail_video_large_image":{"height":373,"image_type":1,"uri":"5bc10000294d290b76f3","url":"http://p1-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo","url_list":[{"url":"http://p1-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo"},{"url":"http://p3-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo"},{"url":"http://p3-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo"},{"url":"http://p6-tt.byteimg.com/img/mosaic-legacy/5bc10000294d290b76f3~noop.jpeg?from=shortvideo"}],"width":660},"direct_play":1,"group_flags":32832,"show_pgc_subscribe":1,"video_id":"e906312ac8cd46139ab84613018ae91a","video_watch_count":221},"video_duration":93,"video_id":"e906312ac8cd46139ab84613018ae91a","video_play_info":null,"video_proportion":1.7777777777777777,"video_proportion_article":1.7777777777777777,"video_source":"ugc_video","video_style":2}',
		'code': ''
	}],
	'has_more': True,
	'offset': 1518229859,
	'tail': '',
	'preload_ack_data': None
}
```

## <span id="jump8">8. 获取头条用户的文章</span>

状态：**无需登录**

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
ret = bot.get_user_posts('67845295779',kind='ARTICLE')

```
返回示例：第一页
```json5
{
	'message': 'success',
	'data': [{
		'content': '{"abstract":"翻开大佬们的履历就会发现，拥有快于常人的职场升迁速度，往往在于某一些关键的工作汇报中获得高层赏识，而开始得到重用Excel高逼格图表模板制作：280集视频教程+1000模板，送给你参考Excel图表制作教程领取提示：1.转发+点赞文章2.评论区回复：图表3.关注我，私信回复：我要","action_extra":"","action_list":null,"activity":null,"ad_button":null,"aggr_type":1,"allow_download":false,"article_alt_url":"","article_open_url":null,"article_sub_type":0,"article_type":0,"article_url":"http://toutiao.com/group/6815781546956423694/","article_version":0,"audio_duration":null,"ban_bury":0,"ban_comment":false,"ban_danmaku":null,"ban_digg":0,"ban_immersive":null,"behot_time":1586922804,"bury_count":0,"bury_style_show":1,"cell_ctrls":{"cell_flag":5898240,"cell_layout_style":26,"cell_height":0,"content_decoration":null,"need_client_impr_recycle":null},"cell_flag":5898240,"cell_layout_style":26,"cell_type":0,"cell_ui_type":null,"city":"","cold_start":null,"comment":null,"comment_count":329,"commoditys":null,"content_decoration":null,"control_meta":{"modify":{"hide":false,"name":"修改","permission":true,"tips":""},"remove":{"hide":false,"name":"删除","permission":true,"tips":""}},"control_panle":null,"cursor":0,"danmaku_count":null,"data_type":1,"debug_info":null,"detail_content":null,"detail_mode":null,"detail_schema":null,"digg_count":0,"digg_icon_key":null,"disallow_web_transform":null,"display_url":"http://toutiao.com/group/6815781546956423694/","entity_info":null,"feed_title":null,"filter_words":null,"follow_button_style":0,"forum_extra_data":"","forward_info":{"forward_count":92},"gallary_flag":null,"gallary_image_count":0,"gallary_style":null,"group_flags":0,"group_id":6815781546956423694,"group_source":2,"group_type":0,"has_audio":null,"has_image":true,"has_m3u8_video":false,"has_mp4_video":false,"has_video":false,"homo_lvideo_info":null,"hot":0,"hot_board_labels":null,"id":6815781546956423694,"ignore_web_transform":0,"image_list":[{"height":400,"uri":"pgc-image/235ec3ff63ab43faa1980758c90997e2","url":"http://p9-tt-ipv6.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~400x400_cs.webp","url_list":[{"url":"http://p9-tt-ipv6.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~400x400_cs.webp"},{"url":"http://p9-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~400x400_cs.webp"},{"url":"http://p26-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~400x400_cs.webp"}],"width":400}],"image_type":null,"info_desc":"","interaction_data":null,"is_original":false,"is_stick":true,"is_subject":false,"is_subscribe":null,"item_id":6815781546956423694,"item_id_str":"6815781546956423694","item_version":0,"keywords":"","label":"","label_extra":null,"label_style":0,"large_image_list":[{"height":380,"uri":"pgc-image/235ec3ff63ab43faa1980758c90997e2","url":"http://p26-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp","url_list":[{"url":"http://p26-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp"},{"url":"http://p3-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp"},{"url":"http://p6-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp"}],"width":720}],"level":0,"like_count":0,"log_pb":{"group_id_str":"6815781546956423694","impr_id":"20200506222329010026077074094FDE60","is_following":"0"},"lynx_labels":null,"media_info":null,"media_name":"","middle_image":{"height":425,"uri":"list/pgc-image/235ec3ff63ab43faa1980758c90997e2","url":"http://p3-tt.bytecdn.cn/list/pgc-image/235ec3ff63ab43faa1980758c90997e2","url_list":[{"url":"http://p3-tt.bytecdn.cn/list/pgc-image/235ec3ff63ab43faa1980758c90997e2"},{"url":"http://p3-tt.bytecdn.cn/list/pgc-image/235ec3ff63ab43faa1980758c90997e2"},{"url":"http://p3-tt.bytecdn.cn/list/pgc-image/235ec3ff63ab43faa1980758c90997e2"}],"width":640},"natant_level":0,"nearby_read_info":null,"need_client_impr_recycle":null,"open_url":null,"optional_data":null,"outsourcing_id":"","packed_json_str":null,"play_auth_token":null,"play_biz_token":null,"pread_params":null,"preload_info":null,"preload_resource_url":null,"preload_web":0,"preload_web_content":null,"pseries":null,"publish_time":1586922804,"raw_data":null,"read_count":2895,"reason":"","reback_flag":0,"recommend_label":null,"recommend_reason":null,"recommond_reason":null,"repin_count":0,"repin_time":0,"req_id":null,"rid":"20200506222329010026077074094FDE60","search_labels":null,"share_count":0,"share_info":null,"share_large_image":null,"share_type":null,"share_url":"http://toutiao.com/group/6815781546956423694/?iid=0\\u0026app=news_article","show_dislike":false,"show_max_line":null,"show_more":null,"show_portrait":null,"show_portrait_article":null,"small_image":null,"source":"乐传壹号","source_avatar":null,"source_desc":null,"source_desc_open_url":null,"source_icon":null,"source_icon_style":null,"source_open_url":null,"stick_style":1,"subject_group_id":0,"subject_label":null,"tag":"news_career","tag_id":6815781546956423694,"tc_head_text":"","tip":0,"title":"Excel高逼格图表模板制作：280集视频教程+1000模板，送给你参考","title_rich_span":null,"ugc_recommend":{"activity":"","reason":""},"ugc_video_cover":null,"url":"http://toutiao.com/group/6815781546956423694/","user_bury":0,"user_digg":0,"user_info":{"avatar_url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/71bb4a63569b4842a6b6a1a26796fae4~120x256.image","description":"分享教育、领导者必备知识库，职场技能!","follow":false,"follower_count":null,"live_info_type":null,"name":"乐传壹号","room_schema":null,"schema":"","user_auth_info":"{\\"auth_info\\":\\"\\",\\"auth_type\\":\\"3\\",\\"other_auth\\":{\\"interest\\":\\"教育领域创作者\\"}}","user_decoration":"","user_id":67845295779,"user_verified":false,"verified_content":""},"user_like":0,"user_repin":0,"user_repin_time":0,"user_verified":null,"verified_content":null,"video_detail_info":{"detail_video_large_image":{"height":380,"uri":"pgc-image/235ec3ff63ab43faa1980758c90997e2","url":"http://p26-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp","url_list":[{"url":"http://p26-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp"},{"url":"http://p3-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp"},{"url":"http://p6-tt.byteimg.com/img/pgc-image/235ec3ff63ab43faa1980758c90997e2~720x380_cs.webp"}],"width":720},"direct_play":1,"group_flags":0,"show_pgc_subscribe":0,"video_id":"","video_preloading_flag":null,"video_subject_id":null,"video_third_monitor_url":"","video_type":null,"video_url":null,"video_watch_count":null,"video_watching_count":null},"video_duration":0,"video_id":null,"video_play_info":null,"video_proportion":null,"video_proportion_article":null,"video_source":null,"video_style":0,"zzcomment":null}',
		'code': ''
	},  {
		'content': '{"abstract":"距离2020年高考还有不到3个月，作为老师、家长都很着急，在有限的时间里如何科学有效地进行备考，非常重要。","action_extra":"","action_list":null,"activity":null,"ad_button":null,"aggr_type":1,"allow_download":false,"article_alt_url":"","article_open_url":null,"article_sub_type":0,"article_type":0,"article_url":"http://toutiao.com/group/6814254086293029389/","article_version":0,"audio_duration":null,"ban_bury":0,"ban_comment":false,"ban_danmaku":null,"ban_digg":0,"ban_immersive":null,"behot_time":1586574773,"bury_count":0,"bury_style_show":1,"cell_ctrls":{"cell_flag":5898240,"cell_layout_style":26,"cell_height":0,"content_decoration":null,"need_client_impr_recycle":null},"cell_flag":5898240,"cell_layout_style":26,"cell_type":0,"cell_ui_type":null,"city":"","cold_start":null,"comment":null,"comment_count":79,"commoditys":null,"content_decoration":null,"control_meta":{"modify":{"hide":false,"name":"修改","permission":true,"tips":""},"remove":{"hide":false,"name":"删除","permission":true,"tips":""}},"control_panle":null,"cursor":0,"danmaku_count":null,"data_type":1,"debug_info":null,"detail_content":null,"detail_mode":null,"detail_schema":null,"digg_count":0,"digg_icon_key":null,"disallow_web_transform":null,"display_url":"http://toutiao.com/group/6814254086293029389/","entity_info":null,"feed_title":null,"filter_words":null,"follow_button_style":0,"forum_extra_data":"","forward_info":{"forward_count":23},"gallary_flag":null,"gallary_image_count":0,"gallary_style":null,"group_flags":0,"group_id":6814254086293029389,"group_source":2,"group_type":0,"has_audio":null,"has_image":true,"has_m3u8_video":false,"has_mp4_video":false,"has_video":false,"homo_lvideo_info":null,"hot":0,"hot_board_labels":null,"id":6814254086293029389,"ignore_web_transform":0,"image_list":[{"height":400,"uri":"dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0","url":"http://p6-tt-ipv6.byteimg.com/img/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0~400x400_cs.webp","url_list":[{"url":"http://p6-tt-ipv6.byteimg.com/img/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0~400x400_cs.webp"},{"url":"http://p3-tt.byteimg.com/img/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0~400x400_cs.webp"},{"url":"http://p6-tt.byteimg.com/img/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0~400x400_cs.webp"}],"width":400}],"image_type":null,"info_desc":"","interaction_data":null,"is_original":false,"is_subject":false,"is_subscribe":null,"item_id":6814254086293029389,"item_id_str":"6814254086293029389","item_version":0,"keywords":"","label":"","label_extra":null,"label_style":0,"large_image_list":[{"height":380,"uri":"dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0","url":"http://p26-tt.byteimg.com/img/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0~720x380_cs.webp","url_list":[{"url":"http://p26-tt.byteimg.com/img/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0~720x380_cs.webp"},{"url":"http://p6-tt.byteimg.com/img/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0~720x380_cs.webp"},{"url":"http://p29-tt.byteimg.com/img/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0~720x380_cs.webp"}],"width":720}],"level":0,"like_count":0,"log_pb":{"group_id_str":"6814254086293029389","impr_id":"20200506222329010026077074094FDE60","is_following":"0"},"lynx_labels":null,"media_info":null,"media_name":"","middle_image":{"height":816,"uri":"list/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0","url":"http://p9-tt.bytecdn.cn/list/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0","url_list":[{"url":"http://p9-tt.bytecdn.cn/list/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0"},{"url":"http://p6-tt.bytecdn.cn/list/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0"},{"url":"http://p3-tt.bytecdn.cn/list/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0"}],"width":1200},"natant_level":0,"nearby_read_info":null,"need_client_impr_recycle":null,"open_url":null,"optional_data":null,"outsourcing_id":"","packed_json_str":null,"play_auth_token":null,"play_biz_token":null,"pread_params":null,"preload_info":null,"preload_resource_url":null,"preload_web":0,"preload_web_content":null,"pseries":null,"publish_time":1586574773,"raw_data":null,"read_count":594,"reason":"","reback_flag":0,"recommend_label":null,"recommend_reason":null,"recommond_reason":null,"repin_count":0,"repin_time":0,"req_id":null,"rid":"20200506222329010026077074094FDE60","search_labels":null,"share_count":0,"share_info":null,"share_large_image":null,"share_type":null,"share_url":"http://toutiao.com/group/6814254086293029389/?iid=0\\u0026app=news_article","show_dislike":false,"show_max_line":null,"show_more":null,"show_portrait":null,"show_portrait_article":null,"small_image":null,"source":"乐传壹号","source_avatar":null,"source_desc":null,"source_desc_open_url":null,"source_icon":null,"source_icon_style":null,"source_open_url":null,"subject_group_id":0,"subject_label":null,"tag":"news_edu","tag_id":6814254086293029389,"tc_head_text":"","tip":0,"title":"200集高三备考全新视频教程免费送：零基础教师讲解+30G配套练习","title_rich_span":null,"ugc_recommend":{"activity":"","reason":""},"ugc_video_cover":null,"url":"http://toutiao.com/group/6814254086293029389/","user_bury":0,"user_digg":0,"user_info":{"avatar_url":"http://sf3-ttcdn-tos.pstatp.com/img/pgc-image/71bb4a63569b4842a6b6a1a26796fae4~120x256.image","description":"分享教育、领导者必备知识库，职场技能!","follow":false,"follower_count":null,"live_info_type":null,"name":"乐传壹号","room_schema":null,"schema":"","user_auth_info":"{\\"auth_info\\":\\"\\",\\"auth_type\\":\\"3\\",\\"other_auth\\":{\\"interest\\":\\"教育领域创作者\\"}}","user_decoration":"","user_id":67845295779,"user_verified":false,"verified_content":""},"user_like":0,"user_repin":0,"user_repin_time":0,"user_verified":null,"verified_content":null,"video_detail_info":{"detail_video_large_image":{"height":380,"uri":"dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0","url":"http://p26-tt.byteimg.com/img/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0~720x380_cs.webp","url_list":[{"url":"http://p26-tt.byteimg.com/img/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0~720x380_cs.webp"},{"url":"http://p6-tt.byteimg.com/img/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0~720x380_cs.webp"},{"url":"http://p29-tt.byteimg.com/img/dfic-imagehandler/f0c102ae-9a5b-4986-856d-f14744bf44b0~720x380_cs.webp"}],"width":720},"direct_play":1,"group_flags":0,"show_pgc_subscribe":0,"video_id":"","video_preloading_flag":null,"video_subject_id":null,"video_third_monitor_url":"","video_type":null,"video_url":null,"video_watch_count":null,"video_watching_count":null},"video_duration":0,"video_id":null,"video_play_info":null,"video_proportion":null,"video_proportion_article":null,"video_source":null,"video_style":0,"zzcomment":null}',
		'code': ''
	}],
	'has_more': True,
	'offset': 1586574772,
	'tail': '',
	'preload_ack_data': None
}
```

## <span id="jump9">9. 获取头条用户的问答</span>

状态：**无需登录**

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
ret = bot.get_user_posts('67845295779',kind='WENDA')

```
返回示例：
```json5
{
	'message': 'success',
	'data': [{
		'content': '{"abstract":"","allow_download":false,"article_sub_type":0,"article_type":0,"article_url":"","ban_comment":0,"ban_immersive":0,"behot_time":1588775234,"bury_count":0,"bury_style_show":1,"cell_ctrls":{"cell_flag":0,"cell_layout_style":1,"cell_height":0,"content_decoration":null,"need_client_impr_recycle":1},"cell_type":202,"comment_count":0,"content_decoration":"","cursor":1588775234000,"data_type":1,"digg_count":0,"has_m3u8_video":false,"has_mp4_video":0,"has_video":false,"hot":0,"id":6623262948439621895,"ignore_web_transform":0,"interaction_data":"","is_subject":false,"item_version":0,"level":0,"log_pb":{"author_id":"5857262808","impr_id":"202005062227140100260601540A3178C9","is_following":"0"},"raw_data":{"content":{"answer":{"abstract_text":"刚在《毒液》里看见客串的老爷子，转眼间英雄已逝，一个时代结束了。\u3000\u3000投资界（微信ID：pedaily2012）11月13日消息，据外媒报道，美国漫画界元老级人物斯坦·李于当地时间周一（12日）在好莱坞一家医疗中心去世，享年95岁。\u3000\u3000斯坦·李的个人官方推特发布其去世消息\u3000\u3000漫威影业主席凯文·费吉悼念：“对我的职业生涯和我们在漫威影业所做的一切影响最大的人，就是斯坦·李了。”\u3000\u3000DC官推悼念斯坦·李：“他改变了我们看英雄的方式，现代漫画将一直有他不可磨灭的印记，他那感染人心的热情，让我们想起自己爱上这些故事的初心。”\u3000\u3000这个超级英雄应该是去拯救宇宙了。\u3000\u3000拯救宇宙的漫威之父\u3000\u3000可以说，没有斯坦·李就没有现在漫威的成功。\u3000\u3000正因斯坦·李的天才创业和不懈努力，才创造了媲美星球大战的漫威宇宙；也是因为他创作出神奇四侠，才让漫威在白银时代能与DC的超人气“闪电侠”相抗衡，成为齐名的漫画巨头；更是因为美国队长、钢铁侠、蜘蛛侠、雷神、绿巨人、金刚狼等的存在，才会有我们幼年伟大的英雄梦想。\u3000\u3000斯坦·李原名斯坦利·马丁·利博，1922年12月28日出生在纽约。斯坦·李从小就喜欢阅读神秘小说和冒险故事，热爱写作。为了补贴家用，小斯坦利到处找活干。他曾给报纸长期写过讣闻，帮美国国家结核病中心写过新闻通稿，帮餐馆送过三明治外卖，做过制裤公司的杂工，做过百老汇大戏院的引座员，还做过《纽约先驱论坛报》的订报员。\u3000\u30001939年，16岁的斯坦利从高中毕业。在舅舅的介绍下，斯坦利跟当时的通俗杂志和漫画书出版商马丁·古德曼见了一面。古德曼同意让斯坦利到自己的Timely漫画公司做助理，周薪是8美元。而Timely就是漫威的前身。\u3000\u30001941年，是漫威史上的重要转折点。这一年，漫威漫画的编辑部作出了创作一部“涵盖爱国主义精神”的漫画，用以契合当时正在白热化开展的第二次世界大战的宏观背景，而这便是后来家喻户晓的《美国队长》。\u3000\u3000同年，斯坦利生平第一部作品问世，即《美国队长》系列漫画的第三部，影响了漫威漫画此后半个世纪发展。1961年11月，《神奇四侠》诞生，斯坦·李在漫画界成为焦点。\u3000\u3000后来在搭档漫画家杰克·科比的协助下，创作了《蜘蛛侠》、《钢铁侠》、《雷神托尔》、《绿巨人》、《X战警》、《奇异博士》等漫画角色，并开创了专属于斯坦·李的“神奇模式”。\u3000\u3000斯坦·李的每一部漫画、每一部电影都向我们展现了无与伦比的想象力与庞大的世界观。在他的笔下，公司一步步走向神坛，是毫无争议的漫威之父。\u3000\u30001996 年，阿维·阿拉德开始领导漫威，成立漫威影业。1998 年斯坦·李参与编剧，漫威和新线电影共同制作的《刀锋战士》大获成功。\u3000\u3000也在同年，斯坦·李离开了漫威，成立了“斯坦·李传媒”公司。但因经营不善，2001 年初就倒闭了。2002年，他与人合作创办了POW！娱乐，这家公司2017年5月，被被中国综合型文化产业集团承兴国际集团收购。\u3000\u3000除了创作漫画，斯坦·李也很喜欢“演”。他在世时曾表示，“我骄傲的是，也许我做的一些事情能娱乐到他人。”他也确实做到了，他相继客串出演了《蜘蛛侠》、《X战警》、《神奇四侠》、《钢铁侠》、《美国队长》《雷神托尔》、《无敌浩克》、《复仇者联盟》、《超凡蜘蛛侠》等电影，借客串的演员身份获得“美国全角色历史最高票房演员”。也成了漫威迷们看电影时最大的彩蛋。\u3000\u3000蜘蛛人是斯坦·李最钟爱的形象。不似外太空的超级物种，蜘蛛侠是一个有关成长的漫画在获得超人能力的同时，还要面对学业、生活、女朋友、家庭、人际关系等问题。斯坦·李在接受美国媒体采访时说，“我的所有超级英雄都有人的缺点，我努力表现他们尽管有超人的力量，但他们的生活并不完美。”\u3000\u3000几十年来，斯坦·李几乎每周都同时创作两本漫画，最多时达5本，作品占漫威总量的90%以上。在2002年出版的传记中，他写道：“如果我可以完全真诚地袒露心迹，那么我可以说我就是自己最大的粉丝。”\u3000\u3000打造超级英雄IP，漫威的从0到1\u3000\u3000令人艳羡的漫威英雄IP的打造并不是一开始就是成功的。它在中国也走了一段从0到1的过程。\u3000\u3000最开始，由于受众基础薄弱，英雄IP的受众并不广泛，连续数部电影票房、口碑表现都不理想。比如最开始推出的《无敌浩克》、《钢铁侠2》、《美国队长》、《雷神》中，除已经有一定知名度的《钢铁侠2》取得了1.75亿票房外，其余几部电影票房均未过亿，按照汇率来看甚至不到北美票房的十分之一。整体的市场表现全看档期选择和运气。\u3000\u3000但漫威很聪明，它知道一根火柴的力量渺小，但一盒火柴的力量将能点燃各个受众的心。所以经过了整整十年的布局，以三部《复仇者联盟》为节点，漫威正式走上了“占领心智、发家致富”的道路。\u3000\u3000通过前期的铺路，加深观众对英雄的了解，漫威于是2012年打响了团战的第一炮《复联》。它将英雄基于一战，一起点燃各个英雄粉丝的热情。而《复联1》也在中国实现了爆发式表现，首日6600万的成绩单，两天狂收1.14亿人民币，轻松创下超级英雄电影在华的首映新纪录。而影片在三四线城市的活跃度提升到了40%左右。\u3000\u3000也就是从这一次抱团出战开始，漫威电影的票房权重一路上扬，平均达到15%以上。而单个作品的票房也都保持在了5亿以上。\u3000\u3000（图片来源于网络）\u3000\u3000当然，这只是漫威的第一步，之后《复仇者联盟2》成功斩获14.22亿元，成为内地史上首部在收获10亿+的漫威电影。\u3000\u3000中国市场的良好表现，让漫威受宠若惊。\u3000\u3000其实，从2008年到2018年，经历了90后从学生时代步入到社会工作的过程，而漫威的英雄更加具有陪伴意义。更重要的是，在漫威发展的过程中，中国内地电影市场也在不断向前。2012年—2015年，内地票房的年增速都在30%左右，2015年更是达到了夸张的49%，大量观众开始走进影院，许多进口片都因此而收获了不错的成绩。\u3000\u3000斯坦.李曾表示：中国将成为世界的影视中心，这个世界人口最多的国家需要有自己的超级英雄。就在2017年，漫威就宣布将和网易合作，首创中国的超级英雄：气旋和林烈。在将来这些“中国化”的本土英雄很可能与钢铁侠等初代超级英雄并肩作战。\u3000\u3000据官方宣布，2020年正式推出全沉浸式超级英雄主题公园，新增的三个漫威主题园区分别位于美国加利福尼亚州、法国巴黎以及中国香港。\u3000\u300010年超160亿美元票房的漫威宇宙\u3000\u3000漫威漫画公司创建于1939年，当年10月，第一本漫画推向市场，同时创造了它第一个超级英雄海王纳摩。1941年3月推出的美国队长再次引起轰动，第一次出场，就卖出了100万册的漫画。此后，漫威又陆续推出了绿巨人、蜘蛛侠、雷神、钢铁侠等超级英雄。\u3000\u3000漫威的命运也像它的英雄们一样跌宕起伏，经历了二战等一系列事故，漫威被多次转手：1986 年，漫威被母公司Cadence Industries卖给了New World Pictures；3年后，又被卖给了MacAndrews \\u0026 Forbes Holdings1994年，Andrews Grou和ME又将漫威改组成为漫威控股公司；1996 年，漫威被卷入Carl Icahn和Perelman间的权力斗争。当年12月27 日，漫威正式宣布破产，之后又在多方帮助下，脱离了破产的窘境。\u3000\u3000漫画行业整体衰败，漫威陷入了财政危机。为了渡过难关，漫威决定出售超级英雄的电影拍摄权。1999年，漫威700万美元把《蜘蛛侠》电影版版权卖给了索尼。后者通过《蜘蛛侠》前两部电影大赚16亿美元，但只有7500万属于漫威。\u3000\u30002005年，对分成不满的漫威成立了影业公司。随后从美林银行贷款2.25亿美元投资了《钢铁侠》，背水一战。豪赌成功了，《钢铁侠》全球取得5.85亿美元票房，帮助漫威摆脱窘境。3部《钢铁侠》电影下来全球总票房高达23.8亿美元，3部电影的DVD总共卖出了1700多万份，赚了3亿美元，成为全球最赚钱的系列电影之一。\u3000\u30002009 年，迪士尼以42.4亿美元现金加股票的价格，收购漫威娱乐。2013年起，在迪士尼的主导下，漫威逐渐开始收回散落各处的超级英雄电影版权。漫威成了迪士尼的一部赚钱机器：电影、动画、玩具、游戏、乐园在一条产业链不断衍生发展。\u3000\u3000凭借《X战警》、《蜘蛛侠》横扫美国票房后，漫威开始了自制超级英雄大片的道路，推出了漫威电影宇宙（Marvel Cinematic Universe）计划。自2008年起，一整套清晰完整的电影计划浮出水面，钢铁侠、雷神、美国队长，金刚狼……一个又一个的超级英雄陆续走上银幕，既能孤胆英雄拯救世界，又能合体打怪兽，随后通过《复仇者联盟》将他们集结起来。\u3000\u3000第一阶段，漫威凭借6部影片，以总计10亿美元的成本取得了37.4亿美元的全球票房。第二阶段仅《X战警》就带来了近40亿美元的回报，第三阶段也已进入了筹备拍摄阶段。\u3000\u300078年来，漫威不断推出、贩卖虚拟世界里的英雄。队伍人员日渐壮大，超级英雄的生意也越做越大。大荧幕上超级英雄层出不穷，漫威也没有放过小屏幕。先后推出《神盾局特工》和《卡特特工》两部美剧，剧情紧扣大电影，神盾局为大电影穿针引线，电影、电视剧环环相扣，共同打造出气势恢宏、场面磅礴的漫威帝国。从漫画到电影、电视剧，从游戏到衍生品。\u3000\u3000作为打造超级IP的帝国，漫威做了非常好的榜样。漫威电影宇宙目前全球总票房早已超过了160亿美元，按日前汇率计算折合人民币超1100亿元。\u3000\u3000自大的托尼、正义的美队、嘴炮蜘蛛侠、聪明的班纳、邪魅的洛基、豪爽的雷神、感性的星爵、绯红女巫、无敌的浩克、理性的奇异博士、天真的格鲁特、帅气酷炫的黑豹、战争机器、猎鹰、性感的黑寡妇……“我们爱每一个超级英雄。”\u3000\u3000结语\u3000\u3000英雄们如期赴约，一次次点燃粉丝们内心的激情。从学生到职场，从青年到父母，这些英雄早已不是一个个IP那么简单。\u3000\u3000但如今，江湖失去了金庸大师，漫威世界憾别斯坦·李。从来都是偶像易有，大英雄百年难得。新旧更迭，超级英雄陪着我们逐渐老去，深深的目光中，都有自己年幼的身影。\u3000\u3000美国队长扮演者克里斯·埃文斯悼念：“不会再有另一个斯坦·李了。”","ansid":"6623262948439621895","answer_detail_schema":"sslocal://wenda_detail?ansid=6623262948439621895\\u0026answer_type=0\\u0026api_param=%7B%22answer_list%22%3A%5B6623262948439621895%5D%2C%22answer_type%22%3A%22combine_answer%22%2C%22enter_ansid%22%3A%226623262948439621895%22%2C%22enter_from%22%3A%22click_pgc%22%2C%22from%22%3A%22outer%22%2C%22has_more%22%3Atrue%2C%22in_offset%22%3A0%2C%22next_offset%22%3A1%2C%22origin_from%22%3A%22click_pgc%22%7D\\u0026gd_ext_json=%7B%22enter_from%22%3A%22click_pgc%22%2C%22ansid%22%3A%226623262948439621895%22%2C%22enterfrom_answerid%22%3A%226623262948439621895%22%2C%22parent_enterfrom%22%3A%22%22%2C%22qid%22%3A%226623196249208127758%22%2C%22category_name%22%3A%22profile_wenda%22%2C%22author_id%22%3A%225857262808%22%2C%22article_type%22%3A%22wenda%22%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202005062227140100260601540A3178C9%22%7D%2C%22from_gid%22%3A%22%22%2C%22with_avatar%22%3A%220%22%7D\\u0026video_type=0","answer_list_schema":"","answer_type":0,"brow_count":3246,"comment_count":0,"comment_schema":"sslocal://wenda_detail?ansid=6623262948439621895\\u0026answer_type=0\\u0026api_param=%7B%22answer_list%22%3A%5B6623262948439621895%5D%2C%22answer_type%22%3A%22combine_answer%22%2C%22enter_ansid%22%3A%226623262948439621895%22%2C%22enter_from%22%3A%22click_pgc%22%2C%22from%22%3A%22outer%22%2C%22has_more%22%3Atrue%2C%22in_offset%22%3A0%2C%22next_offset%22%3A1%2C%22origin_from%22%3A%22click_pgc%22%7D\\u0026gd_ext_json=%7B%22enter_from%22%3A%22click_pgc%22%2C%22ansid%22%3A%226623262948439621895%22%2C%22enterfrom_answerid%22%3A%226623262948439621895%22%2C%22parent_enterfrom%22%3A%22%22%2C%22qid%22%3A%226623196249208127758%22%2C%22category_name%22%3A%22profile_wenda%22%2C%22author_id%22%3A%225857262808%22%2C%22article_type%22%3A%22wenda%22%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202005062227140100260601540A3178C9%22%7D%2C%22from_gid%22%3A%22%22%2C%22with_avatar%22%3A%220%22%7D\\u0026is_jump_comment=1\\u0026show_write_comment_dialog=1\\u0026video_type=0","content_abstract":{"large_image_list":[{"height":416,"type":1,"uri":"113f2000048c8a81abb64","url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~960x0.image?from=wenda","url_list":[{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~960x0.image?from=wenda"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~960x0.image?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~960x0.image?from=wenda"}],"width":539},{"height":604,"type":1,"uri":"db14000159bfb5be2a2d","url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~960x0.image?from=wenda","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~960x0.image?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~960x0.image?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~960x0.image?from=wenda"}],"width":500}],"origin_image_list":[{"height":416,"type":1,"uri":"113f2000048c8a81abb64","url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~0x0.image?from=wenda","url_list":[{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~0x0.image?from=wenda"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~0x0.image?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~0x0.image?from=wenda"}],"width":539},{"height":604,"type":1,"uri":"db14000159bfb5be2a2d","url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~0x0.image?from=wenda","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~0x0.image?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~0x0.image?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~0x0.image?from=wenda"}],"width":500}],"text":"刚在《毒液》里看见客串的老爷子，转眼间英雄已逝，一个时代结束了。\\n\u3000\u3000投资界（微信ID：pedaily2012）11月13日消息，据外媒报道，美国漫画界元老级人物斯坦·李于当地时间周一（12日）在好莱坞一家医疗中心去世，享年95岁。\\n\u3000\u3000斯坦·李的个人官方推特发布其去世消息\\n\u3000\u3000漫威影业主席凯文·费吉悼念：“对我的职业生涯和我们在漫威影业所做的一切影响最大的人，就是斯坦·李了。”\\n\u3000\u3000DC官推悼念斯坦·李：“他改变了我们看英雄的方式，现代漫画将一直有他不可磨灭的印记，他那感染人心的热情，让我们想起自己爱上这些故事的初心。”\\n\u3000\u3000这个超级英雄应该是去拯救宇宙了。\\n\u3000\u3000拯救宇宙的漫威之父\\n\u3000\u3000可以说，没有斯坦·李就没有现在漫威的成功。\\n\u3000\u3000正因斯坦·李的天才创业和不懈努力，才创造了媲美星球大战的漫威宇宙；也是因为他创作出神奇四侠，才让漫威在白银时代能与DC的超人气“闪电侠”相抗衡，成为齐名的漫画巨头；更是因为美国队长、钢铁侠、蜘蛛侠、雷神、绿巨人、金刚狼等的存在，才会有我们幼年伟大的英雄梦想。\\n\u3000\u3000斯坦·李原名斯坦利·马丁·利博，1922年12月28日出生在纽约。斯坦·李从小就喜欢阅读神秘小说和冒险故事，热爱写作。为了补贴家用，小斯坦利到处找活干。他曾给报纸长期写过讣闻，帮美国国家结核病中心写过新闻通稿，帮餐馆送过三明治外卖，做过制裤公司的杂工，做过百老汇大戏院的引座员，还做过《纽约先驱论坛报》的订报员。\\n\u3000\u30001939年，16岁的斯坦利从高中毕业。在舅舅的介绍下，斯坦利跟当时的通俗杂志和漫画书出版商马丁·古德曼见了一面。古德曼同意让斯坦利到自己的Timely漫画公司做助理，周薪是8美元。而Timely就是漫威的前身。\\n\u3000\u30001941年，是漫威史上的重要转折点。这一年，漫威漫画的编辑部作出了创作一部“涵盖爱国主义精神”的漫画，用以契合当时正在白热化开展的第二次世界大战的宏观背景，而这便是后来家喻户晓的《美国队长》。\\n\u3000\u3000同年，斯坦利生平第一部作品问世，即《美国队长》系列漫画的第三部，影响了漫威漫画此后半个世纪发展。1961年11月，《神奇四侠》诞生，斯坦·李在漫画界成为焦点。\\n\u3000\u3000后来在搭档漫画家杰克·科比的协助下，创作了《蜘蛛侠》、《钢铁侠》、《雷神托尔》、《绿巨人》、《X战警》、《奇异博士》等漫画角色，并开创了专属于斯坦·李的“神奇模式”。\\n\u3000\u3000斯坦·李的每一部漫画、每一部电影都向我们展现了无与伦比的想象力与庞大的世界观。在他的笔下，公司一步步走向神坛，是毫无争议的漫威之父。\\n\u3000\u30001996 年，阿维·阿拉德开始领导漫威，成立漫威影业。1998 年斯坦·李参与编剧，漫威和新线电影共同制作的《刀锋战士》大获成功。\\n\u3000\u3000也在同年，斯坦·李离开了漫威，成立了“斯坦·李传媒”公司。但因经营不善，2001 年初就倒闭了。2002年，他与人合作创办了POW！娱乐，这家公司2017年5月，被被中国综合型文化产业集团承兴国际集团收购。\\n\u3000\u3000除了创作漫画，斯坦·李也很喜欢“演”。他在世时曾表示，“我骄傲的是，也许我做的一些事情能娱乐到他人。”他也确实做到了，他相继客串出演了《蜘蛛侠》、《X战警》、《神奇四侠》、《钢铁侠》、《美国队长》《雷神托尔》、《无敌浩克》、《复仇者联盟》、《超凡蜘蛛侠》等电影，借客串的演员身份获得“美国全角色历史最高票房演员”。也成了漫威迷们看电影时最大的彩蛋。\\n\u3000\u3000蜘蛛人是斯坦·李最钟爱的形象。不似外太空的超级物种，蜘蛛侠是一个有关成长的漫画在获得超人能力的同时，还要面对学业、生活、女朋友、家庭、人际关系等问题。斯坦·李在接受美国媒体采访时说，“我的所有超级英雄都有人的缺点，我努力表现他们尽管有超人的力量，但他们的生活并不完美。”\\n\u3000\u3000几十年来，斯坦·李几乎每周都同时创作两本漫画，最多时达5本，作品占漫威总量的90%以上。在2002年出版的传记中，他写道：“如果我可以完全真诚地袒露心迹，那么我可以说我就是自己最大的粉丝。”\\n\u3000\u3000打造超级英雄IP，漫威的从0到1\\n\u3000\u3000令人艳羡的漫威英雄IP的打造并不是一开始就是成功的。它在中国也走了一段从0到1的过程。\\n\u3000\u3000最开始，由于受众基础薄弱，英雄IP的受众并不广泛，连续数部电影票房、口碑表现都不理想。比如最开始推出的《无敌浩克》、《钢铁侠2》、《美国队长》、《雷神》中，除已经有一定知名度的《钢铁侠2》取得了1.75亿票房外，其余几部电影票房均未过亿，按照汇率来看甚至不到北美票房的十分之一。整体的市场表现全看档期选择和运气。\\n\u3000\u3000但漫威很聪明，它知道一根火柴的力量渺小，但一盒火柴的力量将能点燃各个受众的心。所以经过了整整十年的布局，以三部《复仇者联盟》为节点，漫威正式走上了“占领心智、发家致富”的道路。\\n\u3000\u3000通过前期的铺路，加深观众对英雄的了解，漫威于是2012年打响了团战的第一炮《复联》。它将英雄基于一战，一起点燃各个英雄粉丝的热情。而《复联1》也在中国实现了爆发式表现，首日6600万的成绩单，两天狂收1.14亿人民币，轻松创下超级英雄电影在华的首映新纪录。而影片在三四线城市的活跃度提升到了40%左右。\\n\u3000\u3000也就是从这一次抱团出战开始，漫威电影的票房权重一路上扬，平均达到15%以上。而单个作品的票房也都保持在了5亿以上。\\n\u3000\u3000（图片来源于网络）\\n\u3000\u3000当然，这只是漫威的第一步，之后《复仇者联盟2》成功斩获14.22亿元，成为内地史上首部在收获10亿+的漫威电影。\\n\u3000\u3000中国市场的良好表现，让漫威受宠若惊。\\n\u3000\u3000其实，从2008年到2018年，经历了90后从学生时代步入到社会工作的过程，而漫威的英雄更加具有陪伴意义。更重要的是，在漫威发展的过程中，中国内地电影市场也在不断向前。2012年—2015年，内地票房的年增速都在30%左右，2015年更是达到了夸张的49%，大量观众开始走进影院，许多进口片都因此而收获了不错的成绩。\\n\u3000\u3000斯坦.李曾表示：中国将成为世界的影视中心，这个世界人口最多的国家需要有自己的超级英雄。就在2017年，漫威就宣布将和网易合作，首创中国的超级英雄：气旋和林烈。在将来这些“中国化”的本土英雄很可能与钢铁侠等初代超级英雄并肩作战。\\n\u3000\u3000据官方宣布，2020年正式推出全沉浸式超级英雄主题公园，新增的三个漫威主题园区分别位于美国加利福尼亚州、法国巴黎以及中国香港。\\n\u3000\u300010年超160亿美元票房的漫威宇宙\\n\u3000\u3000漫威漫画公司创建于1939年，当年10月，第一本漫画推向市场，同时创造了它第一个超级英雄海王纳摩。1941年3月推出的美国队长再次引起轰动，第一次出场，就卖出了100万册的漫画。此后，漫威又陆续推出了绿巨人、蜘蛛侠、雷神、钢铁侠等超级英雄。\\n\u3000\u3000漫威的命运也像它的英雄们一样跌宕起伏，经历了二战等一系列事故，漫威被多次转手：1986 年，漫威被母公司Cadence Industries卖给了New World Pictures；3年后，又被卖给了MacAndrews \\u0026 Forbes Holdings1994年，Andrews Grou和ME又将漫威改组成为漫威控股公司；1996 年，漫威被卷入Carl Icahn和Perelman间的权力斗争。当年12月27 日，漫威正式宣布破产，之后又在多方帮助下，脱离了破产的窘境。\\n\u3000\u3000漫画行业整体衰败，漫威陷入了财政危机。为了渡过难关，漫威决定出售超级英雄的电影拍摄权。1999年，漫威700万美元把《蜘蛛侠》电影版版权卖给了索尼。后者通过《蜘蛛侠》前两部电影大赚16亿美元，但只有7500万属于漫威。\\n\u3000\u30002005年，对分成不满的漫威成立了影业公司。随后从美林银行贷款2.25亿美元投资了《钢铁侠》，背水一战。豪赌成功了，《钢铁侠》全球取得5.85亿美元票房，帮助漫威摆脱窘境。3部《钢铁侠》电影下来全球总票房高达23.8亿美元，3部电影的DVD总共卖出了1700多万份，赚了3亿美元，成为全球最赚钱的系列电影之一。\\n\u3000\u30002009 年，迪士尼以42.4亿美元现金加股票的价格，收购漫威娱乐。2013年起，在迪士尼的主导下，漫威逐渐开始收回散落各处的超级英雄电影版权。漫威成了迪士尼的一部赚钱机器：电影、动画、玩具、游戏、乐园在一条产业链不断衍生发展。\\n\u3000\u3000凭借《X战警》、《蜘蛛侠》横扫美国票房后，漫威开始了自制超级英雄大片的道路，推出了漫威电影宇宙（Marvel Cinematic Universe）计划。自2008年起，一整套清晰完整的电影计划浮出水面，钢铁侠、雷神、美国队长，金刚狼……一个又一个的超级英雄陆续走上银幕，既能孤胆英雄拯救世界，又能合体打怪兽，随后通过《复仇者联盟》将他们集结起来。\\n\u3000\u3000第一阶段，漫威凭借6部影片，以总计10亿美元的成本取得了37.4亿美元的全球票房。第二阶段仅《X战警》就带来了近40亿美元的回报，第三阶段也已进入了筹备拍摄阶段。\\n\u3000\u300078年来，漫威不断推出、贩卖虚拟世界里的英雄。队伍人员日渐壮大，超级英雄的生意也越做越大。大荧幕上超级英雄层出不穷，漫威也没有放过小屏幕。先后推出《神盾局特工》和《卡特特工》两部美剧，剧情紧扣大电影，神盾局为大电影穿针引线，电影、电视剧环环相扣，共同打造出气势恢宏、场面磅礴的漫威帝国。从漫画到电影、电视剧，从游戏到衍生品。\\n\u3000\u3000作为打造超级IP的帝国，漫威做了非常好的榜样。漫威电影宇宙目前全球总票房早已超过了160亿美元，按日前汇率计算折合人民币超1100亿元。\\n\u3000\u3000自大的托尼、正义的美队、嘴炮蜘蛛侠、聪明的班纳、邪魅的洛基、豪爽的雷神、感性的星爵、绯红女巫、无敌的浩克、理性的奇异博士、天真的格鲁特、帅气酷炫的黑豹、战争机器、猎鹰、性感的黑寡妇……“我们爱每一个超级英雄。”\\n\u3000\u3000结语\\n\u3000\u3000英雄们如期赴约，一次次点燃粉丝们内心的激情。从学生到职场，从青年到父母，这些英雄早已不是一个个IP那么简单。\\n\u3000\u3000但如今，江湖失去了金庸大师，漫威世界憾别斯坦·李。从来都是偶像易有，大英雄百年难得。新旧更迭，超级英雄陪着我们逐渐老去，深深的目光中，都有自己年幼的身影。\\n\u3000\u3000美国队长扮演者克里斯·埃文斯悼念：“不会再有另一个斯坦·李了。”","thumb_image_list":[{"height":415,"type":1,"uri":"113f2000048c8a81abb64","url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~539x415_cs.jpeg?from=wenda","url_list":[{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~539x415_cs.jpeg?from=wenda"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~539x415_cs.jpeg?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~539x415_cs.jpeg?from=wenda"}],"width":539},{"height":533,"type":1,"uri":"db14000159bfb5be2a2d","url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~500x533_cs.jpeg?from=wenda","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~500x533_cs.jpeg?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~500x533_cs.jpeg?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~500x533_cs.jpeg?from=wenda"}],"width":500}],"video_list":[],"wenda_cv_image_list":null},"create_time":1542098575,"digg_count":7,"display_count":0,"forward_count":0,"interactive_data":{"comment_list":[],"digg_user_list":null,"style_ctrls":{"ban_comment":0,"ban_face":0,"ban_pic_comment":0,"comment_entrance":0,"comment_show_more_schema":"","comment_show_more_text":"","digg_show_more_schema":"","digg_show_more_text":"","max_comment_line":4,"max_digg_line":2,"show_repost_entrance":0,"style_type":3}},"is_digg":0,"large_image_list":[{"height":416,"type":1,"uri":"113f2000048c8a81abb64","url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~960x0.jpeg?from=wenda","url_list":[{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~960x0.jpeg?from=wenda"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~960x0.jpeg?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~960x0.jpeg?from=wenda"}],"width":539},{"height":604,"type":1,"uri":"db14000159bfb5be2a2d","url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~960x0.jpeg?from=wenda","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~960x0.jpeg?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~960x0.jpeg?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~960x0.jpeg?from=wenda"}],"width":500}],"max_lines":20,"origin_image_list":[{"height":416,"type":1,"uri":"113f2000048c8a81abb64","url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~0x0.jpeg?from=wenda","url_list":[{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~0x0.jpeg?from=wenda"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~0x0.jpeg?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~0x0.jpeg?from=wenda"}],"width":539},{"height":604,"type":1,"uri":"db14000159bfb5be2a2d","url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~0x0.jpeg?from=wenda","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~0x0.jpeg?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~0x0.jpeg?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~0x0.jpeg?from=wenda"}],"width":500}],"perm":{"can_ban_comment":0,"can_comment_answer":1,"can_delete_answer":0,"can_delete_comment":0,"can_digg_answer":1,"can_edit_answer":0,"can_post_answer":1,"delete_answer_tips":"","edit_answer_tips":"","show_delete_answer":0,"show_edit_answer":0},"read_count":0,"show_count":3246,"show_lines":8,"show_text":"阅读","status":0,"thumb_image_list":[{"height":415,"type":1,"uri":"113f2000048c8a81abb64","url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~539x415_cs.jpeg?from=wenda","url_list":[{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~539x415_cs.jpeg?from=wenda"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~539x415_cs.jpeg?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113f2000048c8a81abb64~539x415_cs.jpeg?from=wenda"}],"width":539},{"height":533,"type":1,"uri":"db14000159bfb5be2a2d","url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~500x533_cs.jpeg?from=wenda","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~500x533_cs.jpeg?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~500x533_cs.jpeg?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/db14000159bfb5be2a2d~500x533_cs.jpeg?from=wenda"}],"width":500}],"video_type":"0"},"cell_layout_style":0,"comment_schema":"sslocal://wenda_detail?ansid=6623262948439621895\\u0026answer_type=0\\u0026api_param=%7B%22answer_list%22%3A%5B6623262948439621895%5D%2C%22answer_type%22%3A%22combine_answer%22%2C%22enter_ansid%22%3A%226623262948439621895%22%2C%22enter_from%22%3A%22click_pgc%22%2C%22from%22%3A%22outer%22%2C%22has_more%22%3Atrue%2C%22in_offset%22%3A0%2C%22next_offset%22%3A1%2C%22origin_from%22%3A%22click_pgc%22%7D\\u0026gd_ext_json=%7B%22enter_from%22%3A%22click_pgc%22%2C%22ansid%22%3A%226623262948439621895%22%2C%22enterfrom_answerid%22%3A%226623262948439621895%22%2C%22parent_enterfrom%22%3A%22%22%2C%22qid%22%3A%226623196249208127758%22%2C%22category_name%22%3A%22profile_wenda%22%2C%22author_id%22%3A%225857262808%22%2C%22article_type%22%3A%22wenda%22%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202005062227140100260601540A3178C9%22%7D%2C%22from_gid%22%3A%22%22%2C%22with_avatar%22%3A%220%22%7D\\u0026is_jump_comment=1\\u0026show_write_comment_dialog=1\\u0026video_type=0","default_lines":3,"filter_words":[{"id":"8:0","is_selected":false,"name":"看过了"},{"id":"9:1","is_selected":false,"name":"内容太水"},{"id":"5:6623262948439621895","is_selected":false,"name":"拉黑作者:投资界"}],"hide_create_time":0,"image_type":0,"jump_type":1,"layout_type":1,"max_lines":6,"question":{"answer_count_description":"7人回答了问题","answer_user_list":[{"avatar_url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/11340/6310107700~120x256.image","is_following":0,"is_verify":0,"uname":"投资界","user_auth_info":"","user_id":"5857262808","user_schema":"","v_icon":""},{"avatar_url":"http://p0.pstatp.com/origin/3791/5035712059","is_following":0,"is_verify":0,"uname":"","user_auth_info":"","user_id":"","user_schema":"","v_icon":""},{"avatar_url":"http://p0.pstatp.com/origin/3791/5035712059","is_following":0,"is_verify":0,"uname":"","user_auth_info":"","user_id":"","user_schema":"","v_icon":""}],"concern_tag_list":[{"concern_id":"6213178576385083905","name":"漫威漫画","schema":"sslocal://concern?api_param=%7B%22wenda_api_param%22%3A%7B%7D%7D\\u0026cid=6213178576385083905\\u0026tab_sname=wenda"},{"concern_id":"6215497895852902913","name":"动漫","schema":"sslocal://concern?api_param=%7B%22wenda_api_param%22%3A%7B%7D%7D\\u0026cid=6215497895852902913\\u0026tab_sname=wenda"},{"concern_id":"6215497896830175745","name":"娱乐","schema":"sslocal://concern?api_param=%7B%22wenda_api_param%22%3A%7B%7D%7D\\u0026cid=6215497896830175745\\u0026tab_sname=wenda"},{"concern_id":"6215497897710979586","name":"文化","schema":"sslocal://concern?api_param=%7B%22wenda_api_param%22%3A%7B%7D%7D\\u0026cid=6215497897710979586\\u0026tab_sname=wenda"}],"content":{"content_rich_span":"{\\"links\\":[]}","large_image_list":[{"height":364,"type":1,"uri":"","url":"http://p3.pstatp.com/thumb/2c650017572758251817","url_list":[{"url":"http://p3.pstatp.com/thumb/2c650017572758251817"}],"width":360}],"origin_image_list":[{"height":364,"type":1,"uri":"","url":"http://p3.pstatp.com/thumb/2c650017572758251817","url_list":[{"url":"http://p3.pstatp.com/thumb/2c650017572758251817"}],"width":360}],"quest_large_image_list":[],"quest_origin_image_list":[],"quest_thumb_image_list":[],"rich_text":"当地时间12日，美国漫画界元老级人物斯坦·李在好莱坞一家医疗中心去世，享年95岁。可以说，斯坦·李创造了美国的漫画宇宙。这位兼作家、编辑和出版商为一身的漫画家创作了包括钢铁侠、蜘蛛侠、X战警、雷神、黑豹和神奇四人等漫威标志性角色。他白手起家，凭借创作才华和惊人的商业头脑振兴了漫威，却晚年被卷入丑闻中。","text":"当地时间12日，美国漫画界元老级人物斯坦·李在好莱坞一家医疗中心去世，享年95岁。可以说，斯坦·李创造了美国的漫画宇宙。这位兼作家、编辑和出版商为一身的漫画家创作了包括钢铁侠、蜘蛛侠、X战警、雷神、黑豹和神奇四人等漫威标志性角色。他白手起家，凭借创作才华和惊人的商业头脑振兴了漫威，却晚年被卷入丑闻中。","thumb_image_list":[{"height":364,"type":1,"uri":"","url":"http://p3.pstatp.com/thumb/2c650017572758251817","url_list":[{"url":"http://p3.pstatp.com/thumb/2c650017572758251817"}],"width":360}]},"count_statistics":[{"count_name":"收藏量","count_num":"1","count_type":1}],"create_time":1542083046,"follow_count":0,"is_anonymous":0,"is_question_delete":0,"main_question_info":"","nice_ans_count":3,"normal_ans_count":4,"qid":"6623196249208127758","question_list_schema":"sslocal://wenda_list?api_param=%7B%22enter_ansid%22%3A%226623262948439621895%22%2C%22enter_from%22%3A%22click_pgc%22%2C%22no_enter_ansid%22%3A%22%22%2C%22origin_from%22%3A%22click_pgc%22%7D\\u0026gd_ext_json=%7B%22enter_from%22%3A%22click_pgc%22%2C%22ansid%22%3A%226623262948439621895%22%2C%22enterfrom_answerid%22%3A%226623262948439621895%22%2C%22parent_enterfrom%22%3A%22%22%2C%22qid%22%3A%226623196249208127758%22%2C%22category_name%22%3A%22profile_wenda%22%2C%22author_id%22%3A%225857262808%22%2C%22article_type%22%3A%22wenda%22%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202005062227140100260601540A3178C9%22%7D%2C%22from_gid%22%3A%22%22%2C%22with_avatar%22%3A%220%22%7D\\u0026qTitle=%22%E6%BC%AB%E5%A8%81%E4%B9%8B%E7%88%B6%22%E6%96%AF%E5%9D%A6%C2%B7%E6%9D%8E%E5%8E%BB%E4%B8%96%EF%BC%8C%E4%BD%A0%E6%80%8E%E4%B9%88%E7%9C%8B%EF%BC%9F\\u0026qid=6623196249208127758","repost_params":{"cover_url":"http://p3.pstatp.com/origin/18a300102cab5d8d0e05","fw_id":6623196249208127758,"fw_id_type":1026,"fw_user_id":94552783900,"opt_id":6623196249208127758,"opt_id_type":1026,"repost_type":218,"schema":"","title":"\\"漫威之父\\"斯坦·李去世，你怎么看？"},"status":0,"tips":{"tips_button_text":"","tips_schema":"","tips_text":"","tips_type":0},"title":"\\"漫威之父\\"斯坦·李去世，你怎么看？","user":{"avatar_url":"http://p1.pstatp.com/thumb/da72000130f6cbc75268","is_following":0,"is_verify":0,"uname":"鲸鱼小姐Milk","user_auth_info":"","user_id":"94552783900","user_intro":"","user_schema":"sslocal://profile?api_param=%7B%22enter_from%22%3A%22click_pgc%22%2C%22origin_from%22%3A%22click_pgc%22%7D\\u0026gd_ext_json=%7B%22enter_from%22%3A%22click_pgc%22%2C%22ansid%22%3A%22%22%2C%22enterfrom_answerid%22%3A%22%22%2C%22parent_enterfrom%22%3A%22%22%2C%22qid%22%3A%226623196249208127758%22%2C%22category_name%22%3A%22profile_wenda%22%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202005062227140100260601540A3178C9%22%7D%2C%22from_gid%22%3A%22%22%2C%22with_avatar%22%3A%22%22%7D\\u0026refer=wenda\\u0026uid=94552783900","v_icon":""},"write_answer_schema":"sslocal://wenda_post?api_param=%7B%22enter_from%22%3A%22click_pgc%22%2C%22origin_from%22%3A%22click_pgc%22%7D\\u0026gd_ext_json=%7B%22enter_from%22%3A%22click_pgc%22%2C%22ansid%22%3A%22%22%2C%22enterfrom_answerid%22%3A%22%22%2C%22parent_enterfrom%22%3A%22%22%2C%22qid%22%3A%226623196249208127758%22%2C%22category_name%22%3A%22profile_wenda%22%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202005062227140100260601540A3178C9%22%7D%2C%22from_gid%22%3A%22%22%2C%22with_avatar%22%3A%22%22%7D\\u0026qTitle=%22%E6%BC%AB%E5%A8%81%E4%B9%8B%E7%88%B6%22%E6%96%AF%E5%9D%A6%C2%B7%E6%9D%8E%E5%8E%BB%E4%B8%96%EF%BC%8C%E4%BD%A0%E6%80%8E%E4%B9%88%E7%9C%8B%EF%BC%9F\\u0026qid=6623196249208127758"},"recommend_reason":"回答了问题","repost_params":{"cover_url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/11340/6310107700~120x256.image","fw_id":6623262948439621895,"fw_id_type":1025,"fw_user_id":5857262808,"opt_id":6623262948439621895,"opt_id_type":1025,"repost_type":214,"schema":"","title":"投资界回答了：\\"漫威之父\\"斯坦·李去世，你怎么看？"},"share_info":{"content":"刚在《毒液》里看见客串的老爷子，转眼间英雄已逝，一个时代结束了。\u3000\u3000投资界（微信ID：pedaily2012）11月13日消息，据外媒报道，美国漫画界元老级人物斯坦·李于当地时间周一（12日）在好莱坞一家医疗中心去世，享年95岁。\u3000\u3000斯坦·李的个人官方推特发布其去世消息\u3000\u3000漫威影业主席凯文·费吉悼念：“对我的职业生涯和我们在漫威影业所做的一切影响最大的人，就是斯坦·李了。”\u3000\u3000DC官推悼念斯坦·李：“他改变了我们看英雄的方式，现代漫画将一直有他不可磨灭的印记，他那感染人心的热情，让我们想起自己爱上这些故事的初心。”\u3000\u3000这个超级英雄应该是去拯救宇宙了。\u3000\u3000拯救宇宙的漫威之父\u3000\u3000可以说，没有斯坦·李就没有现在漫威的成功。\u3000\u3000正因斯坦·李的天才创业和不懈努力，才创造了媲美星球大战的漫威宇宙；也是因为他创作出神奇四侠，才让漫威在白银时代能与DC的超人气“闪电侠”相抗衡，成为齐名的漫画巨头；更是因为美国队长、钢铁侠、蜘蛛侠、雷神、绿巨人、金刚狼等的存在，才会有我们幼年伟大的英雄梦想。\u3000\u3000斯坦·李原名斯坦利·马丁·利博，1922年12月28日出生在纽约。斯坦·李从小就喜欢阅读神秘小说和冒险故事，热爱写作。为了补贴家用，小斯坦利到处找活干。他曾给报纸长期写过讣闻，帮美国国家结核病中心写过新闻通稿，帮餐馆送过三明治外卖，做过制裤公司的杂工，做过百老汇大戏院的引座员，还做过《纽约先驱论坛报》的订报员。\u3000\u30001939年，16岁的斯坦利从高中毕业。在舅舅的介绍下，斯坦利跟当时的通俗杂志和漫画书出版商马丁·古德曼见了一面。古德曼同意让斯坦利到自己的Timely漫画公司做助理，周薪是8美元。而Timely就是漫威的前身。\u3000\u30001941年，是漫威史上的重要转折点。这一年，漫威漫画的编辑部作出了创作一部“涵盖爱国主义精神”的漫画，用以契合当时正在白热化开展的第二次世界大战的宏观背景，而这便是后来家喻户晓的《美国队长》。\u3000\u3000同年，斯坦利生平第一部作品问世，即《美国队长》系列漫画的第三部，影响了漫威漫画此后半个世纪发展。1961年11月，《神奇四侠》诞生，斯坦·李在漫画界成为焦点。\u3000\u3000后来在搭档漫画家杰克·科比的协助下，创作了《蜘蛛侠》、《钢铁侠》、《雷神托尔》、《绿巨人》、《X战警》、《奇异博士》等漫画角色，并开创了专属于斯坦·李的“神奇模式”。\u3000\u3000斯坦·李的每一部漫画、每一部电影都向我们展现了无与伦比的想象力与庞大的世界观。在他的笔下，公司一步步走向神坛，是毫无争议的漫威之父。\u3000\u30001996 年，阿维·阿拉德开始领导漫威，成立漫威影业。1998 年斯坦·李参与编剧，漫威和新线电影共同制作的《刀锋战士》大获成功。\u3000\u3000也在同年，斯坦·李离开了漫威，成立了“斯坦·李传媒”公司。但因经营不善，2001 年初就倒闭了。2002年，他与人合作创办了POW！娱乐，这家公司2017年5月，被被中国综合型文化产业集团承兴国际集团收购。\u3000\u3000除了创作漫画，斯坦·李也很喜欢“演”。他在世时曾表示，“我骄傲的是，也许我做的一些事情能娱乐到他人。”他也确实做到了，他相继客串出演了《蜘蛛侠》、《X战警》、《神奇四侠》、《钢铁侠》、《美国队长》《雷神托尔》、《无敌浩克》、《复仇者联盟》、《超凡蜘蛛侠》等电影，借客串的演员身份获得“美国全角色历史最高票房演员”。也成了漫威迷们看电影时最大的彩蛋。\u3000\u3000蜘蛛人是斯坦·李最钟爱的形象。不似外太空的超级物种，蜘蛛侠是一个有关成长的漫画在获得超人能力的同时，还要面对学业、生活、女朋友、家庭、人际关系等问题。斯坦·李在接受美国媒体采访时说，“我的所有超级英雄都有人的缺点，我努力表现他们尽管有超人的力量，但他们的生活并不完美。”\u3000\u3000几十年来，斯坦·李几乎每周都同时创作两本漫画，最多时达5本，作品占漫威总量的90%以上。在2002年出版的传记中，他写道：“如果我可以完全真诚地袒露心迹，那么我可以说我就是自己最大的粉丝。”\u3000\u3000打造超级英雄IP，漫威的从0到1\u3000\u3000令人艳羡的漫威英雄IP的打造并不是一开始就是成功的。它在中国也走了一段从0到1的过程。\u3000\u3000最开始，由于受众基础薄弱，英雄IP的受众并不广泛，连续数部电影票房、口碑表现都不理想。比如最开始推出的《无敌浩克》、《钢铁侠2》、《美国队长》、《雷神》中，除已经有一定知名度的《钢铁侠2》取得了1.75亿票房外，其余几部电影票房均未过亿，按照汇率来看甚至不到北美票房的十分之一。整体的市场表现全看档期选择和运气。\u3000\u3000但漫威很聪明，它知道一根火柴的力量渺小，但一盒火柴的力量将能点燃各个受众的心。所以经过了整整十年的布局，以三部《复仇者联盟》为节点，漫威正式走上了“占领心智、发家致富”的道路。\u3000\u3000通过前期的铺路，加深观众对英雄的了解，漫威于是2012年打响了团战的第一炮《复联》。它将英雄基于一战，一起点燃各个英雄粉丝的热情。而《复联1》也在中国实现了爆发式表现，首日6600万的成绩单，两天狂收1.14亿人民币，轻松创下超级英雄电影在华的首映新纪录。而影片在三四线城市的活跃度提升到了40%左右。\u3000\u3000也就是从这一次抱团出战开始，漫威电影的票房权重一路上扬，平均达到15%以上。而单个作品的票房也都保持在了5亿以上。\u3000\u3000（图片来源于网络）\u3000\u3000当然，这只是漫威的第一步，之后《复仇者联盟2》成功斩获14.22亿元，成为内地史上首部在收获10亿+的漫威电影。\u3000\u3000中国市场的良好表现，让漫威受宠若惊。\u3000\u3000其实，从2008年到2018年，经历了90后从学生时代步入到社会工作的过程，而漫威的英雄更加具有陪伴意义。更重要的是，在漫威发展的过程中，中国内地电影市场也在不断向前。2012年—2015年，内地票房的年增速都在30%左右，2015年更是达到了夸张的49%，大量观众开始走进影院，许多进口片都因此而收获了不错的成绩。\u3000\u3000斯坦.李曾表示：中国将成为世界的影视中心，这个世界人口最多的国家需要有自己的超级英雄。就在2017年，漫威就宣布将和网易合作，首创中国的超级英雄：气旋和林烈。在将来这些“中国化”的本土英雄很可能与钢铁侠等初代超级英雄并肩作战。\u3000\u3000据官方宣布，2020年正式推出全沉浸式超级英雄主题公园，新增的三个漫威主题园区分别位于美国加利福尼亚州、法国巴黎以及中国香港。\u3000\u300010年超160亿美元票房的漫威宇宙\u3000\u3000漫威漫画公司创建于1939年，当年10月，第一本漫画推向市场，同时创造了它第一个超级英雄海王纳摩。1941年3月推出的美国队长再次引起轰动，第一次出场，就卖出了100万册的漫画。此后，漫威又陆续推出了绿巨人、蜘蛛侠、雷神、钢铁侠等超级英雄。\u3000\u3000漫威的命运也像它的英雄们一样跌宕起伏，经历了二战等一系列事故，漫威被多次转手：1986 年，漫威被母公司Cadence Industries卖给了New World Pictures；3年后，又被卖给了MacAndrews \\u0026 Forbes Holdings1994年，Andrews Grou和ME又将漫威改组成为漫威控股公司；1996 年，漫威被卷入Carl Icahn和Perelman间的权力斗争。当年12月27 日，漫威正式宣布破产，之后又在多方帮助下，脱离了破产的窘境。\u3000\u3000漫画行业整体衰败，漫威陷入了财政危机。为了渡过难关，漫威决定出售超级英雄的电影拍摄权。1999年，漫威700万美元把《蜘蛛侠》电影版版权卖给了索尼。后者通过《蜘蛛侠》前两部电影大赚16亿美元，但只有7500万属于漫威。\u3000\u30002005年，对分成不满的漫威成立了影业公司。随后从美林银行贷款2.25亿美元投资了《钢铁侠》，背水一战。豪赌成功了，《钢铁侠》全球取得5.85亿美元票房，帮助漫威摆脱窘境。3部《钢铁侠》电影下来全球总票房高达23.8亿美元，3部电影的DVD总共卖出了1700多万份，赚了3亿美元，成为全球最赚钱的系列电影之一。\u3000\u30002009 年，迪士尼以42.4亿美元现金加股票的价格，收购漫威娱乐。2013年起，在迪士尼的主导下，漫威逐渐开始收回散落各处的超级英雄电影版权。漫威成了迪士尼的一部赚钱机器：电影、动画、玩具、游戏、乐园在一条产业链不断衍生发展。\u3000\u3000凭借《X战警》、《蜘蛛侠》横扫美国票房后，漫威开始了自制超级英雄大片的道路，推出了漫威电影宇宙（Marvel Cinematic Universe）计划。自2008年起，一整套清晰完整的电影计划浮出水面，钢铁侠、雷神、美国队长，金刚狼……一个又一个的超级英雄陆续走上银幕，既能孤胆英雄拯救世界，又能合体打怪兽，随后通过《复仇者联盟》将他们集结起来。\u3000\u3000第一阶段，漫威凭借6部影片，以总计10亿美元的成本取得了37.4亿美元的全球票房。第二阶段仅《X战警》就带来了近40亿美元的回报，第三阶段也已进入了筹备拍摄阶段。\u3000\u300078年来，漫威不断推出、贩卖虚拟世界里的英雄。队伍人员日渐壮大，超级英雄的生意也越做越大。大荧幕上超级英雄层出不穷，漫威也没有放过小屏幕。先后推出《神盾局特工》和《卡特特工》两部美剧，剧情紧扣大电影，神盾局为大电影穿针引线，电影、电视剧环环相扣，共同打造出气势恢宏、场面磅礴的漫威帝国。从漫画到电影、电视剧，从游戏到衍生品。\u3000\u3000作为打造超级IP的帝国，漫威做了非常好的榜样。漫威电影宇宙目前全球总票房早已超过了160亿美元，按日前汇率计算折合人民币超1100亿元。\u3000\u3000自大的托尼、正义的美队、嘴炮蜘蛛侠、聪明的班纳、邪魅的洛基、豪爽的雷神、感性的星爵、绯红女巫、无敌的浩克、理性的奇异博士、天真的格鲁特、帅气酷炫的黑豹、战争机器、猎鹰、性感的黑寡妇……“我们爱每一个超级英雄。”\u3000\u3000结语\u3000\u3000英雄们如期赴约，一次次点燃粉丝们内心的激情。从学生到职场，从青年到父母，这些英雄早已不是一个个IP那么简单。\u3000\u3000但如今，江湖失去了金庸大师，漫威世界憾别斯坦·李。从来都是偶像易有，大英雄百年难得。新旧更迭，超级英雄陪着我们逐渐老去，深深的目光中，都有自己年幼的身影。\u3000\u3000美国队长扮演者克里斯·埃文斯悼念：“不会再有另一个斯坦·李了。”","share_type":{"pyq":0,"qq":0,"qzone":0,"wx":0},"share_url":"http://toutiao.com/group/6623262948439621895/?iid=0\\u0026app=news_article","title":"\\"漫威之父\\"斯坦·李去世，你怎么看？","token_type":0},"summary":"","tail_content":"","user":{"avatar_url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/11340/6310107700~120x256.image","is_following":0,"is_verify":1,"uname":"投资界","user_auth_info":"{\\"auth_type\\":\\"0\\",\\"auth_info\\":\\"优质财经领域创作者\\",\\"other_auth\\":{\\"interest\\":\\"优质财经领域创作者\\"}}","user_id":"5857262808","user_schema":"sslocal://profile?api_param=%7B%22answer_list%22%3A%5B6623262948439621895%5D%2C%22answer_type%22%3A%22combine_answer%22%2C%22enter_ansid%22%3A%226623262948439621895%22%2C%22enter_from%22%3A%22click_pgc%22%2C%22from%22%3A%22outer%22%2C%22has_more%22%3Atrue%2C%22in_offset%22%3A0%2C%22next_offset%22%3A1%2C%22origin_from%22%3A%22click_pgc%22%7D\\u0026gd_ext_json=%7B%22enter_from%22%3A%22click_pgc%22%2C%22ansid%22%3A%226623262948439621895%22%2C%22enterfrom_answerid%22%3A%226623262948439621895%22%2C%22parent_enterfrom%22%3A%22%22%2C%22qid%22%3A%226623196249208127758%22%2C%22category_name%22%3A%22profile_wenda%22%2C%22author_id%22%3A%225857262808%22%2C%22article_type%22%3A%22wenda%22%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202005062227140100260601540A3178C9%22%7D%2C%22from_gid%22%3A%22%22%2C%22with_avatar%22%3A%220%22%7D\\u0026refer=wenda\\u0026uid=5857262808","v_icon":"优质财经领域创作者"}},"group_id":"6623262948439621895","item_id":"6623262948439621895"},"read_count":0,"req_id":"202005062227140100260601540A3178C9","rid":"202005062227140100260601540A3178C9","share_count":0,"share_info":null,"show_dislike":false,"show_portrait":false,"show_portrait_article":false,"small_image":null,"tip":0,"ugc_recommend":{"activity":"","reason":""},"user_repin":0,"user_verified":0,"verified_content":"","video_style":0}',
		'code': ''
	}, {
		'content': '{"abstract":"","allow_download":false,"article_sub_type":0,"article_type":0,"article_url":"","ban_comment":0,"ban_immersive":0,"behot_time":1588775234,"bury_count":0,"bury_style_show":1,"cell_ctrls":{"cell_flag":0,"cell_layout_style":1,"cell_height":0,"content_decoration":null,"need_client_impr_recycle":1},"cell_type":202,"comment_count":0,"content_decoration":"","cursor":1588775234000,"data_type":1,"digg_count":0,"has_m3u8_video":false,"has_mp4_video":0,"has_video":false,"hot":0,"id":6623262922753704206,"ignore_web_transform":0,"interaction_data":"","is_subject":false,"item_version":0,"level":0,"log_pb":{"author_id":"5857262808","impr_id":"202005062227140100260601540A3178C9","is_following":"0"},"raw_data":{"content":{"answer":{"abstract_text":"刚在《毒液》里看见客串的老爷子，转眼间英雄已逝，一个时代结束了。\u3000\u3000投资界（微信ID：pedaily2012）11月13日消息，据外媒报道，美国漫画界元老级人物斯坦·李于当地时间周一（12日）在好莱坞一家医疗中心去世，享年95岁。\u3000\u3000斯坦·李的个人官方推特发布其去世消息\u3000\u3000漫威影业主席凯文·费吉悼念：“对我的职业生涯和我们在漫威影业所做的一切影响最大的人，就是斯坦·李了。”\u3000\u3000DC官推悼念斯坦·李：“他改变了我们看英雄的方式，现代漫画将一直有他不可磨灭的印记，他那感染人心的热情，让我们想起自己爱上这些故事的初心。”\u3000\u3000这个超级英雄应该是去拯救宇宙了。\u3000\u3000拯救宇宙的漫威之父\u3000\u3000可以说，没有斯坦·李就没有现在漫威的成功。\u3000\u3000正因斯坦·李的天才创业和不懈努力，才创造了媲美星球大战的漫威宇宙；也是因为他创作出神奇四侠，才让漫威在白银时代能与DC的超人气“闪电侠”相抗衡，成为齐名的漫画巨头；更是因为美国队长、钢铁侠、蜘蛛侠、雷神、绿巨人、金刚狼等的存在，才会有我们幼年伟大的英雄梦想。\u3000\u3000斯坦·李原名斯坦利·马丁·利博，1922年12月28日出生在纽约。斯坦·李从小就喜欢阅读神秘小说和冒险故事，热爱写作。为了补贴家用，小斯坦利到处找活干。他曾给报纸长期写过讣闻，帮美国国家结核病中心写过新闻通稿，帮餐馆送过三明治外卖，做过制裤公司的杂工，做过百老汇大戏院的引座员，还做过《纽约先驱论坛报》的订报员。\u3000\u30001939年，16岁的斯坦利从高中毕业。在舅舅的介绍下，斯坦利跟当时的通俗杂志和漫画书出版商马丁·古德曼见了一面。古德曼同意让斯坦利到自己的Timely漫画公司做助理，周薪是8美元。而Timely就是漫威的前身。\u3000\u30001941年，是漫威史上的重要转折点。这一年，漫威漫画的编辑部作出了创作一部“涵盖爱国主义精神”的漫画，用以契合当时正在白热化开展的第二次世界大战的宏观背景，而这便是后来家喻户晓的《美国队长》。\u3000\u3000同年，斯坦利生平第一部作品问世，即《美国队长》系列漫画的第三部，影响了漫威漫画此后半个世纪发展。1961年11月，《神奇四侠》诞生，斯坦·李在漫画界成为焦点。\u3000\u3000后来在搭档漫画家杰克·科比的协助下，创作了《蜘蛛侠》、《钢铁侠》、《雷神托尔》、《绿巨人》、《X战警》、《奇异博士》等漫画角色，并开创了专属于斯坦·李的“神奇模式”。\u3000\u3000斯坦·李的每一部漫画、每一部电影都向我们展现了无与伦比的想象力与庞大的世界观。在他的笔下，公司一步步走向神坛，是毫无争议的漫威之父。\u3000\u30001996 年，阿维·阿拉德开始领导漫威，成立漫威影业。1998 年斯坦·李参与编剧，漫威和新线电影共同制作的《刀锋战士》大获成功。\u3000\u3000也在同年，斯坦·李离开了漫威，成立了“斯坦·李传媒”公司。但因经营不善，2001 年初就倒闭了。2002年，他与人合作创办了POW！娱乐，这家公司2017年5月，被被中国综合型文化产业集团承兴国际集团收购。\u3000\u3000除了创作漫画，斯坦·李也很喜欢“演”。他在世时曾表示，“我骄傲的是，也许我做的一些事情能娱乐到他人。”他也确实做到了，他相继客串出演了《蜘蛛侠》、《X战警》、《神奇四侠》、《钢铁侠》、《美国队长》《雷神托尔》、《无敌浩克》、《复仇者联盟》、《超凡蜘蛛侠》等电影，借客串的演员身份获得“美国全角色历史最高票房演员”。也成了漫威迷们看电影时最大的彩蛋。\u3000\u3000蜘蛛人是斯坦·李最钟爱的形象。不似外太空的超级物种，蜘蛛侠是一个有关成长的漫画在获得超人能力的同时，还要面对学业、生活、女朋友、家庭、人际关系等问题。斯坦·李在接受美国媒体采访时说，“我的所有超级英雄都有人的缺点，我努力表现他们尽管有超人的力量，但他们的生活并不完美。”\u3000\u3000几十年来，斯坦·李几乎每周都同时创作两本漫画，最多时达5本，作品占漫威总量的90%以上。在2002年出版的传记中，他写道：“如果我可以完全真诚地袒露心迹，那么我可以说我就是自己最大的粉丝。”\u3000\u3000打造超级英雄IP，漫威的从0到1\u3000\u3000令人艳羡的漫威英雄IP的打造并不是一开始就是成功的。它在中国也走了一段从0到1的过程。\u3000\u3000最开始，由于受众基础薄弱，英雄IP的受众并不广泛，连续数部电影票房、口碑表现都不理想。比如最开始推出的《无敌浩克》、《钢铁侠2》、《美国队长》、《雷神》中，除已经有一定知名度的《钢铁侠2》取得了1.75亿票房外，其余几部电影票房均未过亿，按照汇率来看甚至不到北美票房的十分之一。整体的市场表现全看档期选择和运气。\u3000\u3000但漫威很聪明，它知道一根火柴的力量渺小，但一盒火柴的力量将能点燃各个受众的心。所以经过了整整十年的布局，以三部《复仇者联盟》为节点，漫威正式走上了“占领心智、发家致富”的道路。\u3000\u3000通过前期的铺路，加深观众对英雄的了解，漫威于是2012年打响了团战的第一炮《复联》。它将英雄基于一战，一起点燃各个英雄粉丝的热情。而《复联1》也在中国实现了爆发式表现，首日6600万的成绩单，两天狂收1.14亿人民币，轻松创下超级英雄电影在华的首映新纪录。而影片在三四线城市的活跃度提升到了40%左右。\u3000\u3000也就是从这一次抱团出战开始，漫威电影的票房权重一路上扬，平均达到15%以上。而单个作品的票房也都保持在了5亿以上。\u3000\u3000（图片来源于网络）\u3000\u3000当然，这只是漫威的第一步，之后《复仇者联盟2》成功斩获14.22亿元，成为内地史上首部在收获10亿+的漫威电影。\u3000\u3000中国市场的良好表现，让漫威受宠若惊。\u3000\u3000其实，从2008年到2018年，经历了90后从学生时代步入到社会工作的过程，而漫威的英雄更加具有陪伴意义。更重要的是，在漫威发展的过程中，中国内地电影市场也在不断向前。2012年—2015年，内地票房的年增速都在30%左右，2015年更是达到了夸张的49%，大量观众开始走进影院，许多进口片都因此而收获了不错的成绩。\u3000\u3000斯坦.李曾表示：中国将成为世界的影视中心，这个世界人口最多的国家需要有自己的超级英雄。就在2017年，漫威就宣布将和网易合作，首创中国的超级英雄：气旋和林烈。在将来这些“中国化”的本土英雄很可能与钢铁侠等初代超级英雄并肩作战。\u3000\u3000据官方宣布，2020年正式推出全沉浸式超级英雄主题公园，新增的三个漫威主题园区分别位于美国加利福尼亚州、法国巴黎以及中国香港。\u3000\u300010年超160亿美元票房的漫威宇宙\u3000\u3000漫威漫画公司创建于1939年，当年10月，第一本漫画推向市场，同时创造了它第一个超级英雄海王纳摩。1941年3月推出的美国队长再次引起轰动，第一次出场，就卖出了100万册的漫画。此后，漫威又陆续推出了绿巨人、蜘蛛侠、雷神、钢铁侠等超级英雄。\u3000\u3000漫威的命运也像它的英雄们一样跌宕起伏，经历了二战等一系列事故，漫威被多次转手：1986 年，漫威被母公司Cadence Industries卖给了New World Pictures；3年后，又被卖给了MacAndrews \\u0026 Forbes Holdings1994年，Andrews Grou和ME又将漫威改组成为漫威控股公司；1996 年，漫威被卷入Carl Icahn和Perelman间的权力斗争。当年12月27 日，漫威正式宣布破产，之后又在多方帮助下，脱离了破产的窘境。\u3000\u3000漫画行业整体衰败，漫威陷入了财政危机。为了渡过难关，漫威决定出售超级英雄的电影拍摄权。1999年，漫威700万美元把《蜘蛛侠》电影版版权卖给了索尼。后者通过《蜘蛛侠》前两部电影大赚16亿美元，但只有7500万属于漫威。\u3000\u30002005年，对分成不满的漫威成立了影业公司。随后从美林银行贷款2.25亿美元投资了《钢铁侠》，背水一战。豪赌成功了，《钢铁侠》全球取得5.85亿美元票房，帮助漫威摆脱窘境。3部《钢铁侠》电影下来全球总票房高达23.8亿美元，3部电影的DVD总共卖出了1700多万份，赚了3亿美元，成为全球最赚钱的系列电影之一。\u3000\u30002009 年，迪士尼以42.4亿美元现金加股票的价格，收购漫威娱乐。2013年起，在迪士尼的主导下，漫威逐渐开始收回散落各处的超级英雄电影版权。漫威成了迪士尼的一部赚钱机器：电影、动画、玩具、游戏、乐园在一条产业链不断衍生发展。\u3000\u3000凭借《X战警》、《蜘蛛侠》横扫美国票房后，漫威开始了自制超级英雄大片的道路，推出了漫威电影宇宙（Marvel Cinematic Universe）计划。自2008年起，一整套清晰完整的电影计划浮出水面，钢铁侠、雷神、美国队长，金刚狼……一个又一个的超级英雄陆续走上银幕，既能孤胆英雄拯救世界，又能合体打怪兽，随后通过《复仇者联盟》将他们集结起来。\u3000\u3000第一阶段，漫威凭借6部影片，以总计10亿美元的成本取得了37.4亿美元的全球票房。第二阶段仅《X战警》就带来了近40亿美元的回报，第三阶段也已进入了筹备拍摄阶段。\u3000\u300078年来，漫威不断推出、贩卖虚拟世界里的英雄。队伍人员日渐壮大，超级英雄的生意也越做越大。大荧幕上超级英雄层出不穷，漫威也没有放过小屏幕。先后推出《神盾局特工》和《卡特特工》两部美剧，剧情紧扣大电影，神盾局为大电影穿针引线，电影、电视剧环环相扣，共同打造出气势恢宏、场面磅礴的漫威帝国。从漫画到电影、电视剧，从游戏到衍生品。\u3000\u3000作为打造超级IP的帝国，漫威做了非常好的榜样。漫威电影宇宙目前全球总票房早已超过了160亿美元，按日前汇率计算折合人民币超1100亿元。\u3000\u3000自大的托尼、正义的美队、嘴炮蜘蛛侠、聪明的班纳、邪魅的洛基、豪爽的雷神、感性的星爵、绯红女巫、无敌的浩克、理性的奇异博士、天真的格鲁特、帅气酷炫的黑豹、战争机器、猎鹰、性感的黑寡妇……“我们爱每一个超级英雄。”\u3000\u3000结语\u3000\u3000英雄们如期赴约，一次次点燃粉丝们内心的激情。从学生到职场，从青年到父母，这些英雄早已不是一个个IP那么简单。\u3000\u3000但如今，江湖失去了金庸大师，漫威世界憾别斯坦·李。从来都是偶像易有，大英雄百年难得。新旧更迭，超级英雄陪着我们逐渐老去，深深的目光中，都有自己年幼的身影。\u3000\u3000美国队长扮演者克里斯·埃文斯悼念：“不会再有另一个斯坦·李了。”","ansid":"6623262922753704206","answer_detail_schema":"sslocal://wenda_detail?ansid=6623262922753704206\\u0026answer_type=0\\u0026api_param=%7B%22answer_list%22%3A%5B6623262922753704206%5D%2C%22answer_type%22%3A%22combine_answer%22%2C%22enter_ansid%22%3A%226623262922753704206%22%2C%22enter_from%22%3A%22click_pgc%22%2C%22from%22%3A%22outer%22%2C%22has_more%22%3Atrue%2C%22in_offset%22%3A0%2C%22next_offset%22%3A1%2C%22origin_from%22%3A%22click_pgc%22%7D\\u0026gd_ext_json=%7B%22enter_from%22%3A%22click_pgc%22%2C%22ansid%22%3A%226623262922753704206%22%2C%22enterfrom_answerid%22%3A%226623262922753704206%22%2C%22parent_enterfrom%22%3A%22%22%2C%22qid%22%3A%226623128142624063758%22%2C%22category_name%22%3A%22profile_wenda%22%2C%22author_id%22%3A%225857262808%22%2C%22article_type%22%3A%22wenda%22%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202005062227140100260601540A3178C9%22%7D%2C%22from_gid%22%3A%22%22%2C%22with_avatar%22%3A%220%22%7D\\u0026video_type=0","answer_list_schema":"","answer_type":0,"brow_count":2949,"comment_count":0,"comment_schema":"sslocal://wenda_detail?ansid=6623262922753704206\\u0026answer_type=0\\u0026api_param=%7B%22answer_list%22%3A%5B6623262922753704206%5D%2C%22answer_type%22%3A%22combine_answer%22%2C%22enter_ansid%22%3A%226623262922753704206%22%2C%22enter_from%22%3A%22click_pgc%22%2C%22from%22%3A%22outer%22%2C%22has_more%22%3Atrue%2C%22in_offset%22%3A0%2C%22next_offset%22%3A1%2C%22origin_from%22%3A%22click_pgc%22%7D\\u0026gd_ext_json=%7B%22enter_from%22%3A%22click_pgc%22%2C%22ansid%22%3A%226623262922753704206%22%2C%22enterfrom_answerid%22%3A%226623262922753704206%22%2C%22parent_enterfrom%22%3A%22%22%2C%22qid%22%3A%226623128142624063758%22%2C%22category_name%22%3A%22profile_wenda%22%2C%22author_id%22%3A%225857262808%22%2C%22article_type%22%3A%22wenda%22%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202005062227140100260601540A3178C9%22%7D%2C%22from_gid%22%3A%22%22%2C%22with_avatar%22%3A%220%22%7D\\u0026is_jump_comment=1\\u0026show_write_comment_dialog=1\\u0026video_type=0","content_abstract":{"large_image_list":[{"height":416,"type":1,"uri":"da770006d2825d35fed7","url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~960x0.image?from=wenda","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~960x0.image?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~960x0.image?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~960x0.image?from=wenda"}],"width":539},{"height":604,"type":1,"uri":"113ee000048f91e9d6387","url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~960x0.image?from=wenda","url_list":[{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~960x0.image?from=wenda"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~960x0.image?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~960x0.image?from=wenda"}],"width":500}],"origin_image_list":[{"height":416,"type":1,"uri":"da770006d2825d35fed7","url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~0x0.image?from=wenda","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~0x0.image?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~0x0.image?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~0x0.image?from=wenda"}],"width":539},{"height":604,"type":1,"uri":"113ee000048f91e9d6387","url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~0x0.image?from=wenda","url_list":[{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~0x0.image?from=wenda"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~0x0.image?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~0x0.image?from=wenda"}],"width":500}],"text":"刚在《毒液》里看见客串的老爷子，转眼间英雄已逝，一个时代结束了。\\n\u3000\u3000投资界（微信ID：pedaily2012）11月13日消息，据外媒报道，美国漫画界元老级人物斯坦·李于当地时间周一（12日）在好莱坞一家医疗中心去世，享年95岁。\\n\u3000\u3000斯坦·李的个人官方推特发布其去世消息\\n\u3000\u3000漫威影业主席凯文·费吉悼念：“对我的职业生涯和我们在漫威影业所做的一切影响最大的人，就是斯坦·李了。”\\n\u3000\u3000DC官推悼念斯坦·李：“他改变了我们看英雄的方式，现代漫画将一直有他不可磨灭的印记，他那感染人心的热情，让我们想起自己爱上这些故事的初心。”\\n\u3000\u3000这个超级英雄应该是去拯救宇宙了。\\n\u3000\u3000拯救宇宙的漫威之父\\n\u3000\u3000可以说，没有斯坦·李就没有现在漫威的成功。\\n\u3000\u3000正因斯坦·李的天才创业和不懈努力，才创造了媲美星球大战的漫威宇宙；也是因为他创作出神奇四侠，才让漫威在白银时代能与DC的超人气“闪电侠”相抗衡，成为齐名的漫画巨头；更是因为美国队长、钢铁侠、蜘蛛侠、雷神、绿巨人、金刚狼等的存在，才会有我们幼年伟大的英雄梦想。\\n\u3000\u3000斯坦·李原名斯坦利·马丁·利博，1922年12月28日出生在纽约。斯坦·李从小就喜欢阅读神秘小说和冒险故事，热爱写作。为了补贴家用，小斯坦利到处找活干。他曾给报纸长期写过讣闻，帮美国国家结核病中心写过新闻通稿，帮餐馆送过三明治外卖，做过制裤公司的杂工，做过百老汇大戏院的引座员，还做过《纽约先驱论坛报》的订报员。\\n\u3000\u30001939年，16岁的斯坦利从高中毕业。在舅舅的介绍下，斯坦利跟当时的通俗杂志和漫画书出版商马丁·古德曼见了一面。古德曼同意让斯坦利到自己的Timely漫画公司做助理，周薪是8美元。而Timely就是漫威的前身。\\n\u3000\u30001941年，是漫威史上的重要转折点。这一年，漫威漫画的编辑部作出了创作一部“涵盖爱国主义精神”的漫画，用以契合当时正在白热化开展的第二次世界大战的宏观背景，而这便是后来家喻户晓的《美国队长》。\\n\u3000\u3000同年，斯坦利生平第一部作品问世，即《美国队长》系列漫画的第三部，影响了漫威漫画此后半个世纪发展。1961年11月，《神奇四侠》诞生，斯坦·李在漫画界成为焦点。\\n\u3000\u3000后来在搭档漫画家杰克·科比的协助下，创作了《蜘蛛侠》、《钢铁侠》、《雷神托尔》、《绿巨人》、《X战警》、《奇异博士》等漫画角色，并开创了专属于斯坦·李的“神奇模式”。\\n\u3000\u3000斯坦·李的每一部漫画、每一部电影都向我们展现了无与伦比的想象力与庞大的世界观。在他的笔下，公司一步步走向神坛，是毫无争议的漫威之父。\\n\u3000\u30001996 年，阿维·阿拉德开始领导漫威，成立漫威影业。1998 年斯坦·李参与编剧，漫威和新线电影共同制作的《刀锋战士》大获成功。\\n\u3000\u3000也在同年，斯坦·李离开了漫威，成立了“斯坦·李传媒”公司。但因经营不善，2001 年初就倒闭了。2002年，他与人合作创办了POW！娱乐，这家公司2017年5月，被被中国综合型文化产业集团承兴国际集团收购。\\n\u3000\u3000除了创作漫画，斯坦·李也很喜欢“演”。他在世时曾表示，“我骄傲的是，也许我做的一些事情能娱乐到他人。”他也确实做到了，他相继客串出演了《蜘蛛侠》、《X战警》、《神奇四侠》、《钢铁侠》、《美国队长》《雷神托尔》、《无敌浩克》、《复仇者联盟》、《超凡蜘蛛侠》等电影，借客串的演员身份获得“美国全角色历史最高票房演员”。也成了漫威迷们看电影时最大的彩蛋。\\n\u3000\u3000蜘蛛人是斯坦·李最钟爱的形象。不似外太空的超级物种，蜘蛛侠是一个有关成长的漫画在获得超人能力的同时，还要面对学业、生活、女朋友、家庭、人际关系等问题。斯坦·李在接受美国媒体采访时说，“我的所有超级英雄都有人的缺点，我努力表现他们尽管有超人的力量，但他们的生活并不完美。”\\n\u3000\u3000几十年来，斯坦·李几乎每周都同时创作两本漫画，最多时达5本，作品占漫威总量的90%以上。在2002年出版的传记中，他写道：“如果我可以完全真诚地袒露心迹，那么我可以说我就是自己最大的粉丝。”\\n\u3000\u3000打造超级英雄IP，漫威的从0到1\\n\u3000\u3000令人艳羡的漫威英雄IP的打造并不是一开始就是成功的。它在中国也走了一段从0到1的过程。\\n\u3000\u3000最开始，由于受众基础薄弱，英雄IP的受众并不广泛，连续数部电影票房、口碑表现都不理想。比如最开始推出的《无敌浩克》、《钢铁侠2》、《美国队长》、《雷神》中，除已经有一定知名度的《钢铁侠2》取得了1.75亿票房外，其余几部电影票房均未过亿，按照汇率来看甚至不到北美票房的十分之一。整体的市场表现全看档期选择和运气。\\n\u3000\u3000但漫威很聪明，它知道一根火柴的力量渺小，但一盒火柴的力量将能点燃各个受众的心。所以经过了整整十年的布局，以三部《复仇者联盟》为节点，漫威正式走上了“占领心智、发家致富”的道路。\\n\u3000\u3000通过前期的铺路，加深观众对英雄的了解，漫威于是2012年打响了团战的第一炮《复联》。它将英雄基于一战，一起点燃各个英雄粉丝的热情。而《复联1》也在中国实现了爆发式表现，首日6600万的成绩单，两天狂收1.14亿人民币，轻松创下超级英雄电影在华的首映新纪录。而影片在三四线城市的活跃度提升到了40%左右。\\n\u3000\u3000也就是从这一次抱团出战开始，漫威电影的票房权重一路上扬，平均达到15%以上。而单个作品的票房也都保持在了5亿以上。\\n\u3000\u3000（图片来源于网络）\\n\u3000\u3000当然，这只是漫威的第一步，之后《复仇者联盟2》成功斩获14.22亿元，成为内地史上首部在收获10亿+的漫威电影。\\n\u3000\u3000中国市场的良好表现，让漫威受宠若惊。\\n\u3000\u3000其实，从2008年到2018年，经历了90后从学生时代步入到社会工作的过程，而漫威的英雄更加具有陪伴意义。更重要的是，在漫威发展的过程中，中国内地电影市场也在不断向前。2012年—2015年，内地票房的年增速都在30%左右，2015年更是达到了夸张的49%，大量观众开始走进影院，许多进口片都因此而收获了不错的成绩。\\n\u3000\u3000斯坦.李曾表示：中国将成为世界的影视中心，这个世界人口最多的国家需要有自己的超级英雄。就在2017年，漫威就宣布将和网易合作，首创中国的超级英雄：气旋和林烈。在将来这些“中国化”的本土英雄很可能与钢铁侠等初代超级英雄并肩作战。\\n\u3000\u3000据官方宣布，2020年正式推出全沉浸式超级英雄主题公园，新增的三个漫威主题园区分别位于美国加利福尼亚州、法国巴黎以及中国香港。\\n\u3000\u300010年超160亿美元票房的漫威宇宙\\n\u3000\u3000漫威漫画公司创建于1939年，当年10月，第一本漫画推向市场，同时创造了它第一个超级英雄海王纳摩。1941年3月推出的美国队长再次引起轰动，第一次出场，就卖出了100万册的漫画。此后，漫威又陆续推出了绿巨人、蜘蛛侠、雷神、钢铁侠等超级英雄。\\n\u3000\u3000漫威的命运也像它的英雄们一样跌宕起伏，经历了二战等一系列事故，漫威被多次转手：1986 年，漫威被母公司Cadence Industries卖给了New World Pictures；3年后，又被卖给了MacAndrews \\u0026 Forbes Holdings1994年，Andrews Grou和ME又将漫威改组成为漫威控股公司；1996 年，漫威被卷入Carl Icahn和Perelman间的权力斗争。当年12月27 日，漫威正式宣布破产，之后又在多方帮助下，脱离了破产的窘境。\\n\u3000\u3000漫画行业整体衰败，漫威陷入了财政危机。为了渡过难关，漫威决定出售超级英雄的电影拍摄权。1999年，漫威700万美元把《蜘蛛侠》电影版版权卖给了索尼。后者通过《蜘蛛侠》前两部电影大赚16亿美元，但只有7500万属于漫威。\\n\u3000\u30002005年，对分成不满的漫威成立了影业公司。随后从美林银行贷款2.25亿美元投资了《钢铁侠》，背水一战。豪赌成功了，《钢铁侠》全球取得5.85亿美元票房，帮助漫威摆脱窘境。3部《钢铁侠》电影下来全球总票房高达23.8亿美元，3部电影的DVD总共卖出了1700多万份，赚了3亿美元，成为全球最赚钱的系列电影之一。\\n\u3000\u30002009 年，迪士尼以42.4亿美元现金加股票的价格，收购漫威娱乐。2013年起，在迪士尼的主导下，漫威逐渐开始收回散落各处的超级英雄电影版权。漫威成了迪士尼的一部赚钱机器：电影、动画、玩具、游戏、乐园在一条产业链不断衍生发展。\\n\u3000\u3000凭借《X战警》、《蜘蛛侠》横扫美国票房后，漫威开始了自制超级英雄大片的道路，推出了漫威电影宇宙（Marvel Cinematic Universe）计划。自2008年起，一整套清晰完整的电影计划浮出水面，钢铁侠、雷神、美国队长，金刚狼……一个又一个的超级英雄陆续走上银幕，既能孤胆英雄拯救世界，又能合体打怪兽，随后通过《复仇者联盟》将他们集结起来。\\n\u3000\u3000第一阶段，漫威凭借6部影片，以总计10亿美元的成本取得了37.4亿美元的全球票房。第二阶段仅《X战警》就带来了近40亿美元的回报，第三阶段也已进入了筹备拍摄阶段。\\n\u3000\u300078年来，漫威不断推出、贩卖虚拟世界里的英雄。队伍人员日渐壮大，超级英雄的生意也越做越大。大荧幕上超级英雄层出不穷，漫威也没有放过小屏幕。先后推出《神盾局特工》和《卡特特工》两部美剧，剧情紧扣大电影，神盾局为大电影穿针引线，电影、电视剧环环相扣，共同打造出气势恢宏、场面磅礴的漫威帝国。从漫画到电影、电视剧，从游戏到衍生品。\\n\u3000\u3000作为打造超级IP的帝国，漫威做了非常好的榜样。漫威电影宇宙目前全球总票房早已超过了160亿美元，按日前汇率计算折合人民币超1100亿元。\\n\u3000\u3000自大的托尼、正义的美队、嘴炮蜘蛛侠、聪明的班纳、邪魅的洛基、豪爽的雷神、感性的星爵、绯红女巫、无敌的浩克、理性的奇异博士、天真的格鲁特、帅气酷炫的黑豹、战争机器、猎鹰、性感的黑寡妇……“我们爱每一个超级英雄。”\\n\u3000\u3000结语\\n\u3000\u3000英雄们如期赴约，一次次点燃粉丝们内心的激情。从学生到职场，从青年到父母，这些英雄早已不是一个个IP那么简单。\\n\u3000\u3000但如今，江湖失去了金庸大师，漫威世界憾别斯坦·李。从来都是偶像易有，大英雄百年难得。新旧更迭，超级英雄陪着我们逐渐老去，深深的目光中，都有自己年幼的身影。\\n\u3000\u3000美国队长扮演者克里斯·埃文斯悼念：“不会再有另一个斯坦·李了。”","thumb_image_list":[{"height":415,"type":1,"uri":"da770006d2825d35fed7","url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~539x415_cs.jpeg?from=wenda","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~539x415_cs.jpeg?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~539x415_cs.jpeg?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~539x415_cs.jpeg?from=wenda"}],"width":539},{"height":533,"type":1,"uri":"113ee000048f91e9d6387","url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~500x533_cs.jpeg?from=wenda","url_list":[{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~500x533_cs.jpeg?from=wenda"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~500x533_cs.jpeg?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~500x533_cs.jpeg?from=wenda"}],"width":500}],"video_list":[],"wenda_cv_image_list":null},"create_time":1542098569,"digg_count":6,"display_count":0,"forward_count":0,"interactive_data":{"comment_list":[],"digg_user_list":null,"style_ctrls":{"ban_comment":0,"ban_face":0,"ban_pic_comment":0,"comment_entrance":0,"comment_show_more_schema":"","comment_show_more_text":"","digg_show_more_schema":"","digg_show_more_text":"","max_comment_line":4,"max_digg_line":2,"show_repost_entrance":0,"style_type":3}},"is_digg":0,"large_image_list":[{"height":416,"type":1,"uri":"da770006d2825d35fed7","url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~960x0.jpeg?from=wenda","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~960x0.jpeg?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~960x0.jpeg?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~960x0.jpeg?from=wenda"}],"width":539},{"height":604,"type":1,"uri":"113ee000048f91e9d6387","url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~960x0.jpeg?from=wenda","url_list":[{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~960x0.jpeg?from=wenda"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~960x0.jpeg?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~960x0.jpeg?from=wenda"}],"width":500}],"max_lines":20,"origin_image_list":[{"height":416,"type":1,"uri":"da770006d2825d35fed7","url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~0x0.jpeg?from=wenda","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~0x0.jpeg?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~0x0.jpeg?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~0x0.jpeg?from=wenda"}],"width":539},{"height":604,"type":1,"uri":"113ee000048f91e9d6387","url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~0x0.jpeg?from=wenda","url_list":[{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~0x0.jpeg?from=wenda"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~0x0.jpeg?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~0x0.jpeg?from=wenda"}],"width":500}],"perm":{"can_ban_comment":0,"can_comment_answer":1,"can_delete_answer":0,"can_delete_comment":0,"can_digg_answer":1,"can_edit_answer":0,"can_post_answer":1,"delete_answer_tips":"","edit_answer_tips":"","show_delete_answer":0,"show_edit_answer":0},"read_count":0,"show_count":2949,"show_lines":8,"show_text":"阅读","status":0,"thumb_image_list":[{"height":415,"type":1,"uri":"da770006d2825d35fed7","url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~539x415_cs.jpeg?from=wenda","url_list":[{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~539x415_cs.jpeg?from=wenda"},{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~539x415_cs.jpeg?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/da770006d2825d35fed7~539x415_cs.jpeg?from=wenda"}],"width":539},{"height":533,"type":1,"uri":"113ee000048f91e9d6387","url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~500x533_cs.jpeg?from=wenda","url_list":[{"url":"http://sf3-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~500x533_cs.jpeg?from=wenda"},{"url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~500x533_cs.jpeg?from=wenda"},{"url":"http://sf6-ttcdn-tos.pstatp.com/img/mosaic-legacy/113ee000048f91e9d6387~500x533_cs.jpeg?from=wenda"}],"width":500}],"video_type":"0"},"cell_layout_style":0,"comment_schema":"sslocal://wenda_detail?ansid=6623262922753704206\\u0026answer_type=0\\u0026api_param=%7B%22answer_list%22%3A%5B6623262922753704206%5D%2C%22answer_type%22%3A%22combine_answer%22%2C%22enter_ansid%22%3A%226623262922753704206%22%2C%22enter_from%22%3A%22click_pgc%22%2C%22from%22%3A%22outer%22%2C%22has_more%22%3Atrue%2C%22in_offset%22%3A0%2C%22next_offset%22%3A1%2C%22origin_from%22%3A%22click_pgc%22%7D\\u0026gd_ext_json=%7B%22enter_from%22%3A%22click_pgc%22%2C%22ansid%22%3A%226623262922753704206%22%2C%22enterfrom_answerid%22%3A%226623262922753704206%22%2C%22parent_enterfrom%22%3A%22%22%2C%22qid%22%3A%226623128142624063758%22%2C%22category_name%22%3A%22profile_wenda%22%2C%22author_id%22%3A%225857262808%22%2C%22article_type%22%3A%22wenda%22%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202005062227140100260601540A3178C9%22%7D%2C%22from_gid%22%3A%22%22%2C%22with_avatar%22%3A%220%22%7D\\u0026is_jump_comment=1\\u0026show_write_comment_dialog=1\\u0026video_type=0","default_lines":3,"filter_words":[{"id":"8:0","is_selected":false,"name":"看过了"},{"id":"9:1","is_selected":false,"name":"内容太水"},{"id":"5:6623262922753704206","is_selected":false,"name":"拉黑作者:投资界"}],"hide_create_time":0,"image_type":0,"jump_type":1,"layout_type":1,"max_lines":6,"question":{"answer_count_description":"22人回答了问题","answer_user_list":[{"avatar_url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/11340/6310107700~120x256.image","is_following":0,"is_verify":0,"uname":"投资界","user_auth_info":"","user_id":"5857262808","user_schema":"","v_icon":""},{"avatar_url":"http://p0.pstatp.com/origin/3791/5035712059","is_following":0,"is_verify":0,"uname":"","user_auth_info":"","user_id":"","user_schema":"","v_icon":""},{"avatar_url":"http://p0.pstatp.com/origin/3791/5035712059","is_following":0,"is_verify":0,"uname":"","user_auth_info":"","user_id":"","user_schema":"","v_icon":""}],"concern_tag_list":[{"concern_id":"6213176851934743042","name":"斯坦·李","schema":"sslocal://concern?api_param=%7B%22wenda_api_param%22%3A%7B%7D%7D\\u0026cid=6213176851934743042\\u0026tab_sname=wenda"},{"concern_id":"6213178576385083905","name":"漫威漫画","schema":"sslocal://concern?api_param=%7B%22wenda_api_param%22%3A%7B%7D%7D\\u0026cid=6213178576385083905\\u0026tab_sname=wenda"},{"concern_id":"6213187413263518209","name":"影视","schema":"sslocal://concern?api_param=%7B%22wenda_api_param%22%3A%7B%7D%7D\\u0026cid=6213187413263518209\\u0026tab_sname=wenda"},{"concern_id":"6215497896830175745","name":"娱乐","schema":"sslocal://concern?api_param=%7B%22wenda_api_param%22%3A%7B%7D%7D\\u0026cid=6215497896830175745\\u0026tab_sname=wenda"}],"content":{"content_rich_span":"{\\"links\\":[]}","large_image_list":[{"height":364,"type":1,"uri":"","url":"http://p3.pstatp.com/thumb/2c650017572758251817","url_list":[{"url":"http://p3.pstatp.com/thumb/2c650017572758251817"}],"width":360}],"origin_image_list":[{"height":364,"type":1,"uri":"","url":"http://p3.pstatp.com/thumb/2c650017572758251817","url_list":[{"url":"http://p3.pstatp.com/thumb/2c650017572758251817"}],"width":360}],"quest_large_image_list":[],"quest_origin_image_list":[],"quest_thumb_image_list":[],"rich_text":"当地时间2018年11月12日，美国洛杉矶，民众在好莱坞“星光大道”上向斯坦·李之星献花悼念。据美媒报道，有“漫威之父”之称的美国漫画界元老级人物斯坦·李于当地时间12日在好莱坞一家医疗中心去世，享年95岁。其代表作品有《蜘蛛侠》《黑豹》《绿巨人》《X战警》《钢铁侠》等。","text":"当地时间2018年11月12日，美国洛杉矶，民众在好莱坞“星光大道”上向斯坦·李之星献花悼念。据美媒报道，有“漫威之父”之称的美国漫画界元老级人物斯坦·李于当地时间12日在好莱坞一家医疗中心去世，享年95岁。其代表作品有《蜘蛛侠》《黑豹》《绿巨人》《X战警》《钢铁侠》等。","thumb_image_list":[{"height":364,"type":1,"uri":"","url":"http://p3.pstatp.com/thumb/2c650017572758251817","url_list":[{"url":"http://p3.pstatp.com/thumb/2c650017572758251817"}],"width":360}]},"count_statistics":[{"count_name":"收藏量","count_num":"4","count_type":1}],"create_time":1542067188,"follow_count":0,"is_anonymous":0,"is_question_delete":0,"main_question_info":"","nice_ans_count":17,"normal_ans_count":5,"qid":"6623128142624063758","question_list_schema":"sslocal://wenda_list?api_param=%7B%22enter_ansid%22%3A%226623262922753704206%22%2C%22enter_from%22%3A%22click_pgc%22%2C%22no_enter_ansid%22%3A%22%22%2C%22origin_from%22%3A%22click_pgc%22%7D\\u0026gd_ext_json=%7B%22enter_from%22%3A%22click_pgc%22%2C%22ansid%22%3A%226623262922753704206%22%2C%22enterfrom_answerid%22%3A%226623262922753704206%22%2C%22parent_enterfrom%22%3A%22%22%2C%22qid%22%3A%226623128142624063758%22%2C%22category_name%22%3A%22profile_wenda%22%2C%22author_id%22%3A%225857262808%22%2C%22article_type%22%3A%22wenda%22%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202005062227140100260601540A3178C9%22%7D%2C%22from_gid%22%3A%22%22%2C%22with_avatar%22%3A%220%22%7D\\u0026qTitle=%E2%80%9C%E6%BC%AB%E5%A8%81%E4%B9%8B%E7%88%B6%E2%80%9D%E6%96%AF%E5%9D%A6%C2%B7%E6%9D%8E%E5%8E%BB%E4%B8%96%EF%BC%8C%E4%BD%A0%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%EF%BC%9F\\u0026qid=6623128142624063758","repost_params":{"cover_url":"http://p3.pstatp.com/origin/18a300102cab5d8d0e05","fw_id":6623128142624063758,"fw_id_type":1026,"fw_user_id":59712475271,"opt_id":6623128142624063758,"opt_id_type":1026,"repost_type":218,"schema":"","title":"“漫威之父”斯坦·李去世，你如何评价？"},"status":0,"tips":{"tips_button_text":"","tips_schema":"","tips_text":"","tips_type":0},"title":"“漫威之父”斯坦·李去世，你如何评价？","user":{"avatar_url":"http://p1.pstatp.com/thumb/53f300048a633f490668","is_following":0,"is_verify":1,"uname":"鉴动漫","user_auth_info":"{\\"auth_type\\":\\"0\\",\\"auth_info\\":\\"优质动漫领域创作者\\",\\"other_auth\\":{\\"interest\\":\\"优质动漫领域创作者\\"}}","user_id":"59712475271","user_intro":"优质动漫领域创作者","user_schema":"sslocal://profile?api_param=%7B%22enter_from%22%3A%22click_pgc%22%2C%22origin_from%22%3A%22click_pgc%22%7D\\u0026gd_ext_json=%7B%22enter_from%22%3A%22click_pgc%22%2C%22ansid%22%3A%22%22%2C%22enterfrom_answerid%22%3A%22%22%2C%22parent_enterfrom%22%3A%22%22%2C%22qid%22%3A%226623128142624063758%22%2C%22category_name%22%3A%22profile_wenda%22%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202005062227140100260601540A3178C9%22%7D%2C%22from_gid%22%3A%22%22%2C%22with_avatar%22%3A%22%22%7D\\u0026refer=wenda\\u0026uid=59712475271","v_icon":"优质动漫领域创作者"},"write_answer_schema":"sslocal://wenda_post?api_param=%7B%22enter_from%22%3A%22click_pgc%22%2C%22origin_from%22%3A%22click_pgc%22%7D\\u0026gd_ext_json=%7B%22enter_from%22%3A%22click_pgc%22%2C%22ansid%22%3A%22%22%2C%22enterfrom_answerid%22%3A%22%22%2C%22parent_enterfrom%22%3A%22%22%2C%22qid%22%3A%226623128142624063758%22%2C%22category_name%22%3A%22profile_wenda%22%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202005062227140100260601540A3178C9%22%7D%2C%22from_gid%22%3A%22%22%2C%22with_avatar%22%3A%22%22%7D\\u0026qTitle=%E2%80%9C%E6%BC%AB%E5%A8%81%E4%B9%8B%E7%88%B6%E2%80%9D%E6%96%AF%E5%9D%A6%C2%B7%E6%9D%8E%E5%8E%BB%E4%B8%96%EF%BC%8C%E4%BD%A0%E5%A6%82%E4%BD%95%E8%AF%84%E4%BB%B7%EF%BC%9F\\u0026qid=6623128142624063758"},"recommend_reason":"回答了问题","repost_params":{"cover_url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/11340/6310107700~120x256.image","fw_id":6623262922753704206,"fw_id_type":1025,"fw_user_id":5857262808,"opt_id":6623262922753704206,"opt_id_type":1025,"repost_type":214,"schema":"","title":"投资界回答了：“漫威之父”斯坦·李去世，你如何评价？"},"share_info":{"content":"刚在《毒液》里看见客串的老爷子，转眼间英雄已逝，一个时代结束了。\u3000\u3000投资界（微信ID：pedaily2012）11月13日消息，据外媒报道，美国漫画界元老级人物斯坦·李于当地时间周一（12日）在好莱坞一家医疗中心去世，享年95岁。\u3000\u3000斯坦·李的个人官方推特发布其去世消息\u3000\u3000漫威影业主席凯文·费吉悼念：“对我的职业生涯和我们在漫威影业所做的一切影响最大的人，就是斯坦·李了。”\u3000\u3000DC官推悼念斯坦·李：“他改变了我们看英雄的方式，现代漫画将一直有他不可磨灭的印记，他那感染人心的热情，让我们想起自己爱上这些故事的初心。”\u3000\u3000这个超级英雄应该是去拯救宇宙了。\u3000\u3000拯救宇宙的漫威之父\u3000\u3000可以说，没有斯坦·李就没有现在漫威的成功。\u3000\u3000正因斯坦·李的天才创业和不懈努力，才创造了媲美星球大战的漫威宇宙；也是因为他创作出神奇四侠，才让漫威在白银时代能与DC的超人气“闪电侠”相抗衡，成为齐名的漫画巨头；更是因为美国队长、钢铁侠、蜘蛛侠、雷神、绿巨人、金刚狼等的存在，才会有我们幼年伟大的英雄梦想。\u3000\u3000斯坦·李原名斯坦利·马丁·利博，1922年12月28日出生在纽约。斯坦·李从小就喜欢阅读神秘小说和冒险故事，热爱写作。为了补贴家用，小斯坦利到处找活干。他曾给报纸长期写过讣闻，帮美国国家结核病中心写过新闻通稿，帮餐馆送过三明治外卖，做过制裤公司的杂工，做过百老汇大戏院的引座员，还做过《纽约先驱论坛报》的订报员。\u3000\u30001939年，16岁的斯坦利从高中毕业。在舅舅的介绍下，斯坦利跟当时的通俗杂志和漫画书出版商马丁·古德曼见了一面。古德曼同意让斯坦利到自己的Timely漫画公司做助理，周薪是8美元。而Timely就是漫威的前身。\u3000\u30001941年，是漫威史上的重要转折点。这一年，漫威漫画的编辑部作出了创作一部“涵盖爱国主义精神”的漫画，用以契合当时正在白热化开展的第二次世界大战的宏观背景，而这便是后来家喻户晓的《美国队长》。\u3000\u3000同年，斯坦利生平第一部作品问世，即《美国队长》系列漫画的第三部，影响了漫威漫画此后半个世纪发展。1961年11月，《神奇四侠》诞生，斯坦·李在漫画界成为焦点。\u3000\u3000后来在搭档漫画家杰克·科比的协助下，创作了《蜘蛛侠》、《钢铁侠》、《雷神托尔》、《绿巨人》、《X战警》、《奇异博士》等漫画角色，并开创了专属于斯坦·李的“神奇模式”。\u3000\u3000斯坦·李的每一部漫画、每一部电影都向我们展现了无与伦比的想象力与庞大的世界观。在他的笔下，公司一步步走向神坛，是毫无争议的漫威之父。\u3000\u30001996 年，阿维·阿拉德开始领导漫威，成立漫威影业。1998 年斯坦·李参与编剧，漫威和新线电影共同制作的《刀锋战士》大获成功。\u3000\u3000也在同年，斯坦·李离开了漫威，成立了“斯坦·李传媒”公司。但因经营不善，2001 年初就倒闭了。2002年，他与人合作创办了POW！娱乐，这家公司2017年5月，被被中国综合型文化产业集团承兴国际集团收购。\u3000\u3000除了创作漫画，斯坦·李也很喜欢“演”。他在世时曾表示，“我骄傲的是，也许我做的一些事情能娱乐到他人。”他也确实做到了，他相继客串出演了《蜘蛛侠》、《X战警》、《神奇四侠》、《钢铁侠》、《美国队长》《雷神托尔》、《无敌浩克》、《复仇者联盟》、《超凡蜘蛛侠》等电影，借客串的演员身份获得“美国全角色历史最高票房演员”。也成了漫威迷们看电影时最大的彩蛋。\u3000\u3000蜘蛛人是斯坦·李最钟爱的形象。不似外太空的超级物种，蜘蛛侠是一个有关成长的漫画在获得超人能力的同时，还要面对学业、生活、女朋友、家庭、人际关系等问题。斯坦·李在接受美国媒体采访时说，“我的所有超级英雄都有人的缺点，我努力表现他们尽管有超人的力量，但他们的生活并不完美。”\u3000\u3000几十年来，斯坦·李几乎每周都同时创作两本漫画，最多时达5本，作品占漫威总量的90%以上。在2002年出版的传记中，他写道：“如果我可以完全真诚地袒露心迹，那么我可以说我就是自己最大的粉丝。”\u3000\u3000打造超级英雄IP，漫威的从0到1\u3000\u3000令人艳羡的漫威英雄IP的打造并不是一开始就是成功的。它在中国也走了一段从0到1的过程。\u3000\u3000最开始，由于受众基础薄弱，英雄IP的受众并不广泛，连续数部电影票房、口碑表现都不理想。比如最开始推出的《无敌浩克》、《钢铁侠2》、《美国队长》、《雷神》中，除已经有一定知名度的《钢铁侠2》取得了1.75亿票房外，其余几部电影票房均未过亿，按照汇率来看甚至不到北美票房的十分之一。整体的市场表现全看档期选择和运气。\u3000\u3000但漫威很聪明，它知道一根火柴的力量渺小，但一盒火柴的力量将能点燃各个受众的心。所以经过了整整十年的布局，以三部《复仇者联盟》为节点，漫威正式走上了“占领心智、发家致富”的道路。\u3000\u3000通过前期的铺路，加深观众对英雄的了解，漫威于是2012年打响了团战的第一炮《复联》。它将英雄基于一战，一起点燃各个英雄粉丝的热情。而《复联1》也在中国实现了爆发式表现，首日6600万的成绩单，两天狂收1.14亿人民币，轻松创下超级英雄电影在华的首映新纪录。而影片在三四线城市的活跃度提升到了40%左右。\u3000\u3000也就是从这一次抱团出战开始，漫威电影的票房权重一路上扬，平均达到15%以上。而单个作品的票房也都保持在了5亿以上。\u3000\u3000（图片来源于网络）\u3000\u3000当然，这只是漫威的第一步，之后《复仇者联盟2》成功斩获14.22亿元，成为内地史上首部在收获10亿+的漫威电影。\u3000\u3000中国市场的良好表现，让漫威受宠若惊。\u3000\u3000其实，从2008年到2018年，经历了90后从学生时代步入到社会工作的过程，而漫威的英雄更加具有陪伴意义。更重要的是，在漫威发展的过程中，中国内地电影市场也在不断向前。2012年—2015年，内地票房的年增速都在30%左右，2015年更是达到了夸张的49%，大量观众开始走进影院，许多进口片都因此而收获了不错的成绩。\u3000\u3000斯坦.李曾表示：中国将成为世界的影视中心，这个世界人口最多的国家需要有自己的超级英雄。就在2017年，漫威就宣布将和网易合作，首创中国的超级英雄：气旋和林烈。在将来这些“中国化”的本土英雄很可能与钢铁侠等初代超级英雄并肩作战。\u3000\u3000据官方宣布，2020年正式推出全沉浸式超级英雄主题公园，新增的三个漫威主题园区分别位于美国加利福尼亚州、法国巴黎以及中国香港。\u3000\u300010年超160亿美元票房的漫威宇宙\u3000\u3000漫威漫画公司创建于1939年，当年10月，第一本漫画推向市场，同时创造了它第一个超级英雄海王纳摩。1941年3月推出的美国队长再次引起轰动，第一次出场，就卖出了100万册的漫画。此后，漫威又陆续推出了绿巨人、蜘蛛侠、雷神、钢铁侠等超级英雄。\u3000\u3000漫威的命运也像它的英雄们一样跌宕起伏，经历了二战等一系列事故，漫威被多次转手：1986 年，漫威被母公司Cadence Industries卖给了New World Pictures；3年后，又被卖给了MacAndrews \\u0026 Forbes Holdings1994年，Andrews Grou和ME又将漫威改组成为漫威控股公司；1996 年，漫威被卷入Carl Icahn和Perelman间的权力斗争。当年12月27 日，漫威正式宣布破产，之后又在多方帮助下，脱离了破产的窘境。\u3000\u3000漫画行业整体衰败，漫威陷入了财政危机。为了渡过难关，漫威决定出售超级英雄的电影拍摄权。1999年，漫威700万美元把《蜘蛛侠》电影版版权卖给了索尼。后者通过《蜘蛛侠》前两部电影大赚16亿美元，但只有7500万属于漫威。\u3000\u30002005年，对分成不满的漫威成立了影业公司。随后从美林银行贷款2.25亿美元投资了《钢铁侠》，背水一战。豪赌成功了，《钢铁侠》全球取得5.85亿美元票房，帮助漫威摆脱窘境。3部《钢铁侠》电影下来全球总票房高达23.8亿美元，3部电影的DVD总共卖出了1700多万份，赚了3亿美元，成为全球最赚钱的系列电影之一。\u3000\u30002009 年，迪士尼以42.4亿美元现金加股票的价格，收购漫威娱乐。2013年起，在迪士尼的主导下，漫威逐渐开始收回散落各处的超级英雄电影版权。漫威成了迪士尼的一部赚钱机器：电影、动画、玩具、游戏、乐园在一条产业链不断衍生发展。\u3000\u3000凭借《X战警》、《蜘蛛侠》横扫美国票房后，漫威开始了自制超级英雄大片的道路，推出了漫威电影宇宙（Marvel Cinematic Universe）计划。自2008年起，一整套清晰完整的电影计划浮出水面，钢铁侠、雷神、美国队长，金刚狼……一个又一个的超级英雄陆续走上银幕，既能孤胆英雄拯救世界，又能合体打怪兽，随后通过《复仇者联盟》将他们集结起来。\u3000\u3000第一阶段，漫威凭借6部影片，以总计10亿美元的成本取得了37.4亿美元的全球票房。第二阶段仅《X战警》就带来了近40亿美元的回报，第三阶段也已进入了筹备拍摄阶段。\u3000\u300078年来，漫威不断推出、贩卖虚拟世界里的英雄。队伍人员日渐壮大，超级英雄的生意也越做越大。大荧幕上超级英雄层出不穷，漫威也没有放过小屏幕。先后推出《神盾局特工》和《卡特特工》两部美剧，剧情紧扣大电影，神盾局为大电影穿针引线，电影、电视剧环环相扣，共同打造出气势恢宏、场面磅礴的漫威帝国。从漫画到电影、电视剧，从游戏到衍生品。\u3000\u3000作为打造超级IP的帝国，漫威做了非常好的榜样。漫威电影宇宙目前全球总票房早已超过了160亿美元，按日前汇率计算折合人民币超1100亿元。\u3000\u3000自大的托尼、正义的美队、嘴炮蜘蛛侠、聪明的班纳、邪魅的洛基、豪爽的雷神、感性的星爵、绯红女巫、无敌的浩克、理性的奇异博士、天真的格鲁特、帅气酷炫的黑豹、战争机器、猎鹰、性感的黑寡妇……“我们爱每一个超级英雄。”\u3000\u3000结语\u3000\u3000英雄们如期赴约，一次次点燃粉丝们内心的激情。从学生到职场，从青年到父母，这些英雄早已不是一个个IP那么简单。\u3000\u3000但如今，江湖失去了金庸大师，漫威世界憾别斯坦·李。从来都是偶像易有，大英雄百年难得。新旧更迭，超级英雄陪着我们逐渐老去，深深的目光中，都有自己年幼的身影。\u3000\u3000美国队长扮演者克里斯·埃文斯悼念：“不会再有另一个斯坦·李了。”","share_type":{"pyq":0,"qq":0,"qzone":0,"wx":0},"share_url":"http://toutiao.com/group/6623262922753704206/?iid=0\\u0026app=news_article","title":"“漫威之父”斯坦·李去世，你如何评价？","token_type":0},"summary":"","tail_content":"","user":{"avatar_url":"http://sf1-ttcdn-tos.pstatp.com/img/mosaic-legacy/11340/6310107700~120x256.image","is_following":0,"is_verify":1,"uname":"投资界","user_auth_info":"{\\"auth_type\\":\\"0\\",\\"auth_info\\":\\"优质财经领域创作者\\",\\"other_auth\\":{\\"interest\\":\\"优质财经领域创作者\\"}}","user_id":"5857262808","user_schema":"sslocal://profile?api_param=%7B%22answer_list%22%3A%5B6623262922753704206%5D%2C%22answer_type%22%3A%22combine_answer%22%2C%22enter_ansid%22%3A%226623262922753704206%22%2C%22enter_from%22%3A%22click_pgc%22%2C%22from%22%3A%22outer%22%2C%22has_more%22%3Atrue%2C%22in_offset%22%3A0%2C%22next_offset%22%3A1%2C%22origin_from%22%3A%22click_pgc%22%7D\\u0026gd_ext_json=%7B%22enter_from%22%3A%22click_pgc%22%2C%22ansid%22%3A%226623262922753704206%22%2C%22enterfrom_answerid%22%3A%226623262922753704206%22%2C%22parent_enterfrom%22%3A%22%22%2C%22qid%22%3A%226623128142624063758%22%2C%22category_name%22%3A%22profile_wenda%22%2C%22author_id%22%3A%225857262808%22%2C%22article_type%22%3A%22wenda%22%2C%22log_pb%22%3A%7B%22impr_id%22%3A%22202005062227140100260601540A3178C9%22%7D%2C%22from_gid%22%3A%22%22%2C%22with_avatar%22%3A%220%22%7D\\u0026refer=wenda\\u0026uid=5857262808","v_icon":"优质财经领域创作者"}},"group_id":"6623262922753704206","item_id":"6623262922753704206"},"read_count":0,"req_id":"202005062227140100260601540A3178C9","rid":"202005062227140100260601540A3178C9","share_count":0,"share_info":null,"show_dislike":false,"show_portrait":false,"show_portrait_article":false,"small_image":null,"tip":0,"ugc_recommend":{"activity":"","reason":""},"user_repin":0,"user_verified":0,"verified_content":"","video_style":0}',
		'code': ''
	},
    ],
	'has_more': True,
	'offset': 1541730014000,
	'tail': '',
	'preload_ack_data': None
}
```

## <span id="jump10">10. 获取头条用户的小视频</span>

状态：**无需登录**

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
ret = bot.get_user_posts('5857262808',kind='SHORTVIDEO')

```
返回示例：第一页
```json
与 10.获取头条用户的问答 返回结果类似
```

## <span id="jump11">11. 获取头条用户的粉丝</span>

状态：**无需登录**

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
ret = bot.get_user_followers('5857262808',offset=20)

```
返回示例：第二页
```json5
{
	'err_no': 0,
	'err_tips': '',
	'offset': 40,
	'cursor': 0,
	'has_more': 1,
	'data': {
		'users': [{
			'user': {
				'info': {
					'user_id': 3714202077,
					'name': '云海摩途影摄',
					'desc': '寻找美，寻觅大自 然光影，愿与你分享摄影美的一切，共享影韵。',
					'schema': 'sslocal://profile?uid=3714202077',
					'avatar_url': 'http://p1.pstatp.com/thumb/db06001bcf9120b13761',
					'user_auth_info': '{"auth_type":"0","auth_info":"山东省摄影家协会会员 优质摄影领域创作者","other_auth":{"interest":"优质摄影领域创作者"}}',
					'user_verified': 0,
					'verified_content': '山东省摄影家协会会员 优质摄影领域创作者',
					'medals': None,
					'user_url': '',
					'remark_name': '',
					'user_decoration': ''
				},
				'relation': {
					'is_friend': 0,
					'is_following': 0,
					'is_followed': 0
				},
				'relation_count': {
					'followings_count': 4974,
					'followers_count': 4317
				}
			},
			'recommend_reason': '山东省摄影家协会会员 优质摄影领域创作者',
			'stats_place_holder': '{"impr_id":"2020050622440001002103404714662B5B"}',
			'interaction': 0
		}, 
         ],
		'anonymous_fans': 82890
	}
}
```

## <span id="jump12">12. 获取头条用户的关注列表</span>

状态：**无需登录**

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
ret = bot.get_user_followings('5857262808',offset=20)

```
返回示例：第二页
```json5
{
	'err_no': 0,
	'err_tips': '',
	'offset': 40,
	'cursor': 0,
	'has_more': 1,
	'data': {
		'users': [{
			'user': {
				'info': {
					'user_id': 4734810855,
					'name': '潘石屹',
					'desc': 'SOHO中国董事长。分享我的工作和生活。',
					'schema': 'sslocal://profile?uid=4734810855',
					'avatar_url': 'http://p1.pstatp.com/thumb/137560000012d65440f77',
					'user_auth_info': '{"auth_type": "1", "auth_info": "SOHO中国董事长"}',
					'user_verified': 1,
					'verified_content': 'SOHO中国董事长',
					'medals': None,
					'user_url': '',
					'remark_name': '',
					'user_decoration': ''
				},
				'relation': {
					'is_friend': 0,
					'is_following': 0,
					'is_followed': 0
				},
				'relation_count': {
					'followings_count': 43,
					'followers_count': 1386666
				}
			},
			'recommend_reason': 'SOHO中国董事长',
			'stats_place_holder': '{"impr_id":"202005062254000100260790193F541D79"}',
			'interaction': 0
		},]
	}
}
```

## <span id="jump13">13. 获取头条多媒体（视频/文章等）信息</span>

状态：**无需登录**

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
ret = bot.get_item_info('6771975338621665796')

```
返回示例：略

## <span id="jump14">14. 获取头条多媒体（视频/文章）的一级评论</span>

状态：**无需登录**

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
ret = bot.get_item_comments('6771975338621665796')

```
返回示例：略

## <span id="jump15">15. 关键词搜索</span>

状态：**无需登录**

调用示例：
```python
from toutiao import TTBot

bot = TTBot()
# 关键词搜索直播间，根据kind参数确定类别，具体字段为： 
# 用户/USER 视频/VIDEO 小视频/SHORTVIDEO
# 图片/PICTURE 音乐/MUSIC 综合/GENERAL 资讯/NEWS
# 问答/QUESTION 话题/TOPIC 直播/LIVE
ret = bot.search('美女',kind='LIVE')

```
返回示例：略

