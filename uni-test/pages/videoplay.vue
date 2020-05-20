<template>
	<view style="text-align: center;">
		<video style="width: 100%; height: 400rpx;" id='myvideo' enable-danmu :src='videosrc' danmu-btn='true' autoplay :danmu-list="danmuList"  controls loop='false'></video>
		<input style="margin: 4rpx;" v-model="danmuValue" placeholder="在此输入弹幕" />
		<view v-if="islogin">
			<radio-group @change="changeColor">		
				<radio v-for="color in colorList" :value="color.color" :key='color.text'>{{color.text}}</radio>		
			</radio-group>
		</view>
		<view v-else>
			<text>{{msg}}</text>
		</view>
		<button style="width: 50%;" type="primary" @click="sendDanmu">发送弹幕</button>
	</view>
</template>
<script>
	export default{
		data(){
			return {
				colorValue:'',
				islogin:'',
				msg:'',
				videosrc:'https://img.cdn.aliyun.dcloud.net.cn/guide/uniapp/%E7%AC%AC1%E8%AE%B2%EF%BC%88uni-app%E4%BA%A7%E5%93%81%E4%BB%8B%E7%BB%8D%EF%BC%89-%20DCloud%E5%AE%98%E6%96%B9%E8%A7%86%E9%A2%91%E6%95%99%E7%A8%8B@20181126.mp4',
				danmuValue:'',
				colorList:[{text:'红色',color:'#ff0000'},
							{text:'黄色',color:'#FFA200'},
							{text:'绿色',color:'#4CD964'},	
							{text:'蓝色',color:'#007AFF'}],
				danmuList:[{
				        text: '第 1s 出现的弹幕',
				        color: '#ff0000',
				        time: 1
				    },
				    {
				        text: '第 3s 出现的弹幕',
				        color: '#ff00ff',
				        time: 3
				    }
				],
			}
		},
		onLoad() {
			this.islogin=global.isLogin()
			if(!this.islogin){
				this.msg='登录可选弹幕颜色'
			}
		},
		onReady() {
			this.videotext=uni.createVideoContext('myvideo')
		},
		methods:{
			changeColor(e){
				this.colorValue=e.target.value
			},
			sendDanmu(){
				this.videotext.sendDanmu({
					text:this.danmuValue,
					color:this.colorValue
				}
				)
				this.danmuValue=''
			}
		}
		
	}
</script>

<style>
{
}
</style>
