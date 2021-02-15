<template>
  <dialog open>
    <header>
      <h1>{{ customerName }}</h1>
    </header>
    <p>{{ customerDescription }}</p>
    <button @click="$emit('hide-details', true)">Return to list</button>
  </dialog>
</template>

<script>
export default {
  props: {
    customerName: {
      type: String,
      required: true,
    },
    customerDescription: {
      type: String,
      required: false,
    },
  },
  emits: ["hide-details"],
};
</script>

<style scoped>
dialog {
  margin: 0;
  position: fixed;
  top: 20vh;
  left: 30%;
  width: 40%;
  background-color: white;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);
  padding: 1rem;
}
</style>
