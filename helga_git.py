from collections import defaultdict

from helga.plugins import command, registry

from github import Github

def format_help_string(name, *helps):
    return u'[{0}] {1}'.format(name, '. '.join(helps))

g = Github("[add_your_Github_token_here]")

@command('checkLGTM', aliases=['check'],
         help="check if any of the PRs on the repo have more than 2 LGTMs")
def checkLGTM(client, channel, nick, message, cmd, args):

    try:
        return_list = []
        repo = args[0]
        for pull in g.get_user().get_repo(repo).get_pulls():
                    title = pull.title
                    #print title
                    count = 0
                    #flag = false
                    for comment in pull.get_issue_comments():
                        if "LGTM" in comment.body:
                            count +=  1
                    if count >= 2 :
                        return_list.append("{title} is Ready to be merged with {n} LGTMs".format(title=title, n=count))
                    else:
                        return_list.append("{title} is NOT Ready to be merged because it has only {n} LGTMs".format(title=title, n=count))
        if len(return_list) == 0:
            return "There are no Pull Requests for this repository"
        return return_list
    except IndexError:
        print "The repo name is invalid"
