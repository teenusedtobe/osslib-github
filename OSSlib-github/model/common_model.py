from sqlobject import *
from conf import config_operate
uri = config_operate.get_dbconfig_uri()
sqlhub.processConnection = connectionForURI(uri)


# oss community api
class OsslibCommunityApi(SQLObject):
    community_name = StringCol(length=50, notNone=True)
    get_oss_list_api = StringCol(length=255, notNone=True)
    get_oss_single_api = StringCol(length=255, notNone=True)
    git_api = StringCol(length=255)


class OsslibMetadata_2(SQLObject):
    community_id = IntCol(length=50,)
    community_from = IntCol(length=11)
    oss_name = StringCol(length=50)
    oss_fullname = StringCol(length=100, unique=True)
    oss_create_time = StringCol(length=50)
    oss_git_url = StringCol(length=200)
    oss_git_tool = StringCol(length=30)
    oss_repo_url = StringCol(length=200)
    oss_homepage = StringCol(length=100)
    oss_license = StringCol(length=100)
    oss_description = StringCol(length=5000)
    oss_local_path = StringCol(length=50)
    oss_line_count = IntCol(length=50)
    oss_developer_count = IntCol(length=50)
    oss_file_count = IntCol(length=50)
    oss_commit_count = IntCol(length=50)
    oss_lastupdate_time = StringCol(length=50)
    oss_owner_id = IntCol(length=50)
    oss_owner_type = StringCol(length=100)
    oss_star = IntCol(length=11)
    oss_main_language = StringCol(length=50)
    oss_owner_id = IntCol(length=11)
    oss_owner_type = StringCol(length=11)
    oss_size = IntCol(length=11)
    oss_lastupdate_time = StringCol(length=50)
    has_wiki = IntCol(length=11)
    readme = StringCol(length=5000)

class OsslibTopic(SQLObject):
    oss_id = IntCol(length=11)
    topic = StringCol(length=100)
	
	
	
class General(SQLObject):
    project_name = StringCol(length=255)
    generated = StringCol(length=255)
    generator = StringCol(length=255)
    report_period = StringCol(length=255)
    age_days = StringCol(length=255)
    total_files = StringCol(length=255)
    total_lines_of_code = StringCol(length=255)
    total_commits = StringCol(length=255)
    authors = StringCol(length=255)

class ActivityWeek (SQLObject):
    week=IntCol(length=11)
    commits=IntCol(length=11)
    project_name=StringCol(length=255)
	
	
class ActivityHour (SQLObject):
    hour = IntCol(length=11)
    commits = IntCol(length=11)
    project_name=StringCol(length=255)
	
class ActivityDay(SQLObject):
    day = StringCol(length=255)
    commits = IntCol(length=11)
    project_name=StringCol(length=255)
	
class ActivityHourOfWeek(SQLObject):
    weekday_hour = StringCol(length=255)
    commits = IntCol(length=11)
    project_name=StringCol(length=255)
	
class ActivityMonth(SQLObject):
    month = StringCol(length=255)
    commits = IntCol(length=11)
    project_name=StringCol(length=255)


class ActivityYear(SQLObject):
    year = IntCol(length=11)
    commits = IntCol(length=11)
    project_name=StringCol(length=255)
	
class ActivityYearMonth(SQLObject):
    yearmonth = StringCol(length=255)
    commits = IntCol(length=11)
    project_name=StringCol(length=255)
	
class ActivityTimezone(SQLObject):
    timezone = StringCol(length=255)
    commits = IntCol(length=11)
    project_name=StringCol(length=255)
	
class AuthorList(SQLObject):
    author = StringCol(length=255)
    commits = IntCol(length=11)
    commits_frac = StringCol(length=255)
    lines_added = IntCol(length=11)
    lines_removed = IntCol(length=11)
    first_commit = StringCol(length=255)
    last_commit = StringCol(length=255)
    age = StringCol(length=255)
    active_days = IntCol(length=11)
    by_commits = IntCol(length=11)
    project_name=StringCol(length=255)
	
class AuthorCumulated(SQLObject):
    date = StringCol(length=255)
    author = StringCol(length=255)
    cumulated_commits = IntCol(length=11)
    cumulated_lines = IntCol(length=11)
    project_name = StringCol(length=255)
	
class AuthorMonth(SQLObject):
    month = StringCol(length=255)
    author = StringCol(length=255)
    commits = StringCol(length=255)
    next_top5 = StringCol(length=255)
    author_number = IntCol(length=11)
    project_name = StringCol(length=255)
	
class AuthorYear(SQLObject):
    year = IntCol(length=11)
    author = StringCol(length=255)
    commits = StringCol(length=255)
    next_top5 = StringCol(length=255)
    author_number = IntCol(length=11)
    project_name = StringCol(length=255)

class Domain(SQLObject):
    domain=StringCol(length=255)
    commits=StringCol(length=255)
    project_name = StringCol(length=255)
	
class FileDateCount(SQLObject):
    date=StringCol(length=255)
    files=IntCol(length=11)
    project_name = StringCol(length=255)

class FileExtension(SQLObject):
    extension=StringCol(length=255)
    files=StringCol(length=255)
    line=StringCol(length=255)
    filesdividelines=IntCol(length=11)
    project_name = StringCol(length=255)
 
class LineDateCount(SQLObject):
    date=StringCol(length=255)
    line=IntCol(length=11)
    project_name = StringCol(length=255)

class Tag(SQLObject):
    name=StringCol(length=255)
    date=StringCol(length=255)
    commits=IntCol(length=11)
    authors=StringCol(length=3000)
    project_name=StringCol(length=255)
 

	