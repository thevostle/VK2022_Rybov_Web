<template>
  <div>
    <h2>Корзина</h2>
    <div class="shoppingCart">
        <shoppingCartItem v-for="item of items" v-bind:item="item" :key="item.id" v-on:removeItem="removeItem"/>
        <button class="shoppingCart__buttonBuy" >оформить заказ</button>
    </div>
  </div>
</template>

<script>
import shoppingCartItem from '@/components/shoppingCartItem';

export default {
  props: ['items'],
  components: {
    shoppingCartItem,
  },
  methods: {
    removeItem(id) {
      this.$emit('removeItem', id)
    }
  }
};
</script>

<style>
    .shoppingCart {
      margin-bottom: 5rem;
    }

    .shoppingCart__buttonBuy {
        margin-top: 3rem;
    }
</style>