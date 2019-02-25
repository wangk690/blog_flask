#coding=utf-8
# from flask import Flask
# app = Flask(__name__, static_folder='tmp', static_url_path='/assets')
# app = Flask(__name__)
# print(app.root_path)
# @app.route('/')
# def index():
# 	return 'Hello Flask.'

# @app.route('/test')
# def test():
# 	return 'this is reponse'

# def test_a():
# 	return 'this is reponse a'
# app.add_url_rule('/test_a', view_func=test_a)

# @app.route('/a', endpoint='whocare')
# def home_a():
# 	return 'endpoint is whocare'

# @app.route('/b')
# def home_b():
# 	return 'endpoint is home_b'

# @app.route('/ep_index', endpoint='whocare')
# def home():
# 	return 'ep_index'

# @app.route('/ep_about')
# def home():
# 	return 'ep_abhout'

# print(app.url_map)
# print('------------')
# print(app.view_functions)

from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def v_index():
	return '''
	 <form method='GET' action='/search'>
	 	<input type='text' placeholder="input keywords" value='Python Flask' name="q">
	 	<input type='text' placeholder='page' name='page'>
	 	<input type="submit" value='search'>
	 </form>
	'''

@app.route('/search')
def v_search():
	if 'q' in request.args:
		if 'page' in request.args:
			if request.args['page'] != '':
				ret = '<p> searching %s..., page is %s</p>' % (request.args['q'], request.args['page'])
			else:
				ret = '<p> searching %s...</p>' % request.args['q']
	else:
		ret = 'what do you want to search?'
	return ret

# @app.route('/')
# def index():
# 	uid = request.form['uid']
# 	pwd = request.form['pwd']
# 	return 'uid: %s, pwd: %s' %(uid, pwd)

# @app.route('/search')
# def v_search():
# 	q = request.args['q']
# 	return 'you ard searching %s' %q
# @app.route('/')
# def index():
# 	print(url_for('v_contacts')) 
# 	print(url_for('v_contact', uname='Julia'))
# 	print(url_for('v_contact', uname='Julia', ret='json'))
# 	print(url_for('v_contact', uname='Julia', _external=True))
# 	print(url_for('v_contact', uname='Julia', _external=True, _scheme='https'))
# 	print(url_for('v_contact', uname='Julia', _anchor='phto'))
# 	return ''

# @app.route('/contact/<uname>')
# def v_contact(uname):
# 	pass
# @app.route('/contact', methods=['POST','GET'])
# def v_contacts():
# 	pass

app.run('0.0.0.0', port=8080, debug=True)
