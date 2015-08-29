#coding=utf-8
from app import app, db
from flask import render_template, request, session, flash, redirect, url_for
from .forms import addForm
from .models import Post, Subject
import sqlite3

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from datetime import datetime

now = datetime.now()
numWeek = now.isoweekday()
Week = ''
if numWeek == 1:
	Week = '一'
elif numWeek == 2:
	Week = '二'
elif numWeek == 3:
	Week = '三'
elif numWeek == 4:
	Week = '四'
elif numWeek == 5:
	Week = '五'
elif numWeek == 6:
	Week = '六'
elif numWeek == 7:
	Week = '日'



@app.route('/')

@app.route('/index')
def index():
	#sjkpost = Post.query.filter(Post.subject == '数据库系统')
	sjkpost = db.session.execute("SELECT * FROM post WHERE subject='数据库系统' ORDER BY timestamp desc limit 1")
	czxtpost = db.session.execute("SELECT * FROM post WHERE subject='操作系统' ORDER BY timestamp desc limit 1")
	txwlpost = db.session.execute("SELECT * FROM post WHERE subject='计算机通信与网络' ORDER BY timestamp desc limit 1")
	sfpost = db.session.execute("SELECT * FROM post WHERE subject='算法设计与软件工程' ORDER BY timestamp desc limit 1")
	wjyypost = db.session.execute("SELECT * FROM post WHERE subject='微机应用系统及设计' ORDER BY timestamp desc limit 1")
	xhpost = db.session.execute("SELECT * FROM post WHERE subject='数字信号处理' ORDER BY timestamp desc limit 1")
	return render_template("index.html",
		Year = now.year,
		Month = now.month,
		Day = now.day,
		Weekday = Week,
		Weeknum = numWeek,
		sjkpost = sjkpost,
		czxtpost = czxtpost,
		txwlpost = txwlpost,
		sfpost = sfpost,
		wjyypost =wjyypost,
		xhpost = xhpost
		)

@app.route('/add', methods = ['GET', 'POST'])
def add():
	error = None
	form = addForm()
	if form.validate_on_submit():
		s = Subject.query.get(form.subject.data)
		if s == None:
			error = '无此科目名！'
		elif s.code != form.code.data:
			error = '科目代码错误！'
		else:
			post = Post(body = form.homework.data, timestamp = datetime.utcnow(), subject = form.subject.data, date=datetime.now().strftime('%c'))
			db.session.add(post)
			db.session.commit()
			error = '通知内容成功提交！'

	return render_template('add.html',
		title='添加作业通知',
		form = form,
		Year = now.year,
		Month = now.month,
		Day = now.day,
		Weekday = Week,
		error = error
		)

@app.route('/schedule')
def schedule():
	with sqlite3.connect('scheduleDB.db') as conn:
		cursor = conn.cursor()
		cursor.execute('SELECT className from classSchedule WHERE numWeek=?',[numWeek])
	className = cursor.fetchall()
	return render_template("schedule.html",
		title='课程表',
		Year = now.year,
		Month = now.month,
		Day = now.day,
		Weekday = Week,
		Weeknum = numWeek,
		className = className
		)

#Homework History Query
@app.route('/sjk')
def sjk():
	sjk = db.session.execute("SELECT * FROM post WHERE subject='数据库系统' ORDER BY timestamp desc")
	return render_template("history.html",
		title = '数据库系统',
		Year = now.year,
		Month = now.month,
		Day = now.day,
		Weekday = Week,
		Weeknum = numWeek,
		homework = sjk
		)
@app.route('/czxt')
def czxt():
	czxt = db.session.execute("SELECT * FROM post WHERE subject='操作系统' ORDER BY timestamp desc")
	return render_template("history.html",
		title = '操作系统',
		Year = now.year,
		Month = now.month,
		Day = now.day,
		Weekday = Week,
		Weeknum = numWeek,
		homework = czxt
		)
@app.route('/txwl')
def txwl():
	txwl = db.session.execute("SELECT * FROM post WHERE subject='计算机通信与网络' ORDER BY timestamp desc")
	return render_template("history.html",
		title = '计算机通信与网络',
		Year = now.year,
		Month = now.month,
		Day = now.day,
		Weekday = Week,
		Weeknum = numWeek,
		homework = txwl
		)
@app.route('/sf')
def sf():
	sf = db.session.execute("SELECT * FROM post WHERE subject='算法设计与软件工程' ORDER BY timestamp desc")
	return render_template("history.html",
		title = '算法设计与软件工程',
		Year = now.year,
		Month = now.month,
		Day = now.day,
		Weekday = Week,
		Weeknum = numWeek,
		homework = sf
		)
@app.route('/wjyy')
def wjyy():
	wjyy = db.session.execute("SELECT * FROM post WHERE subject='微机应用系统及设计' ORDER BY timestamp desc")
	return render_template("history.html",
		title = '微机应用系统及设计',
		Year = now.year,
		Month = now.month,
		Day = now.day,
		Weekday = Week,
		Weeknum = numWeek,
		homework = wjyy
		)
@app.route('/xh')
def xh():
	xh = db.session.execute("SELECT * FROM post WHERE subject='数字信号处理' ORDER BY timestamp desc")
	return render_template("history.html",
		title = '数字信号处理',
		Year = now.year,
		Month = now.month,
		Day = now.day,
		Weekday = Week,
		Weeknum = numWeek,
		homework = xh
		)