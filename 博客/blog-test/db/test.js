var Exec=require('./Mysql')
exec=new Exec()
// exec.addUser(['zy2','1234','zy'])
// exec.findBlog([1]).then(data=>{
//     console.log(data)
// })
// var times=new Date()
// var time=`${times.getFullYear()}-${times.getMonth()+1}-${times.getDate()} ${times.getHours()}:${times.getMinutes()}:${times.getSeconds()}`
// // console.log(time)
// // exec.updateBlog(['hhah',time,'zy','12']).then(data=>{
// //     console.log(data)
// // })
exec.findBlog(['%12%','%ha%']).then(data=>{
    console.log(data)
})