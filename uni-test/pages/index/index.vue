<template>
	<view class="container">		
		<view class="navigators">
			<view class="uni-row">
				<view class="navigator">导航</view>
				<view class="navigator"><navigator  url="../image" open-type="navigate" >图片</navigator></view>
				<view class="navigator"><navigator  url="../videoplay" open-type="navigate" >视频</navigator></view>
				<view class="navigator"><navigator  url="../uniui" open-type="navigate" >图标</navigator></view>
				<view class="navigator" style="position: absolute;right: 10rpx;background-color: #F7F7F7;" v-if="islogin"><text>{{localname}},你好</text></view>
				<view class="navigator" style="position: absolute;right: 10rpx;background-color: #F7F7F7;color: #FF0000;" @click="gotologin" v-else>登录</view>
			</view>
			<view class="navigators">
				<view class="uni-row">
					<view class="navigator"><navigator  url="../refresh" open-type="navigate" >刷新</navigator></view>
					<view class="navigator"><navigator  url="../paltform" open-type="navigate" >平台</navigator></view>
					<view class="navigator"><navigator  url="../audioplay" open-type="switchTab" >音乐</navigator></view>
					<view class="navigator"><navigator  url="../canvas" open-type="navigate" >动画</navigator></view>
					
				</view>
			</view>
			
		</view>
		<swiper style="height: 200rpx; text-align: center; " :autoplay="autoplay" :duration="duration" :indicator-dots="indicator" :interval="interval">
				<swiper-item  v-for="(image,index) in images" :key='index'>
					<image :src="image.src"  mode="scaleToFill" style="width: 100%;height: 100%;"></image>
				</swiper-item>	
		</swiper>
		<view style="text-align: center;">
			<view>
				<text>指示点显示</text><switch :checked='indicator' @change="changeDot"></switch>
				<text>自动播放</text><switch :checked='autoplay' @change="changePlay"></switch>
			</view>
			<view>切换时间 {{duration}}ms</view><slider min="2000" max="10000" :value="duration" @change="changeDu"></slider>
			<view>切换间隔时间 {{interval}}ms</view><slider min="2000" max="10000" :value="interval" @change="changeIn"></slider>
		</view>
		<view style="text-align: center;">
			<text>性别</text>
			<radio-group @change="changeVa">
				<radio name='sex' checked="true" value="man" ></radio><text>男</text>
				<radio name='sex'  value="woman"></radio><text>女</text>
			</radio-group>
			<text>我是{{sex}}</text>
			<checkbox-group @change='changeLi'>
				<label v-for="(item,index) in items" :key="index">
					<view><checkbox :checked="item.checked" :value="item.name"  :name="item.name"></checkbox><text>{{item.name}}</text></view>
				</label>
			</checkbox-group>
			<view>我去过{{youselected}}</view>
			<text>地区选择器</text>
			<picker :value="indexofA" :range="youselect" @change="changePickC" ><view>{{youselect[indexofA]}}</view></picker>
			<text>时间选择器</text>
			<picker mode="time" :value="time" start="00:00" end="24:00" @change="changePickT"><view>{{time}}</view></picker>
			<text>日期选择器</text>
			<picker mode="date" :value="today" start="startDate" end="endDate" @change="changePickD"><view>{{today}}</view></picker>
		</view>

	</view>
</template>
<script>
	export default {
		data() {
			
			const currentDay=this.getTime('day')
			const currenTime=this.getTime('time')
			return {
				
				islogin:false,
				images:[{src:'../../static/学生登录逻辑.jpg'},
						{src:'../../static/教师逻辑.jpg'},
						{src:'../../static/教师登录首页.jpg'},
						{src:'../../static/学生登录首页.jpg'}],
				indicator:true,
				autoplay:true,
				duration:2000,
				interval:2000,
				localname:'',
				sex:'man',
				youselect:['中国'],
				indexofA:0,
				time:currenTime,
				today:currentDay,
				items: [{
				                        value: 'USA',
				                        name: '美国'
				                    },
				                    {
				                        value: 'CHN',
				                        name: '中国',
				                        checked: 'true'
				                    },
				                    {
				                        value: 'BRA',
				                        name: '巴西'
				                    },
				                    {
				                        value: 'JPN',
				                        name: '日本'
				                    },
				                    {
				                        value: 'ENG',
				                        name: '英国'
				                    },
				                    {
				                        value: 'FRA',
				                        name: '法国'
				                    }
				                ]
				
			}
		},
		onPullDownRefresh() {
			uni.navigateTo({
				url:'../index/index'
			})
		},
		onShareAppMessage() {
			console.log('aaa')
		},
		onLoad() {	
			this.islogin=global.isLogin()&&true
			if(this.islogin){
				this.localname=global.isLogin().username
			}
			else{
				
			}
		},
	
		computed:{

			youselected:function(){
			return this.youselect.join(',')
			},
			startDate:function(){
				var today=this.getTime('day')
				const oldday=today.replace(/\d+/,2000)
				return oldday
			},
			endDate:function(){
				var today=this.getTime('day')
				var nextyear=2+today.slice(0,4)
				const newday=today.replace(/\d+/,nextyear)
				return newday
			}
		},
		methods: {
			gotologin(){
				console.log('zheng')
				uni.switchTab({
					url:'../loginindex'
				})
			},
			changePlay(){
				this.autoplay=!this.autoplay
			},
			changeDot(){
				this.indicator=!this.indicator
			},
			changeDu(e){
				this.duration=e.target.value
			},
			changeIn(e){
				this.interval=e.target.value
			},
			changeVa(e){
				this.sex=e.target.value
			},
			changeLi(e){
				this.youselect=e.target.value
			},
			changePickC(e){
				this.indexofA=e.target.value
			},
			changePickT(e){
				this.time=e.target.value
			},
			changePickD(e){
				this.today=e.target.value
			},
			getTime(typ){
				let time=new Date()
				if(typ==='day'){
					let Y=time.getFullYear()
					let M=time.getMonth()+1
					let D=time.getDate()
					// console.log(`${Y}-${M}-${D}`)
					return `${Y}-${M}-${D}`
				}
				else{
					let H=time.getHours()
					let M=time.getMinutes()
					// console.log(`${H}:${M}`)
					return `${H}:${M}`
				}
			},
	},
}
</script>

<style>
	
</style>
