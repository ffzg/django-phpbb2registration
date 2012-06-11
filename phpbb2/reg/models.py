# -*- coding: UTF-8 -*-
# This is an auto-generated Django model module.

from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _

import time

def get_current_unix_time():
    return int(time.time())

class TopicsEmailTable(models.Model):
    user_id = models.IntegerField(primary_key=True)
    friend_name = models.CharField(max_length=300)
    friend_email = models.CharField(max_length=300)
    topic_id = models.IntegerField()
    time = models.IntegerField()
    class Meta:
        db_table = u'TOPICS_EMAIL_TABLE'

class PhpbbAntiRoboticReg(models.Model):
    session_id = models.CharField(max_length=96, primary_key=True)
    reg_key = models.CharField(max_length=15)
    timestamp = models.IntegerField()
    class Meta:
        db_table = u'phpbb_anti_robotic_reg'

class PhpbbAuthAccess(models.Model):
    group_id = models.IntegerField(primary_key=True)
    forum_id = models.IntegerField()
    auth_view = models.IntegerField()
    auth_read = models.IntegerField()
    auth_post = models.IntegerField()
    auth_reply = models.IntegerField()
    auth_edit = models.IntegerField()
    auth_delete = models.IntegerField()
    auth_sticky = models.IntegerField()
    auth_announce = models.IntegerField()
    auth_vote = models.IntegerField()
    auth_pollcreate = models.IntegerField()
    auth_attachments = models.IntegerField()
    auth_mod = models.IntegerField()
    class Meta:
        db_table = u'phpbb_auth_access'

class PhpbbBanlist(models.Model):
    ban_id = models.IntegerField(primary_key=True)
    ban_userid = models.IntegerField()
    ban_ip = models.CharField(max_length=24)
    ban_email = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'phpbb_banlist'

