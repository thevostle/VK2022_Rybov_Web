<template>
  <div class="shoppingCartItem">
    {{item.id}}
    <button class="shoppingCartItem__deleteButton" v-on:click="$emit('removeItem', item.id)">&times;</button>
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
    removeItem: function(event) {
      console.log('вы удалили товар');
    }
  }
};
</script>

<style>
  .shoppingCartItem__deleteButton {
    margin-left: 2rem;
  }
</style>
