import threading
import datetime
import os

def clone(repo):
    def f():
        if os.system('cd %s/media/repositories && git clone %s %s' %
                (os.getcwd(), repo.url, repo.name)) == 0:
            repo.state = 'o'
            repo.latest_fetch = datetime.datetime.now()
        else:
            repo.state = 'n'
        repo.save()
    thread = threading.Thread(target=f, name='Cloning repo %s.' % repo.name)
    thread.start()
    return thread