class PhpbbCategories(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_title = models.CharField(max_length=300, blank=True)
    cat_order = models.IntegerField()
    class Meta:
        db_table = u'phpbb_categories'

class PhpbbConfirm(models.Model):
    confirm_id = models.CharField(max_length=96, primary_key=True)
    session_id = models.CharField(max_length=96, primary_key=True)
    code = models.CharField(max_length=18)
    class Meta:
        db_table = u'phpbb_confirm'

class PhpbbDisallow(models.Model):
    disallow_id = models.IntegerField(primary_key=True)
    disallow_username = models.CharField(max_length=75, blank=True)
    class Meta:
        db_table = u'phpbb_disallow'

class PhpbbForumPrune(models.Model):
    prune_id = models.IntegerField(primary_key=True)
    forum_id = models.IntegerField()
    prune_days = models.IntegerField()
    prune_freq = models.IntegerField()
    class Meta:
        db_table = u'phpbb_forum_prune'

class PhpbbForums(models.Model):
    forum_id = models.IntegerField(primary_key=True)
    cat_id = models.IntegerField()
    forum_name = models.CharField(max_length=450, blank=True)
    forum_desc = models.TextField(blank=True)
    forum_status = models.IntegerField()
    forum_order = models.IntegerField()
    forum_posts = models.IntegerField()
    forum_topics = models.IntegerField()
    forum_last_post_id = models.IntegerField()
    prune_next = models.IntegerField(null=True, blank=True)
    prune_enable = models.IntegerField()
    auth_view = models.IntegerField()
    auth_read = models.IntegerField()
    auth_post = models.IntegerField()
    auth_reply = models.IntegerField()
    auth_edit = models.IntegerField()
    auth_delete = models.IntegerField()
    auth_sticky = models.IntegerField()
    auth_announce = models.IntegerField()
    auth_vote = models.IntegerField()
    auth_pollcreate = models.IntegerField()
    auth_attachments = models.IntegerField()
    class Meta:
        db_table = u'phpbb_forums'

class PhpbbGroups(models.Model):
    group_id = models.IntegerField(primary_key=True)
    group_type = models.IntegerField()
    group_name = models.CharField(max_length=120, blank=True)
    group_description = models.CharField(max_length=765, blank=True)
    group_moderator = models.IntegerField()
    group_single_user = models.IntegerField()
    class Meta:
        db_table = u'phpbb_groups'

class PhpbbIgnore(models.Model):
    user_id = models.IntegerField(primary_key=True)
    user_ignore = models.IntegerField()
    class Meta:
        db_table = u'phpbb_ignore'

class PhpbbPosts(models.Model):
    post_id = models.IntegerField(primary_key=True)
    topic_id = models.IntegerField()
    forum_id = models.IntegerField()
    poster_id = models.IntegerField()
    post_time = models.IntegerField()
    poster_ip = models.CharField(max_length=24, blank=True)
    post_username = models.CharField(max_length=75, blank=True)
    enable_bbcode = models.IntegerField()
    enable_html = models.IntegerField()
    enable_smilies = models.IntegerField()
    enable_sig = models.IntegerField()
    post_edit_time = models.IntegerField(null=True, blank=True)
    post_edit_count = models.IntegerField()
    class Meta:
        db_table = u'phpbb_posts'

class PhpbbPostsText(models.Model):
    post_id = models.IntegerField(primary_key=True)
    bbcode_uid = models.CharField(max_length=30)
    post_subject = models.CharField(max_length=180, blank=True)
    post_text = models.TextField(blank=True)
    class Meta:
        db_table = u'phpbb_posts_text'

class PhpbbPrivmsgs(models.Model):
    privmsgs_id = models.IntegerField(primary_key=True)
    privmsgs_type = models.IntegerField()
    privmsgs_subject = models.CharField(max_length=765, blank=True)
    privmsgs_from_userid = models.IntegerField()
    privmsgs_to_userid = models.IntegerField()
    privmsgs_date = models.IntegerField()
    privmsgs_ip = models.CharField(max_length=24, blank=True)
    privmsgs_enable_bbcode = models.IntegerField()
    privmsgs_enable_html = models.IntegerField()
    privmsgs_enable_smilies = models.IntegerField()
    privmsgs_attach_sig = models.IntegerField()
    class Meta:
        db_table = u'phpbb_privmsgs'

class PhpbbPrivmsgsText(models.Model):
    privmsgs_text_id = models.IntegerField(primary_key=True)
    privmsgs_bbcode_uid = models.CharField(max_length=30, blank=True)
    privmsgs_text = models.TextField(blank=True)
    class Meta:
        db_table = u'phpbb_privmsgs_text'

class PhpbbProfileView(models.Model):
    user_id = models.IntegerField(primary_key=True)
    viewername = models.CharField(max_length=75, blank=True)
    viewer_id = models.IntegerField()
    view_stamp = models.IntegerField()
    counter = models.IntegerField()
    class Meta:
        db_table = u'phpbb_profile_view'

class PhpbbRanks(models.Model):
    rank_id = models.IntegerField(primary_key=True)
    rank_title = models.CharField(max_length=150)
    rank_min = models.IntegerField()
    rank_special = models.IntegerField(null=True, blank=True)
    rank_image = models.CharField(max_length=765, blank=True)
    class Meta:
        db_table = u'phpbb_ranks'

class PhpbbSearchResults(models.Model):
    search_id = models.IntegerField(primary_key=True)
    session_id = models.CharField(max_length=96, blank=True)
    search_array = models.TextField()
    search_time = models.IntegerField()
    class Meta:
        db_table = u'phpbb_search_results'

class PhpbbSearchWordlist(models.Model):
    word_text = models.CharField(max_length=150, primary_key=True)
    word_id = models.IntegerField()
    word_common = models.IntegerField()
    class Meta:
        db_table = u'phpbb_search_wordlist'

class PhpbbSearchWordmatch(models.Model):
    post_id = models.IntegerField()
    word_id = models.IntegerField(primary_key=True)
    title_match = models.IntegerField()
    class Meta:
        db_table = u'phpbb_search_wordmatch'

class PhpbbSessions(models.Model):
    session_id = models.CharField(max_length=96, primary_key=True)
    session_user_id = models.IntegerField()
    session_start = models.IntegerField()
    session_time = models.IntegerField()
    session_ip = models.CharField(max_length=24)
    session_page = models.IntegerField()
    session_logged_in = models.IntegerField()
    session_admin = models.IntegerField()
    priv_session_id = models.CharField(max_length=96)
    class Meta:
        db_table = u'phpbb_sessions'

class PhpbbSessionsKeys(models.Model):
    key_id = models.CharField(max_length=96, primary_key=True)
    user_id = models.IntegerField(primary_key=True)
    last_ip = models.CharField(max_length=24, blank=True)
    last_login = models.IntegerField()
    class Meta:
        db_table = u'phpbb_sessions_keys'

class PhpbbSmilies(models.Model):
    smilies_id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=150, blank=True)
    smile_url = models.CharField(max_length=300, blank=True)
    emoticon = models.CharField(max_length=225, blank=True)
    class Meta:
        db_table = u'phpbb_smilies'

