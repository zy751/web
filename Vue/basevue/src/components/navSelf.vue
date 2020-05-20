<template>
  <div>
    <a v-for="(item,index) in items" :key="index" :class="item.active? 'active':
    ''" @click="changeActive(items,index)">{{item.text}}</a>
  </div>
</template>

<script>
export default {
  name: 'navself',
  data () {
    return {
      items: [
        {
          text: '首页',
          active: true
        },
        {
          text: '列表',
          active: false
        },
        {
          text: '关于',
          active: false
        },
        {
          text: '招聘',
          active: false
        }
      ]
    }
  },
  methods: {
    changeActive: function (items, index) {
      items.forEach(function (item) {
        item.active = false
      })
      items[index].active = true
    }
  }
}
</script>

<style scoped>
  a{
    display: inline-block;
    height: 60px;
    width: 140px;
    text-align: center;
    line-height: 60px;
    background-color: #42b983;
    margin: 10px;
    cursor: pointer;
  }
  .active{
    background-color: red;
  }
  a:hover {
    background-color: blue;
  }
</style>
