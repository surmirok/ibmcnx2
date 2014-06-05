######
#  Sync ExId through all Applications
#
#  Author:        Christoph Stoettner
#  Mail:          christoph.stoettner@stoeps.de
#  Documentation: http://scripting101.stoeps.de
#
#  Version:       2.0
#  Date:          2014-06-04
#
#  License:       Apache 2.0
#

# Load all jython commands, when they are not loaded
try:
    NewsActivityStreamService.listApplicationRegistrations()
except NameError:
    print "Connections Commands not loaded! Load now: "
    execfile("loadAll.py")

EmailMatch = ''
while EmailMatch != ( 'TRUE' or 'FALSE' ):
    EmailMatchInput = raw_input( 'updateOnEmailLoginMatch (t)rue or (f)alse) ' ).upper()
    if EmailMatchInput == 'T' or EmailMatchInput == "TRUE":
        EmailMatch = 'true'
        break
    elif EmailMatchInput == 'F' or EmailMatchInput == "FALSE":
        EmailMatch = 'false'
        break
    else:
        continue

apps = ['Activities', 'Blogs', 'Communities', 'Dogear', 'Files', 'Forums', 'News', 'Wikis']

def memService( appname, EmailMatch ):
    if( "Activities" == appname ) :
        # print "\tActivitiesMemberService.syncAllMembersByExtId"
        ActivitiesMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    elif( "Blogs" == appname ) :
        # print "\tBlogsMemberService.syncAllMembersByExtId"
        BlogsMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    elif( "News" == appname ) :
        # print "\tNewsMemberService.syncAllMembersByExtId"
        NewsMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    elif( "Dogear" == appname ) :
        # print "\tDogearMemberService.syncAllMembersByExtId"
        DogearMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    elif( "Communities" == appname ) :
        # print "\tCommunitesMemberService.syncAllMembersByExtId"
        CommunitiesMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    elif( "Files" == appname ) :
        # print "\tFilesMemberService.syncAllMembersByExtId"
        FilesMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    elif( "Forums" == appname ) :
        # print "\tForumsMemberService.syncAllMembersByExtId"
        ForumsMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    elif( "Wikis" == appname ) :
        # print "\tWikisMemberService.syncAllMembersByExtId"
        WikisMemberService.syncAllMembersByExtId( {"updateOnEmailLoginMatch": EmailMatch } )
    else :
        print "\tUnknown application name '" + appname + "'"

for app in apps:
    print "Sync all Members by EXTID for " + app + ', ',
    try:
        memService( app, EmailMatch )
    except:
        print 'Error when synchronizing ' + app
