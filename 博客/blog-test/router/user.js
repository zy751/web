const express=require('express')
const router=express.Router()
const path=require('path')
const pro=require('crypto')

function checkLogin(req){
    return req.cookies.login
}

router.get('/login',(req,res)=>{
    var loginSta=checkLogin(req)
    if (loginSta){
        res.render('logSuc.html',{username:req.cookies.username,realname:req.cookies.realname})
    }else{
        res.render('login.html',{msg:''})
    }
})

router.post('/login',(req,res)=>{
    var username=req.body.username
    var pwd=req.body.pwd
    let md5=pro.createHash('md5')
    let newPas=md5.update(pwd).digest('hex')
    exec.findUser([username,newPas]).then((data)=>{
        var RES=data
        if (RES){
            res.cookie('username',username,{maxAge: 90000})
            res.cookie('login',true,{maxAge: 90000})
            res.cookie('realname',data.realname,{maxAge: 90000})
            res.render('logSuc.html',{username:username,realname:data.realname})
        }
        else{
            res.render('login.html',{msg:'用户名或密码错误'})
        }
    })

})

router.get('/register',(req,res)=>{
    res.render('register.html',{msg:''})
})

router.post('/register',(req,res)=>{
    let username=req.body.username
    let pwd=req.body.pwd
    let realname=req.body.realname
    let md5=pro.createHash('md5')
    let newPas=md5.update(pwd).digest('hex')
    exec.addUser([username,newPas,realname]).then(data=>{
        if(data){
            res.redirect('/login')
        }else{
            res.render('register.html',{msg:'用户名重复'})
        }
    })
})

router.get('/changePwd',(req,res)=>{
    res.render('changePwd.html',{msg:''})
})

router.post('/changePwd',(req,res)=>{
    let username=req.body.username
    let oldpwd=req.body.oldpwd
    let newpwd=req.body.newpwd
    let md5=pro.createHash('md5')
    let md6=pro.createHash('md5')
    let newoldPas=md5.update(oldpwd).digest('hex')
    let newnewPas=md6.update(newpwd).digest('hex')
    exec.updateUser([username,newnewPas,username,newoldPas]).then(data=>{
        if(data){
            res.redirect('/logout')
        }else{
            res.render('changePwd.html',{msg:'原密码错误'})
        }
    })
})

router.get('/logout',(req,res)=>{
    if (checkLogin(req)){
        for(let i in req.cookies){
            res.clearCookie(`${i}`)
        }
    }
    res.redirect('/login')
})

module.exports=router