var  {MYSQL_Conf} =require('../config/db')
var mysql=require('mysql')
const conn=mysql.createConnection(MYSQL_Conf)
conn.connect()

const pageSize=4

class Exec {
    constructor() {
    }
    getPageSum(){
        var sql=`select count(id) as sum from blogs`
        var promise=new Promise((res,rej)=>{
            conn.query(sql,null,(err,data)=>{
                res(Math.ceil(data[0].sum/pageSize))
            })
        })
        return promise
    }
    getPage(par){
        var sql=`select * from blogs limit ?,?`
        var promise=new Promise((res,rej)=>{
            conn.query(sql,par,(err,data)=>{
                res(data)
            })
        })
        return promise
    }
    addBlog(par){
        var findsql=`select * from blogs where title='${par[0]}'`
        var sql='insert into blogs(title,content,createtime,author) values (?,?,?,?)'
        var promise=new Promise((res,rej)=>{
            conn.query(findsql,null,(err,data)=>{
                if (data[0]){
                    res(false)
                }else{
                    conn.query(sql,par,(err,data)=>{
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
    findBlogT(par){
            var sql='select * from blogs where title  =?'
            var promise=new Promise((res,rej)=>{
                conn.query(sql,par,(err,data)=>{
                    res(data[0])
                })
            })
        return promise
    }
    findBlogK(par){
        var sql='select * from blogs where  title like ? or content like ? limit ?,?'
        var promise=new Promise((res,rej)=>{
            conn.query(sql,par,(err,data)=>{
                res(data)
            })
        })
        return promise
    }
    findBlogM(par){
        var sql=`select * from blogs where author=? order by createtime`
        var promise=new Promise((res,rej)=>{
            conn.query(sql,par,(err,data)=>{
                res(data)
            })
        })
        return promise
    }

    delBlog(par){
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
    updateBlog(par){
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
    findUser(par) {
        var sql='select * from users where username=? and password=?'
        var promise=new Promise((res,rej)=>{
            conn.query(sql,par,(err,data)=>{
                res(data[0])
            })
        })
        return promise
    }
    addUser(par) {
        var findsql=`select * from users where username='${par[0]}'`
        var promise=new Promise((res,rej)=>{
            conn.query(findsql,null,(err,data)=>{
                if(!data[0]){
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
    delUser(par) {
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
    updateUser(par) {
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



