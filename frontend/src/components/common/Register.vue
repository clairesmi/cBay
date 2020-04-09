<template>
<div id="register" class="flex flex-col items-center h-full">
  <h1 class="animated zoomInDown user-form-title text-6xl tracking-wide text-orange-600 mt-10 mb-10">Sign Up!</h1>
  <div class="form-wrapper h-64 w-2/4 flex">
    <form class="flex flex-col w-full justify-around p-40 text-gray-900" @submit.prevent="handleSubmit">
      <label>Username</label>
      <input 
      placeholder=" username"
      name="username"
      v-model="data.username"
      type="text"
      required="required"
      />
      <label>Email</label>
        <input 
      placeholder=" email"
      name="email"
      v-model="data.email"
      type="text"
      required="required"
      />
      <label>Password</label>
        <input 
      placeholder=" password"
      name="password"
      v-model="data.password"
      type="password"
      required="required"
      />
      <label>Confirm your password</label>
        <input 
      placeholder=" password confirmation"
      name="password_confirmation"
      v-model="data.password_confirmation"
      type="password"
      required="required"
      />
      <button type="submit" class="form-button p-5 mt-5">Submit</button>
    </form>
  </div>
</div>
  
</template>

<script>

import axios from 'axios'

export default {
  name: "register",
  data() {
    return {
      data: {
        username: '',
        email: '',
        password: '',
        password_confirmation: ''
      },
    }
  },

  methods: {

    async handleSubmit() {
      console.log(this.data)
      try {
        await axios.post('/api/register', this.data)
        this.$router.push('/login')
      }
      catch(err) {
        console.log(err)
      }
    },

  }
  
}
</script>
<style>
.user-form-title {
  font-family: 'Pacifico', cursive;
  font-size: 80px;
}
.form-wrapper {
  font-family: 'Oswald', sans-serif;
  font-size: 22px;
  letter-spacing: 0.5px;
  height: 400px;
}
input {
  margin: 5px 0px 10px 0px;
}
.form-button {
  padding: 5px 10px;
  box-shadow: 1px 1px 10px 1px gray;
  font-family: 'Oswald', sans-serif;
}
.form-button:hover {
  transform: scale(0.98);
  color: #dd6b33;
}

</style>