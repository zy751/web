<template>
	<view class="container">
		<view style="text-align: center;" >
			<view>listen to music</view>
			<audio id='myaudio' :src="shaonian.src" :author="shaonian.author" :name="shaonian.name" loop="true" controls :actions="audioAction" @timeupdate="getGtime" ></audio>
			<view>audio</view>
			<progress  show-info="true" :percent="percent" backgroundColor="#333333"></progress>
		</view>
	</view>
</template>
	
<script>
	export default{
		data(){
			return{
				audioAction:{method:'pause'},
				percent:0,
				getime:0,
				shaonian:{src:'https://img-cdn-qiniu.dcloud.net.cn/uniapp/audio/music.mp3',
						  author:'zy',
						  name:'致爱丽丝'},
			}
		},
		onReady() {
			const innerAudioContext = uni.createInnerAudioContext();
			innerAudioContext.autoplay = true;
			innerAudioContext.src = 'https://img-cdn-qiniu.dcloud.net.cn/uniapp/audio/music.mp3';
			innerAudioContext.onPlay(() => {
			  console.log('开始播放');
			});
			innerAudioContext.onError((res) => {
			  console.log(res.errMsg);
			  console.log(res.errCode);
			});
		},
		methods:{
			getGtime(e){
				this.getime=e.detail.currentTime.toFixed(0)
				this.percent=(e.detail.currentTime*100/e.detail.duration).toFixed(0)
			},
		}
	}
</script>

<style>

	
</style>