class PhpbbThemes(models.Model):
    themes_id = models.IntegerField(primary_key=True)
    template_name = models.CharField(max_length=90)
    style_name = models.CharField(max_length=90)
    head_stylesheet = models.CharField(max_length=300, blank=True)
    body_background = models.CharField(max_length=300, blank=True)
    body_bgcolor = models.CharField(max_length=18, blank=True)
    body_text = models.CharField(max_length=18, blank=True)
    body_link = models.CharField(max_length=18, blank=True)
    body_vlink = models.CharField(max_length=18, blank=True)
    body_alink = models.CharField(max_length=18, blank=True)
    body_hlink = models.CharField(max_length=18, blank=True)
    tr_color1 = models.CharField(max_length=18, blank=True)
    tr_color2 = models.CharField(max_length=18, blank=True)
    tr_color3 = models.CharField(max_length=18, blank=True)
    tr_class1 = models.CharField(max_length=75, blank=True)
    tr_class2 = models.CharField(max_length=75, blank=True)
    tr_class3 = models.CharField(max_length=75, blank=True)
    th_color1 = models.CharField(max_length=18, blank=True)
    th_color2 = models.CharField(max_length=18, blank=True)
    th_color3 = models.CharField(max_length=18, blank=True)
    th_class1 = models.CharField(max_length=75, blank=True)
    th_class2 = models.CharField(max_length=75, blank=True)
    th_class3 = models.CharField(max_length=75, blank=True)
    td_color1 = models.CharField(max_length=18, blank=True)
    td_color2 = models.CharField(max_length=18, blank=True)
    td_color3 = models.CharField(max_length=18, blank=True)
    td_class1 = models.CharField(max_length=75, blank=True)
    td_class2 = models.CharField(max_length=75, blank=True)
    td_class3 = models.CharField(max_length=75, blank=True)
    fontface1 = models.CharField(max_length=150, blank=True)
    fontface2 = models.CharField(max_length=150, blank=True)
    fontface3 = models.CharField(max_length=150, blank=True)
    fontsize1 = models.IntegerField(null=True, blank=True)
    fontsize2 = models.IntegerField(null=True, blank=True)
    fontsize3 = models.IntegerField(null=True, blank=True)
    fontcolor1 = models.CharField(max_length=18, blank=True)
    fontcolor2 = models.CharField(max_length=18, blank=True)
    fontcolor3 = models.CharField(max_length=18, blank=True)
    span_class1 = models.CharField(max_length=75, blank=True)
    span_class2 = models.CharField(max_length=75, blank=True)
    span_class3 = models.CharField(max_length=75, blank=True)
    img_size_poll = models.IntegerField(null=True, blank=True)
    img_size_privmsg = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'phpbb_themes'

