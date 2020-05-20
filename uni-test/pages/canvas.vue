<template>
	<view>
		<canvas canvas-id="smile" style="width: 300px; height: 200px;"></canvas>
		<canvas canvas-id="timeclock" style="width: 300px; height: 300px;"></canvas>
	</view>
</template>

<script>
	export default{
		onReady() {
			function drawSmile(){
				var context=uni.createCanvasContext('smile')
				context.setStrokeStyle("#00ff00")
				context.setLineWidth(5)
				context.rect(0, 0, 200, 200)
				context.stroke()
				context.setStrokeStyle("#ff0000")
				context.setLineWidth(2)
				context.moveTo(160, 100)
				context.arc(100, 100, 60, 0, 2 * Math.PI, true)
				context.moveTo(140, 100)
				context.arc(100, 100, 40, 0, Math.PI, false)
				context.moveTo(85, 80)
				context.arc(80, 80, 5, 0, 2 * Math.PI, true)
				context.moveTo(125, 80)
				context.arc(120, 80, 5, 0, 2 * Math.PI, true)
				context.stroke()
				context.draw()
			}
			drawSmile()
			uni.requestAnimationFrame
			function drawAllHands(ctx){
				 let pi = Math.PI;
 
    ctx.clearRect(0, 0, 300, 300); //清除所有内容
    ctx.save();
 
    ctx.translate(150, 150); //一定坐标原点到原来的中心
    ctx.beginPath();
    ctx.arc(0, 0, 148, 0, 2 * pi); //绘制圆周
    ctx.stroke();
    ctx.closePath();
 
    for (let i = 0; i < 60; i++){//绘制刻度。
        ctx.save();
        ctx.rotate(-pi / 2 + i * pi / 30);  //旋转坐标轴。坐标轴x的正方形从 向上开始算起
        ctx.beginPath();
        ctx.moveTo(110, 0);
        ctx.lineTo(140, 0);
        ctx.lineWidth = i % 5 ? 2 : 4;
        ctx.strokeStyle = i % 5 ? "blue" : "red";
        ctx.stroke();
        ctx.closePath();
        ctx.restore();
    }
    ctx.restore();
			}
	}
}
</script>

<style>
</style>
