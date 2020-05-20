<script>
	global.isLogin=function(){
		try{
			var username=uni.getStorageSync('userinfo')
		}catch(e){
			
		}		
		if(username==''){
			return false
		}else{
			return username
		}
	}
export default {
	onLaunch: function() {
		console.log('App Launch');
	},
	onShow: function() {
		console.log('App Show');
	},
	onHide: function() {
		console.log('App Hide');
	},
	globalData:{
		loginStatus:false
	},
};

</script>

<style>
/* 解决头条小程序组件内引入字体不生效的问题 */
/* #ifdef MP-TOUTIAO */
@font-face {
	font-family: uniicons;
	src: url('/static/uni.ttf');
}
/* #endif */
.navigator:hover{
		background-color: #007AFF;
	}
	.navigator{
		width: 18%;
		height: 40rpx;
		line-height: 40rpx;
		background-color: #4CD964;
		margin: 1rpx;
	}
	.container {
		text-align: center;
		padding: 2px;
		font-size: 14px;
		line-height: 24px;
	}
	.uni-row{
		display: flex;
		flex-direction: row;
		text-align: center;
		line-height: 50rpx;
	}
	.uni-colum{
		display: flex;
		flex-direction: column;
		text-align: center;
		line-height: 50rpx;
	}
	.uni-bg-green{
		background-color: #4CD964;
		width: 33%;
		height: 50rpx;
	}
	.uni-bg-red{
		background-color: #DD524D;
		width: 33%;
		height: 50rpx;
	}
	.uni-bg-blue {
		background-color: #007AFF;
		width: 33%;
		height: 50rpx;
	}
	button{
		width: 50%;
	}
</style>
