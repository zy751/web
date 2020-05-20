const  express=require('express')
const Exec=require('./db/Mysql')
const body =require('body-parser')
const cookieP =require('cookie-parser')
const ejs=require('ejs')
const app=express()


app.engine('html',ejs.renderFile)

app.set('views','views')
app.use(body.urlencoded({extended:false}))
app.use(cookieP())
app.use('/public',express.static('public'))

app.use(require('./router/user'))
app.use(require('./router/blog'))

exec=new Exec()

app.listen(8000,function () {
    console.log('启动成功，请访问 http://127.0.0.1:8000')
})


