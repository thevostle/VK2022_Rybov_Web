<template>
  <div class="productItem">
    <img class="productItem__photo" v-bind:src="item.image_link">
    <div class="productItem__title">{{ item.title }}</div>
    <div class="productItem__price">{{ item.price }}</div>
    <div class="productItem__buttonBuyWrapper" v-if="item.count > 0">
      <button class="productItem__buttonBuy" v-on:click="$emit('addToCart', item.id)" >Добавить</button>
    </div>
    <p v-else>нет в наличии</p>
  </div>
</template>

<script>
export default {
  props: {
    item: {
      type: Object,
      required: true,
    },
  },
  methods: {
    addToCart: function(event) {
      alert('вы добавили товар');
    }
  }
};
</script>

<style>
    .productItem {
        border: 2px;
        height: 8rem;
        width: 15rem;
        padding: 2rem 3rem;
        box-shadow: 0 0 3px rgba(0,0,0,0.5);
        height: 15rem;
    }

    .productItem__photo {
        width: 10rem;
        height: 8rem;
    }

    .productItem__title {
      margin-bottom: 1rem;
    }

    .productItem__price {
      margin-bottom: 1rem;
    }

    .productItem__buttonBuy {
      background-color: rgb(255, 119, 50);
      height: 3rem;
      width: 100%;
    }

</style>
