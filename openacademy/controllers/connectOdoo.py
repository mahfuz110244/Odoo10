import functools
import xmlrpclib
HOST = 'localhost'
PORT = 8069
DB = 'local'
USER = 'bs-086'
PASS = 'admin'
ROOT = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

# 1. Login
uid = xmlrpclib.ServerProxy(ROOT + 'common').login(DB,USER,PASS)
print "Logged in as %s (uid:%d)" % (USER,uid)

call = functools.partial(
    xmlrpclib.ServerProxy(ROOT + 'object').execute,
    DB, uid, PASS)

# # 2. Read the sessions
# sessions = call('openacademy.session','search_read', [], ['name','seats'])

# for session in sessions:
#     print "Session %s (%s seats)" % (session['name'], session['seats'])
# 3.create a new session
# session_id = call('openacademy.session', 'create', {
#     'name' : 'My session',
#     'course_id' : 2,
# })

server = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/common')
user_id = server.login(DB, USER, PASS)

server = xmlrpclib.ServerProxy('http://localhost:8069/xmlrpc/object')
user_ids = server.execute(
    DB, user_id, PASS,
    'res.users', 'search', []
)

users = server.execute(
    DB, user_id, PASS,
    'res.users', 'read', user_ids, []
)

for user in users:
    print(user['id'], user['name'])