class PhpbbThemesName(models.Model):
    themes_id = models.IntegerField(primary_key=True)
    tr_color1_name = models.CharField(max_length=150, blank=True)
    tr_color2_name = models.CharField(max_length=150, blank=True)
    tr_color3_name = models.CharField(max_length=150, blank=True)
    tr_class1_name = models.CharField(max_length=150, blank=True)
    tr_class2_name = models.CharField(max_length=150, blank=True)
    tr_class3_name = models.CharField(max_length=150, blank=True)
    th_color1_name = models.CharField(max_length=150, blank=True)
    th_color2_name = models.CharField(max_length=150, blank=True)
    th_color3_name = models.CharField(max_length=150, blank=True)
    th_class1_name = models.CharField(max_length=150, blank=True)
    th_class2_name = models.CharField(max_length=150, blank=True)
    th_class3_name = models.CharField(max_length=150, blank=True)
    td_color1_name = models.CharField(max_length=150, blank=True)
    td_color2_name = models.CharField(max_length=150, blank=True)
    td_color3_name = models.CharField(max_length=150, blank=True)
    td_class1_name = models.CharField(max_length=150, blank=True)
    td_class2_name = models.CharField(max_length=150, blank=True)
    td_class3_name = models.CharField(max_length=150, blank=True)
    fontface1_name = models.CharField(max_length=150, blank=True)
    fontface2_name = models.CharField(max_length=150, blank=True)
    fontface3_name = models.CharField(max_length=150, blank=True)
    fontsize1_name = models.CharField(max_length=150, blank=True)
    fontsize2_name = models.CharField(max_length=150, blank=True)
    fontsize3_name = models.CharField(max_length=150, blank=True)
    fontcolor1_name = models.CharField(max_length=150, blank=True)
    fontcolor2_name = models.CharField(max_length=150, blank=True)
    fontcolor3_name = models.CharField(max_length=150, blank=True)
    span_class1_name = models.CharField(max_length=150, blank=True)
    span_class2_name = models.CharField(max_length=150, blank=True)
    span_class3_name = models.CharField(max_length=150, blank=True)
    class Meta:
        db_table = u'phpbb_themes_name'

class PhpbbTopics(models.Model):
    topic_id = models.IntegerField(primary_key=True)
    forum_id = models.IntegerField()
    topic_title = models.CharField(max_length=180, blank=True)
    topic_poster = models.IntegerField()
    topic_time = models.IntegerField()
    topic_views = models.IntegerField()
    topic_replies = models.IntegerField()
    topic_status = models.IntegerField()
    topic_vote = models.IntegerField()
    topic_type = models.IntegerField()
    topic_first_post_id = models.IntegerField()
    topic_last_post_id = models.IntegerField()
    topic_moved_id = models.IntegerField()
    class Meta:
        db_table = u'phpbb_topics'

class PhpbbUserGroup(models.Model):
    group_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    user_pending = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = u'phpbb_user_group'

