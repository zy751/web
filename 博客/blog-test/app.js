const  express=require('express')
const Exec=require('./db/Mysql')//导入数据库
const body =require('body-parser')//解析请求参数
const cookieP =require('cookie-parser')//解析cookie
const ejs=require('ejs')
app.engine('html',ejs.renderFile)//使得可以使用html代码直接渲染
const app=express()



app.set('views','views')//视图代码存放路径
app.use(body.urlencoded({extended:false}))
app.use(cookieP())//app实例使用上面导入的
app.use('/public',express.static('public'))

app.use(require('./router/user'))
app.use(require('./router/blog'))//导入编写的路由

exec=new Exec()

app.listen(8000,function () {
    console.log('启动成功，请访问 http://127.0.0.1:8000')
})


