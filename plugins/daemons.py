import threading
import datetime
import os

from settings import MEDIA_ROOT

def clone(repo):
    def f():
        path = os.path.join(MEDIA_ROOT, 'repositories')
        if os.system('cd %s/media/repositories && git clone %s %s' %
                (path, repo.url, repo.name)) == 0:
            repo.state = 'o'
            repo.latest_fetch = datetime.datetime.now()
        else:
            repo.state = 'n'
        repo.save()
    thread = threading.Thread(target=f, name='Cloning repo %s.' % repo.name)
    thread.start()
    return thread