class PhpbbUsers(models.Model):

    LANGUAGE = (
        ('croatian', _('Croatian')),
        ('czech', _('Czech')),
        ('english', _('English')),
        ('french', _('French')),
        ('german', _('German')),
        ('italian', _('Italian')),
        ('polish', _('Polish')),
        ('russian', _('Russian')),
        ('slovenian', _('Slovenian')),
    )
    
    # better solution ?
    YES_NO = (
    	(1, _('Yes')),
	    (0, _('No')),
    )

    user_id = models.IntegerField(primary_key=True)
    user_active = models.IntegerField(null=True, default=0)
    username = models.CharField(max_length=75)
    user_password = models.CharField(max_length=96)
    user_session_time = models.IntegerField(default=0)
    user_session_page = models.IntegerField(default=0)
    user_lastvisit = models.IntegerField(default=0)
    user_regdate = models.IntegerField(default=get_current_unix_time())
    user_level = models.IntegerField(null=True, default=0)
    user_posts = models.IntegerField(default=0)
    user_timezone = models.DecimalField(max_digits=7, decimal_places=2, default="1.00")
    user_style = models.IntegerField(null=True, default=21)
    user_lang = models.CharField(max_length=765, choices=LANGUAGE)
    user_dateformat = models.CharField(max_length=42, default='d M Y H:i')
    user_new_privmsg = models.IntegerField(default=0)
    user_unread_privmsg = models.IntegerField(default=0)
    user_last_privmsg = models.IntegerField(default=0)
    user_emailtime = models.IntegerField(null=True, blank=True)
    user_viewemail = models.IntegerField(null=True, default=0)
    user_profile_view_popup = models.IntegerField(null=True, default=0)
    user_attachsig = models.IntegerField(null=True, choices=YES_NO, default=1)
    user_allowhtml = models.IntegerField(null=True, choices=YES_NO, default=1)
    user_allowbbcode = models.IntegerField(null=True, choices=YES_NO, default=1)
    user_allowsmile = models.IntegerField(null=True, choices=YES_NO, default=1)
    user_allowavatar = models.IntegerField(choices=YES_NO, default=1)
    user_allow_pm = models.IntegerField(choices=YES_NO, default=1)
    user_allow_viewonline = models.IntegerField(choices=YES_NO, default=1)
    user_notify = models.IntegerField(choices=YES_NO, default=0)
    user_notify_pm = models.IntegerField(choices=YES_NO, default=1)
    user_popup_pm = models.IntegerField(choices=YES_NO, default=1)
    user_rank = models.IntegerField(null=True, default=0)
    user_avatar = models.CharField(max_length=300, blank=True)
    user_avatar_type = models.IntegerField(default=0)
    user_email = models.CharField(max_length=765)
    user_icq = models.CharField(max_length=45, blank=True)
    user_website = models.CharField(max_length=300, blank=True)
    user_from = models.CharField(max_length=300, blank=True)
    user_sig = models.TextField(blank=True)
    user_sig_bbcode_uid = models.CharField(max_length=30, blank=True)
    user_aim = models.CharField(max_length=765, blank=True)
    user_yim = models.CharField(max_length=765, blank=True)
    user_msnm = models.CharField(max_length=765, blank=True)
    user_occ = models.CharField(max_length=300, blank=True)
    user_interests = models.CharField(max_length=765, blank=True)
    user_actkey = models.CharField(max_length=96, blank=True)
    user_newpasswd = models.CharField(max_length=96, blank=True)
    user_profile_view = models.IntegerField(default=0)
    user_last_profile_view = models.IntegerField(default=0)
    irc_commands = models.CharField(max_length=765, blank=True)
    user_birthday = models.IntegerField(default=999999)
    user_next_birthday_greeting = models.IntegerField(default=0)
    user_uppp = models.IntegerField(default=0)
    user_reg_ip = models.TextField(blank=True)
    user_reg_host = models.TextField(blank=True)
    user_topics_per_page = models.CharField(max_length=15, default=50)
    user_posts_per_page = models.CharField(max_length=15, default=15)
    user_hot_threshold = models.CharField(max_length=15, default=15)
    user_login_tries = models.IntegerField(default=0)
    user_last_login_try = models.IntegerField(default=0)
    ldap_username = models.CharField(max_length=96, blank=True)
    local_user = models.IntegerField(null=True, default=0)
    user_allowsignature = models.IntegerField(choices=YES_NO, default=1)

    def __unicode__(self):
        return self.username

    class Meta:
        db_table = u'phpbb_users'
        verbose_name = 'phpbb user'

    def save(self, *args, **kwargs):
        if not self.user_id:
            i = PhpbbUsers.objects.all().order_by('-user_id')[0]
            self.user_id = i.user_id+1
        super(PhpbbUsers, self).save(*args, **kwargs) 


class PhpbbDjangoUserLink(models.Model):
    user = models.ForeignKey(User, unique=True)
    phpbb_user = models.ForeignKey(PhpbbUsers, unique=True)

class PhpbbVoteDesc(models.Model):
    vote_id = models.IntegerField(primary_key=True)
    topic_id = models.IntegerField()
    vote_text = models.TextField(blank=True)
    vote_start = models.IntegerField()
    vote_length = models.IntegerField()
    class Meta:
        db_table = u'phpbb_vote_desc'

class PhpbbVoteResults(models.Model):
    vote_id = models.IntegerField(primary_key=True)
    vote_option_id = models.IntegerField()
    vote_option_text = models.CharField(max_length=765, blank=True)
    vote_result = models.IntegerField()
    class Meta:
        db_table = u'phpbb_vote_results'

class PhpbbVoteVoters(models.Model):
    vote_id = models.IntegerField()
    vote_user_id = models.IntegerField(primary_key=True)
    vote_user_ip = models.CharField(max_length=24, blank=True)
    class Meta:
        db_table = u'phpbb_vote_voters'

class PhpbbWords(models.Model):
    word_id = models.IntegerField(primary_key=True)
    word = models.CharField(max_length=300, blank=True)
    replacement = models.CharField(max_length=300, blank=True)
    class Meta:
        db_table = u'phpbb_words'

