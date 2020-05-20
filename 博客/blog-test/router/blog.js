const express=require('express')
const blogRouter=express.Router()
const path=require('path')


function checkLogin(req){
    return req.cookies.login
}

blogRouter.get('/',(req,res)=>{
    var username=req.cookies.username
    res.render('index.html',{username:username})
})

blogRouter.get('/blog/index',(req,res)=>{
    if (checkLogin(req)){
        exec.getPageSum().then(data=>{
            var pageSum=data
            var currentPage,prePage,nextPage
            if(req.query.page){
                currentPage=parseInt(req.query.page)
            }
            else{
                currentPage=1
            }
            if(currentPage===1){
                prePage=1
                nextPage=2
            }
            else if(currentPage===pageSum){
                prePage=currentPage-1
                nextPage=pageSum
            }
            else{
                prePage=currentPage-1
                nextPage=currentPage+1
            }
            exec.getPage([(currentPage-1)*4,4]).then(data=>{
                res.render('blogIndex.html',{username:req.cookies.username,
                    realname:req.cookies.realname,
                    prePage:prePage,nextPage:nextPage,
                    dataS:data,currentPage:currentPage,
                    pageSum:pageSum})
            })

        })
    }else{
        res.render('login.html',{msg:''})
    }
})

blogRouter.get('/blog/detail',(req,res)=>{
    var title=req.query.title
    exec.findBlogT([title]).then(data=>{
        res.render('blogDetail.html',{title:data.title,content:data.content,author:data.author,createT:data.createtime})
    })
})

blogRouter.get('/blog/search',(req,res)=>{
    //还可完善，搜索结果多页
    var keyword=req.query.keyword
    if(req.query.page){
        var page=req.query.page
    }else {
        var page=1
    }
    console.log(keyword)
    exec.findBlogK([`%${keyword}%`,`%${keyword}%`,(page-1)*4,4]).then(data=>{
            res.render('searchIndex.html',{dataS:data,pageSum:1})
    })
})

blogRouter.get('/blog/searchMY',(req,res)=>{
    var author=req.cookies.username
    exec.findBlogM([author]).then(data=>{
        res.render('searchIndex.html',{dataS:data,pageSum:1})
    })
})
module.exports=blogRouter