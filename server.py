# Flask : flask에서 Flask라는 class import
# request : 웹브라우저가 웹서버로 전송한 요청 확인 가능
# redirect : 웹 페이지 이동
from flask import Flask, request, redirect



app = Flask(__name__) # Flask 클래스의 객체 생성 후 인자 : 모듈이나 패키지 이름 => 플라스크에서 템플릿이나 정적파일 찾을 때 필요



@app.route('/') # 생성한 객체의 route 설정 = URL 설정
def index(): # 함수 생성
	return 'Hello World!'




# variable 이름 정한 뒤 받는 함수의 파라미터 중에 동일한 이름의 파라미터가 그 값을 받을 수 있게 해줌
# route에 패턴(<id>)을 적으면 함수에 들어오는 파라미터는 무조건 문자열
# 패턴 차원에서 정수(int)로 지정해줘도 됨(int:) => 플라스크가 자동으로 int로 바꿔줌
@app.route('/read/<int:id>')
def read(id):
	return 'Read ' + id

nextId = 4
topics = [
	{'id': 1, 'title': 'aaa', 'body': 'aaa is ...'},
	{'id': 2, 'title': 'bbb', 'body': 'bbb is ...'},
	{'id': 3, 'title': 'ccc', 'body': 'ccc is ...'}
]

# 중복되는 코드 함수로 만들기
def template(contents, content):
	# ''' : 멀티라인 string
	return f'''<!doctype html>
		<html>
			<body>
				<h1><a href="/">WEB</a></h1>
				<ol>
					{contents}
				</ol>
				{content}
			</body>
		</html>
	'''

def getContents():
	liTags = ''
	for topic in topics:
		liTags = liTags + f'<li><a href="read/{topic["id"]}">{topic["title"]}</li>' # 문자열을 변수와 함께 섞을 때 f string 사용
		# liTags = liTags + '<li>' + topic['title'] + '</li>'
	return liTags

@app.route('/test')
def test1():
	title = ''
	body = ''
	for topic in topics:
		if id == topic['id']:
			title = topic['title']
			body = topic['body']
			break

	return template(getContents(), f'<h2>{title}</h2>{body}')
				

@app.route('/create', methods=['GET', 'POST'])
def create():
	if request.method == 'GET':
		content = '''
			<form action="/create" method="POST>
				<p><input type="text" name="title" placeholder="title"></p>
				<p><textarea name="body" placeholder="body"></textarea></p>
				<p><input type="submit" value="create"></p>
			</form>
		'''
		return template(getContents(), content)
	elif request.method == 'POST':
		# nextId : 전역변수
		global nextId

		# request form을 이용해서 post 방식으로 전송한 데이터 가져올 수 있음
		title = request.form['title']
		body = request.form['body']
		newTopic = {'id': nextId, 'title': title, 'body': body}
		topics.append(newTopic)
		url = '/read/' + str(nextId)
		nextId = nextId + 1 # 전역변수를 바꿀 때는 전역 변수가 사용되기 이전의 코드에서 global로 전역변수로 지정
		return redirect(url)



#if __name__ == '__main__': # 실행한 서버가 현재 동작되는 유일한 서버
app.run() # run() 함수로 어플리케이션을 로컬 서버로 실행(기본 포트 5000)
