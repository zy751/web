var  {MYSQL_Conf} =require('../config/db')
var mysql=require('mysql')
const conn=mysql.createConnection(MYSQL_Conf)
conn.connect()//连接数据库

const pageSize=4//规定一页的显示内容

class Exec {//创建数据库类
    constructor() {
    }
    getPageSum(){//获取数据可分的页数
        var sql=`select count(id) as sum from blogs`
        var promise=new Promise((res,rej)=>{
            conn.query(sql,null,(err,data)=>{
                res(Math.ceil(data[0].sum/pageSize))
            })
        })
        return promise
    }
    getPage(par){//返回指定页数内容
        var sql=`select * from blogs limit ?,?`
        var promise=new Promise((res,rej)=>{
            conn.query(sql,par,(err,data)=>{
                res(data)
            })
        })
        return promise
    }
    addBlog(par){//增加博客
        var findsql=`select * from blogs where title='${par[0]}'`//查询语句
        var sql='insert into blogs(title,content,createtime,author) values (?,?,?,?)'//增加语句
        var promise=new Promise((res,rej)=>{
            conn.query(findsql,null,(err,data)=>{//先查看新增博客主题是否存在
                if (data[0]){
                    res(false)
                }else{
                    conn.query(sql,par,(err,data)=>{//不存在就新增
                        if (data.affectedRows>0){
                            res(true)
                        }else {
                            res(false)
                        }
                    })
                }
            })

        })
        return promise
    }
    findBlogT(par){//根据标题查找博客
            var sql='select * from blogs where title  =?'
            var promise=new Promise((res,rej)=>{
                conn.query(sql,par,(err,data)=>{
                    res(data[0])
                })
            })
        return promise
    }
    findBlogK(par){//根据关键词查找博客
        var sql='select * from blogs where  title like ? or content like ? limit ?,?'
        var promise=new Promise((res,rej)=>{
            conn.query(sql,par,(err,data)=>{
                res(data)
            })
        })
        return promise
    }
    findBlogM(par){//查找自己的博客
        var sql=`select * from blogs where author=? order by createtime`
        var promise=new Promise((res,rej)=>{
            conn.query(sql,par,(err,data)=>{
                res(data)
            })
        })
        return promise
    }

    delBlog(par){//删除博客
        var sql='delete from blogs where title=?'
        var promise=new Promise((res,req)=>{
            conn.query(sql,par,(err,data)=>{
                if (data.affectedRows===0){
                    res(false)
                }else {
                    res(true)
                }
            })
        })
        return promise
    }
    updateBlog(par){//更新博客
        var sql='update blogs set content=? ,createtime=?,author=? where title=?'
        var promise=new Promise((res,rej)=>{
            conn.query(sql,par,(err,data)=>{
                if(data.affectedRows===0){
                    res(false)
                }else {
                    res(true)
                }
            })
        })
        return promise
    }
    findUser(par) {//查找用户信息
        var sql='select * from users where username=? and password=?'
        var promise=new Promise((res,rej)=>{
            conn.query(sql,par,(err,data)=>{
                res(data[0])
            })
        })
        return promise
    }
    addUser(par) {//新增用户
        var findsql=`select * from users where username='${par[0]}'`//先查询用户是否存在
        var promise=new Promise((res,rej)=>{
            conn.query(findsql,null,(err,data)=>{
                if(!data[0]){//不存在新增
                    var sql='insert into users(username,password,realname) values (?,?,?)'
                    conn.query(sql,par,(err,data)=>{
                        if(err){
                            console.log(err)
                            return 'error'
                        }else{
                            res(true)
                        }
                    })
                }
                else{
                    res(false)
                }

            })
        })
        return promise
    }
    delUser(par) {//删除用户
        var sql='delete from users where username=?'
        conn.query(sql,par,(err,data)=>{
            if(err){
                console.log(err)
                return 'error'
            }else{
                if(data.affectedRows===0){
                    console.log('不存在该用户')
                }else{
                    console.log('删除成功')
                }
            }
        })
    }
    updateUser(par) {//更新用户信息
        var sql='update users set username=? ,password=? where username=? and password=?'
        var promise=new Promise((res,rej)=>{
            conn.query(sql,par,(err,data)=>{
                if(err){
                    console.log(err)
                    return 'error'
                }else{
                    console.log(data)
                    if(data.affectedRows===0){
                        res(false)
                    }else{
                        res(true)
                    }
                }
            })
        })
        return promise

    }
}

module.exports=Exec



