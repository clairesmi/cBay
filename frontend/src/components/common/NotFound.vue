<template>
<div id="not-found" class="h-screen flex flex-col justify-center items-center font-sans bg-red-200 text-orange-600">
  <h1 class="error-header p-5">Oops!</h1>
  <h2 class="error-text">Something went wrong...</h2>
<router-link to="/"><p class="error-text">Go back to homepage</p></router-link>
</div>
</template>
<script>
export default {
  
}
</script>
<style scoped>
.error-header {  
  font-family: 'Pacifico', cursive;
  font-size: 100px;
}
.error-text {
  font-family: 'Oswald', sans-serif;
  font-size: 22px;
  padding: 5px;
}

p {
  text-decoration: underline;
}

p:hover {
  transform: scale(1.1);
  color: black;
  opacity: 0.8;
}
</style>
